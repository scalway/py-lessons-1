"""
Database module for work hours tracker.
Handles SQLite database operations for tasks and timespans.
"""

import sqlite3
from datetime import datetime
from typing import List, Optional, Tuple


class Database:
    """Manages SQLite database for tasks and timespans."""
    
    def __init__(self, db_path: str = "workhours.db"):
        """Initialize database connection and create tables if needed."""
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self._create_tables()
    
    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        cursor = self.connection.cursor()
        
        # Tasks table with tree structure using parent_id
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                parent_id INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (parent_id) REFERENCES tasks(id) ON DELETE CASCADE
            )
        """)
        
        # Timespans table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS timespans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_id INTEGER NOT NULL,
                start_time TIMESTAMP NOT NULL,
                end_time TIMESTAMP,
                FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
            )
        """)
        
        self.connection.commit()
    
    def add_task(self, name: str, parent_id: Optional[int] = None) -> int:
        """Add a new task and return its ID."""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (name, parent_id) VALUES (?, ?)",
            (name, parent_id)
        )
        self.connection.commit()
        return cursor.lastrowid
    
    def get_all_tasks(self) -> List[sqlite3.Row]:
        """Get all tasks from database."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tasks ORDER BY id")
        return cursor.fetchall()
    
    def get_task_by_id(self, task_id: int) -> Optional[sqlite3.Row]:
        """Get a specific task by ID."""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        return cursor.fetchone()
    
    def delete_task(self, task_id: int):
        """Delete a task and its children (cascading)."""
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.connection.commit()
    
    def start_timespan(self, task_id: int) -> int:
        """Start a new timespan for a task."""
        cursor = self.connection.cursor()
        start_time = datetime.now().isoformat()
        cursor.execute(
            "INSERT INTO timespans (task_id, start_time) VALUES (?, ?)",
            (task_id, start_time)
        )
        self.connection.commit()
        return cursor.lastrowid
    
    def stop_timespan(self, timespan_id: int):
        """Stop a running timespan."""
        cursor = self.connection.cursor()
        end_time = datetime.now().isoformat()
        cursor.execute(
            "UPDATE timespans SET end_time = ? WHERE id = ?",
            (end_time, timespan_id)
        )
        self.connection.commit()
    
    def update_timespan_task(self, timespan_id: int, new_task_id: int):
        """Update the task associated with a timespan."""
        cursor = self.connection.cursor()
        cursor.execute(
            "UPDATE timespans SET task_id = ? WHERE id = ?",
            (new_task_id, timespan_id)
        )
        self.connection.commit()
    
    def get_timespans_for_task(self, task_id: int) -> List[sqlite3.Row]:
        """Get all timespans for a specific task."""
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT * FROM timespans WHERE task_id = ? ORDER BY start_time DESC",
            (task_id,)
        )
        return cursor.fetchall()
    
    def get_all_timespans(self) -> List[sqlite3.Row]:
        """Get all timespans with task names."""
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT t.id, t.task_id, t.start_time, t.end_time, tasks.name as task_name
            FROM timespans t
            JOIN tasks ON t.task_id = tasks.id
            ORDER BY t.start_time DESC
        """)
        return cursor.fetchall()
    
    def get_task_total_hours(self, task_id: int, include_children: bool = True) -> float:
        """Calculate total hours for a task and optionally its children."""
        cursor = self.connection.cursor()
        
        if include_children:
            # Get all child task IDs recursively
            task_ids = self._get_task_and_children_ids(task_id)
        else:
            task_ids = [task_id]
        
        total_seconds = 0
        for tid in task_ids:
            cursor.execute(
                "SELECT start_time, end_time FROM timespans WHERE task_id = ?",
                (tid,)
            )
            timespans = cursor.fetchall()
            
            for ts in timespans:
                if ts['end_time']:
                    start = datetime.fromisoformat(ts['start_time'])
                    end = datetime.fromisoformat(ts['end_time'])
                    total_seconds += (end - start).total_seconds()
        
        return total_seconds / 3600.0  # Convert to hours
    
    def _get_task_and_children_ids(self, task_id: int) -> List[int]:
        """Recursively get task ID and all its children IDs."""
        cursor = self.connection.cursor()
        task_ids = [task_id]
        
        cursor.execute("SELECT id FROM tasks WHERE parent_id = ?", (task_id,))
        children = cursor.fetchall()
        
        for child in children:
            task_ids.extend(self._get_task_and_children_ids(child['id']))
        
        return task_ids
    
    def close(self):
        """Close database connection."""
        self.connection.close()
