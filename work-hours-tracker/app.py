"""
Main GUI application for work hours tracker.
A simple desktop application to track work hours on different tasks.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from database import Database
from task_manager import TaskManager
from timer import Timer


class WorkHoursApp:
    """Main application window for work hours tracker."""
    
    def __init__(self, root):
        """Initialize the application."""
        self.root = root
        self.root.title("Work Hours Tracker")
        self.root.geometry("900x600")
        
        # Initialize components
        self.db = Database()
        self.task_manager = TaskManager(self.db)
        self.timer = Timer(self.db)
        
        # Selected task ID
        self.selected_task_id = None
        
        # Setup UI
        self.setup_ui()
        
        # Start timer update loop
        self.update_timer_display()
        
        # Bind cleanup on close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_ui(self):
        """Setup the user interface."""
        # Create main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Timer section (top)
        self.setup_timer_section(main_frame)
        
        # Left panel - Tasks
        self.setup_tasks_panel(main_frame)
        
        # Right panel - Tabs for summary and timespans
        self.setup_right_panel(main_frame)
    
    def setup_timer_section(self, parent):
        """Setup timer display and controls."""
        timer_frame = ttk.LabelFrame(parent, text="Timer", padding="10")
        timer_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Timer display
        self.timer_label = ttk.Label(
            timer_frame, 
            text="00:00:00", 
            font=("Arial", 24, "bold")
        )
        self.timer_label.grid(row=0, column=0, padx=10)
        
        # Current task label
        self.current_task_label = ttk.Label(
            timer_frame, 
            text="No task selected", 
            font=("Arial", 12)
        )
        self.current_task_label.grid(row=0, column=1, padx=10)
        
        # Play/Stop button
        self.play_button = ttk.Button(
            timer_frame, 
            text="▶ Play", 
            command=self.toggle_timer,
            width=10
        )
        self.play_button.grid(row=0, column=2, padx=10)
    
    def setup_tasks_panel(self, parent):
        """Setup tasks tree panel."""
        tasks_frame = ttk.LabelFrame(parent, text="Tasks", padding="10")
        tasks_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 5))
        tasks_frame.columnconfigure(0, weight=1)
        tasks_frame.rowconfigure(0, weight=1)
        
        # Tasks tree
        self.tasks_tree = ttk.Treeview(tasks_frame, selectmode='browse')
        self.tasks_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar for tasks
        tasks_scroll = ttk.Scrollbar(tasks_frame, orient=tk.VERTICAL, command=self.tasks_tree.yview)
        tasks_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.tasks_tree.configure(yscrollcommand=tasks_scroll.set)
        
        # Bind selection
        self.tasks_tree.bind('<<TreeviewSelect>>', self.on_task_select)
        
        # Task buttons
        button_frame = ttk.Frame(tasks_frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=(5, 0))
        
        ttk.Button(button_frame, text="Add Root Task", command=self.add_root_task).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Add Child Task", command=self.add_child_task).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Delete Task", command=self.delete_task).pack(side=tk.LEFT, padx=2)
        ttk.Button(button_frame, text="Refresh", command=self.refresh_tasks).pack(side=tk.LEFT, padx=2)
        
        # Initial load
        self.refresh_tasks()
    
    def setup_right_panel(self, parent):
        """Setup right panel with tabs."""
        notebook = ttk.Notebook(parent)
        notebook.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Summary tab
        summary_frame = ttk.Frame(notebook, padding="10")
        notebook.add(summary_frame, text="Summary")
        self.setup_summary_tab(summary_frame)
        
        # Timespans tab
        timespans_frame = ttk.Frame(notebook, padding="10")
        notebook.add(timespans_frame, text="All Timespans")
        self.setup_timespans_tab(timespans_frame)
    
    def setup_summary_tab(self, parent):
        """Setup summary tab showing task hours."""
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        
        # Summary tree
        self.summary_tree = ttk.Treeview(
            parent, 
            columns=('Hours',), 
            selectmode='browse'
        )
        self.summary_tree.heading('#0', text='Task')
        self.summary_tree.heading('Hours', text='Total Hours')
        self.summary_tree.column('Hours', width=100)
        self.summary_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar
        summary_scroll = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.summary_tree.yview)
        summary_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.summary_tree.configure(yscrollcommand=summary_scroll.set)
        
        # Refresh button
        ttk.Button(parent, text="Refresh Summary", command=self.refresh_summary).grid(row=1, column=0, pady=(5, 0))
        
        self.refresh_summary()
    
    def setup_timespans_tab(self, parent):
        """Setup timespans tab showing all time entries."""
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        
        # Timespans tree
        columns = ('Task', 'Start', 'End', 'Duration')
        self.timespans_tree = ttk.Treeview(
            parent, 
            columns=columns, 
            show='headings',
            selectmode='browse'
        )
        
        self.timespans_tree.heading('Task', text='Task')
        self.timespans_tree.heading('Start', text='Start Time')
        self.timespans_tree.heading('End', text='End Time')
        self.timespans_tree.heading('Duration', text='Duration')
        
        self.timespans_tree.column('Task', width=200)
        self.timespans_tree.column('Start', width=150)
        self.timespans_tree.column('End', width=150)
        self.timespans_tree.column('Duration', width=100)
        
        self.timespans_tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Bind double-click event for editing
        self.timespans_tree.bind('<Double-Button-1>', self.on_timespan_double_click)
        
        # Scrollbar
        timespans_scroll = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.timespans_tree.yview)
        timespans_scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.timespans_tree.configure(yscrollcommand=timespans_scroll.set)
        
        # Refresh button
        ttk.Button(parent, text="Refresh Timespans", command=self.refresh_timespans).grid(row=1, column=0, pady=(5, 0))
        
        self.refresh_timespans()
    
    def refresh_tasks(self):
        """Refresh the tasks tree display."""
        # Clear existing items
        for item in self.tasks_tree.get_children():
            self.tasks_tree.delete(item)
        
        # Get task tree
        task_tree = self.task_manager.get_task_tree()
        
        # Add tasks to tree
        for task_id, indented_name, level in task_tree:
            self.tasks_tree.insert('', 'end', iid=str(task_id), text=indented_name, values=(task_id,))
    
    def refresh_summary(self):
        """Refresh the summary display."""
        # Clear existing items
        for item in self.summary_tree.get_children():
            self.summary_tree.delete(item)
        
        # Get task tree and add hours
        task_tree = self.task_manager.get_task_tree()
        
        for task_id, indented_name, level in task_tree:
            hours = self.db.get_task_total_hours(task_id, include_children=True)
            self.summary_tree.insert(
                '', 'end', 
                text=indented_name, 
                values=(f"{hours:.2f}",)
            )
    
    def refresh_timespans(self):
        """Refresh the timespans display."""
        # Clear existing items
        for item in self.timespans_tree.get_children():
            self.timespans_tree.delete(item)
        
        # Get all timespans
        timespans = self.db.get_all_timespans()
        
        for ts in timespans:
            task_name = ts['task_name']
            start_time = datetime.fromisoformat(ts['start_time']).strftime('%Y-%m-%d %H:%M:%S')
            
            if ts['end_time']:
                end_time = datetime.fromisoformat(ts['end_time']).strftime('%Y-%m-%d %H:%M:%S')
                start_dt = datetime.fromisoformat(ts['start_time'])
                end_dt = datetime.fromisoformat(ts['end_time'])
                duration_seconds = (end_dt - start_dt).total_seconds()
                duration = f"{duration_seconds / 3600:.2f}h"
            else:
                end_time = "Running..."
                duration = "N/A"
            
            self.timespans_tree.insert(
                '', 'end',
                iid=str(ts['id']),
                values=(task_name, start_time, end_time, duration)
            )
    
    def on_task_select(self, event):
        """Handle task selection."""
        selection = self.tasks_tree.selection()
        if selection:
            self.selected_task_id = int(selection[0])
    
    def on_timespan_double_click(self, event):
        """Handle double-click on timespan to edit task."""
        selection = self.timespans_tree.selection()
        if not selection:
            return
        
        timespan_id = int(selection[0])
        
        # Create a simple dialog to select new task
        new_task_id = self.show_task_selection_dialog()
        
        if new_task_id is not None:
            # Update the timespan with new task
            self.db.update_timespan_task(timespan_id, new_task_id)
            # Refresh displays
            self.refresh_timespans()
            self.refresh_summary()
            messagebox.showinfo("Success", "Timespan task updated successfully!")
    
    def show_task_selection_dialog(self):
        """Show dialog to select a task. Returns selected task_id or None."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Select Task")
        dialog.geometry("400x500")
        dialog.transient(self.root)
        dialog.grab_set()
        
        selected_task_id = [None]  # Use list to store result from nested function
        
        # Create frame for tree
        frame = ttk.Frame(dialog, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)
        
        # Label
        ttk.Label(frame, text="Select a task:", font=("Arial", 12)).pack(pady=(0, 10))
        
        # Task tree
        tree = ttk.Treeview(frame, selectmode='browse')
        tree.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Populate tree with tasks
        task_tree = self.task_manager.get_task_tree()
        for task_id, indented_name, level in task_tree:
            tree.insert('', 'end', iid=str(task_id), text=indented_name)
        
        # Button frame
        button_frame = ttk.Frame(dialog, padding="10")
        button_frame.pack(fill=tk.X)
        
        def on_select():
            selection = tree.selection()
            if selection:
                selected_task_id[0] = int(selection[0])
                dialog.destroy()
            else:
                messagebox.showwarning("No Selection", "Please select a task.")
        
        def on_cancel():
            dialog.destroy()
        
        ttk.Button(button_frame, text="Select", command=on_select).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Cancel", command=on_cancel).pack(side=tk.LEFT, padx=5)
        
        # Wait for dialog to close
        self.root.wait_window(dialog)
        
        return selected_task_id[0]
    
    def add_root_task(self):
        """Add a new root task."""
        name = simpledialog.askstring("Add Root Task", "Enter task name:")
        if name:
            self.task_manager.add_task(name, parent_id=None)
            self.refresh_tasks()
            self.refresh_summary()
    
    def add_child_task(self):
        """Add a child task to selected task."""
        if self.selected_task_id is None:
            messagebox.showwarning("No Selection", "Please select a parent task first.")
            return
        
        name = simpledialog.askstring("Add Child Task", "Enter task name:")
        if name:
            self.task_manager.add_task(name, parent_id=self.selected_task_id)
            self.refresh_tasks()
            self.refresh_summary()
    
    def delete_task(self):
        """Delete selected task."""
        if self.selected_task_id is None:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return
        
        if messagebox.askyesno("Confirm Delete", "Delete this task and all its children?"):
            self.task_manager.delete_task(self.selected_task_id)
            self.selected_task_id = None
            self.refresh_tasks()
            self.refresh_summary()
    
    def toggle_timer(self):
        """Toggle timer play/stop."""
        if self.timer.is_running:
            self.timer.stop()
            self.play_button.config(text="▶ Play")
            self.current_task_label.config(text="No task selected")
            self.refresh_timespans()
            self.refresh_summary()
        else:
            if self.selected_task_id is None:
                messagebox.showwarning("No Selection", "Please select a task first.")
                return
            
            self.timer.start(self.selected_task_id)
            self.play_button.config(text="⏸ Stop")
            task_path = self.task_manager.get_task_path(self.selected_task_id)
            self.current_task_label.config(text=f"Task: {task_path}")
    
    def update_timer_display(self):
        """Update timer display every second.
        
        This runs continuously to keep the display updated, showing either
        the elapsed time (when running) or 00:00:00 (when stopped).
        """
        if self.timer.is_running:
            self.timer_label.config(text=self.timer.format_elapsed_time())
        else:
            self.timer_label.config(text="00:00:00")
        
        # Schedule next update (always runs to keep display current)
        self.root.after(1000, self.update_timer_display)
    
    def on_closing(self):
        """Handle application closing."""
        if self.timer.is_running:
            if messagebox.askyesno("Timer Running", "Timer is running. Stop and exit?"):
                self.timer.stop()
            else:
                return
        
        self.db.close()
        self.root.destroy()


def main():
    """Main entry point."""
    root = tk.Tk()
    app = WorkHoursApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
