# Quick Start Guide

## Running the Application

### 1. Start the GUI Application

```bash
cd work-hours-tracker
python3 app.py
```

This will open the Work Hours Tracker window.

### 2. Create Your First Task

1. Click "Add Root Task"
2. Enter a task name (e.g., "Work")
3. Click OK

### 3. Add Sub-Tasks

1. Select a task from the task tree
2. Click "Add Child Task"
3. Enter the sub-task name (e.g., "Client 1")
4. Repeat to build your hierarchy

Example hierarchy:
```
Work
  ├── Client 1
  │   ├── Feature A
  │   └── Feature B
  └── Client 2
      └── Playtech
          ├── Bug Fixes
          └── New Features
```

### 4. Track Time

1. Select a task from the tree
2. Click "▶ Play" to start the timer
3. Work on your task (timer counts up)
4. Click "⏸ Stop" when done

The time is automatically saved to the database!

### 5. View Your Work

- **Summary Tab**: Shows total hours for each task (including sub-tasks)
- **All Timespans Tab**: Shows every time entry you've recorded

## Running the Demo

To see a demonstration without the GUI:

```bash
python3 demo.py
```

This will:
- Create sample tasks
- Track some time
- Show you how the system works
- Leave a `demo.db` file you can inspect

## Tips

- **Task Organization**: Use the tree structure to match your workflow
  - Example: Company → Client → Project → Feature
- **Timer**: The timer automatically saves when you stop it
- **Summary**: Parent tasks show total time including all children
- **Database**: Everything is saved to `workhours.db` automatically

## Troubleshooting

### "No module named 'tkinter'"

Install tkinter:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# macOS (usually included)
# Windows (usually included)
```

### Database is locked

- Close all instances of the application
- Only one instance can run at a time

### Want to reset everything?

Delete the database file:
```bash
rm workhours.db
```

The app will create a fresh database on next run.
