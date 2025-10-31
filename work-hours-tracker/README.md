# Work Hours Tracker

A simple Python desktop application for tracking work hours across different tasks organized in a tree structure.

## Features

- **Timer with Play/Stop**: Start and stop time tracking for tasks
- **Hierarchical Task Management**: Organize tasks in a tree structure (e.g., work/client1/feature/playtech)
- **SQLite Database**: All timespans and tasks are saved to a local SQLite database
- **Summary View**: See total hours for each task including children
- **Timespans View**: View all recorded time entries with start/end times and durations

## Project Structure

The application is modular with separate concerns in different files:

```
work-hours-tracker/
├── app.py            # Main GUI application (tkinter)
├── database.py       # SQLite database operations
├── task_manager.py   # Task tree structure management
├── timer.py          # Timer logic for tracking time
└── README.md         # This file
```

## Requirements

- Python 3.8 or higher
- tkinter (usually included with Python)
- No external dependencies required!

## Installation and Usage

1. Navigate to the work-hours-tracker directory:
```bash
cd work-hours-tracker
```

2. Run the application:
```bash
python app.py
```

The application will create a `workhours.db` SQLite database file in the same directory on first run.

## How to Use

### Managing Tasks

1. **Add Root Task**: Click "Add Root Task" to create a top-level task
2. **Add Child Task**: Select a task and click "Add Child Task" to create a subtask
3. **Delete Task**: Select a task and click "Delete Task" to remove it (and all children)
4. **Refresh**: Click "Refresh" to reload the task tree

### Tracking Time

1. Select a task from the task tree
2. Click the "▶ Play" button to start tracking time
3. The timer will count up and display the current task
4. Click "⏸ Stop" to stop the timer
5. Time is automatically saved to the database

### Viewing Data

- **Summary Tab**: Shows all tasks with their total hours (including subtasks)
- **All Timespans Tab**: Shows every recorded time entry with start/end times and duration

## Code Design

The code follows these principles:

- **Modular**: Each aspect is in a separate file (database, tasks, timer, GUI)
- **Concise**: Clear, readable code without unnecessary complexity
- **Easy to understand**: Well-documented with docstrings and comments
- **Separation of concerns**: Database logic, business logic, and UI are separated

## Database Schema

### Tasks Table
- `id`: Primary key
- `name`: Task name
- `parent_id`: Reference to parent task (NULL for root tasks)
- `created_at`: Timestamp

### Timespans Table
- `id`: Primary key
- `task_id`: Reference to task
- `start_time`: When tracking started
- `end_time`: When tracking stopped (NULL while running)

## Example Usage

Create a task hierarchy like:
```
Work
├── Client 1
│   ├── Feature A
│   └── Feature B
└── Client 2
    └── Playtech
        ├── Bug fixes
        └── New features
```

Then track time on each task and view summaries showing total hours spent on each client, feature, etc.
