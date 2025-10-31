"""
Task management module for work hours tracker.
Handles task tree structure and operations.
"""

from typing import List, Optional, Tuple
from database import Database


class TaskManager:
    """Manages tasks in a hierarchical tree structure."""
    
    def __init__(self, database: Database):
        """Initialize task manager with database."""
        self.db = database
    
    def add_task(self, name: str, parent_id: Optional[int] = None) -> int:
        """Add a new task."""
        return self.db.add_task(name, parent_id)
    
    def delete_task(self, task_id: int):
        """Delete a task."""
        self.db.delete_task(task_id)
    
    def get_task_path(self, task_id: int) -> str:
        """Get full path of a task (e.g., 'work/client1/feature/playtech')."""
        path_parts = []
        current_id = task_id
        
        while current_id is not None:
            task = self.db.get_task_by_id(current_id)
            if task:
                path_parts.insert(0, task['name'])
                current_id = task['parent_id']
            else:
                break
        
        return '/'.join(path_parts)
    
    def get_task_tree(self) -> List[Tuple[int, str, int]]:
        """
        Get tasks organized as a tree structure.
        Returns list of tuples: (task_id, indented_name, level)
        """
        all_tasks = self.db.get_all_tasks()
        
        # Build tree structure
        tree = []
        root_tasks = [t for t in all_tasks if t['parent_id'] is None]
        
        def add_task_and_children(task, level=0):
            tree.append((task['id'], '  ' * level + task['name'], level))
            children = [t for t in all_tasks if t['parent_id'] == task['id']]
            for child in children:
                add_task_and_children(child, level + 1)
        
        for root in root_tasks:
            add_task_and_children(root)
        
        return tree
    
    def get_children(self, parent_id: Optional[int]) -> List:
        """Get direct children of a task (or root tasks if parent_id is None)."""
        all_tasks = self.db.get_all_tasks()
        return [t for t in all_tasks if t['parent_id'] == parent_id]
