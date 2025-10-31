#!/usr/bin/env python3
"""
Demo script showing the timespan editing feature.

This demonstrates the new functionality without requiring a GUI display.
To use this feature in the actual application:
1. Run: python app.py
2. Go to the "All Timespans" tab
3. Double-click on any timespan row
4. A dialog will appear showing all available tasks
5. Select the new task and click "Select"
6. The timespan will be updated to the new task
"""

import sys
import os

# Add the current directory to the path to import local modules
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from database import Database
from task_manager import TaskManager
from datetime import datetime, timedelta

# Create demo database
demo_db_path = "/tmp/demo_edit_feature.db"
if os.path.exists(demo_db_path):
    os.remove(demo_db_path)

db = Database(demo_db_path)
task_manager = TaskManager(db)

print("=" * 60)
print("Work Hours Tracker - Timespan Edit Feature Demo")
print("=" * 60)

# Create sample task hierarchy
print("\n1. Creating sample tasks...")
work_id = task_manager.add_task("Work")
client1_id = task_manager.add_task("Client 1", parent_id=work_id)
feature_a_id = task_manager.add_task("Feature A", parent_id=client1_id)
feature_b_id = task_manager.add_task("Feature B", parent_id=client1_id)
client2_id = task_manager.add_task("Client 2", parent_id=work_id)

print("\nTask hierarchy created:")
task_tree = task_manager.get_task_tree()
for task_id, indented_name, level in task_tree:
    print(f"  {indented_name}")

# Create some timespans
print("\n2. Creating sample timespans...")
ts1_id = db.start_timespan(feature_a_id)
db.stop_timespan(ts1_id)
ts2_id = db.start_timespan(feature_b_id)
db.stop_timespan(ts2_id)
ts3_id = db.start_timespan(client2_id)
db.stop_timespan(ts3_id)

print("\nInitial timespans:")
timespans = db.get_all_timespans()
for ts in timespans:
    start_time = datetime.fromisoformat(ts['start_time']).strftime('%H:%M:%S')
    print(f"  Timespan {ts['id']}: {ts['task_name']} (started at {start_time})")

# Demonstrate the edit feature
print("\n3. Demonstrating the edit feature...")
print(f"\nScenario: You accidentally tracked time for 'Feature A' but it should have been 'Feature B'")
print(f"\nAction: Double-click on timespan {ts1_id} in the GUI...")
print("        A dialog appears with all tasks")
print("        Select 'Feature B' and click 'Select'")

# Simulate the edit
db.update_timespan_task(ts1_id, feature_b_id)

print("\n✓ Timespan updated successfully!")

print("\nUpdated timespans:")
timespans = db.get_all_timespans()
for ts in timespans:
    start_time = datetime.fromisoformat(ts['start_time']).strftime('%H:%M:%S')
    marker = " ← Updated!" if ts['id'] == ts1_id else ""
    print(f"  Timespan {ts['id']}: {ts['task_name']} (started at {start_time}){marker}")

# Show summary to demonstrate impact
print("\n4. Impact on task summaries...")
print("\nTotal hours per task (including children):")
for task_id, indented_name, level in task_tree:
    hours = db.get_task_total_hours(task_id, include_children=True)
    if hours > 0:
        print(f"  {indented_name}: {hours:.4f}h")

print("\n" + "=" * 60)
print("Demo completed!")
print("=" * 60)
print("\nKey features of the timespan editing functionality:")
print("  ✓ Double-click on any timespan in the 'All Timespans' tab")
print("  ✓ Select a different task from the hierarchical task list")
print("  ✓ Timespan is immediately updated in the database")
print("  ✓ Summary view automatically reflects the change")
print("  ✓ Simple and intuitive user interface")

db.close()
