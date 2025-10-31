"""
Timer module for work hours tracker.
Handles timing functionality for tracking work hours.
"""

from datetime import datetime, timedelta
from typing import Optional
from database import Database


class Timer:
    """Manages time tracking for tasks."""
    
    def __init__(self, database: Database):
        """Initialize timer with database."""
        self.db = database
        self.current_task_id: Optional[int] = None
        self.current_timespan_id: Optional[int] = None
        self.start_time: Optional[datetime] = None
        self.is_running = False
    
    def start(self, task_id: int):
        """Start timer for a task."""
        if self.is_running:
            self.stop()
        
        self.current_task_id = task_id
        self.start_time = datetime.now()
        self.current_timespan_id = self.db.start_timespan(task_id)
        self.is_running = True
    
    def stop(self):
        """Stop the current timer."""
        if not self.is_running or self.current_timespan_id is None:
            return
        
        self.db.stop_timespan(self.current_timespan_id)
        self.is_running = False
        self.current_task_id = None
        self.current_timespan_id = None
        self.start_time = None
    
    def get_elapsed_time(self) -> timedelta:
        """Get elapsed time for current running timer."""
        if not self.is_running or self.start_time is None:
            return timedelta(0)
        
        return datetime.now() - self.start_time
    
    def format_elapsed_time(self) -> str:
        """Format elapsed time as HH:MM:SS."""
        elapsed = self.get_elapsed_time()
        total_seconds = int(elapsed.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
