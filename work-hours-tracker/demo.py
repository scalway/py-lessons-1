"""
Demo script showing programmatic usage of the work hours tracker.
This demonstrates how the modules work together.
"""

import time
from database import Database
from task_manager import TaskManager
from timer import Timer


def demo():
    """Run a demonstration of the work hours tracker."""
    print("=" * 60)
    print("Work Hours Tracker - Demo")
    print("=" * 60)
    
    # Initialize components
    db = Database('demo.db')
    task_manager = TaskManager(db)
    timer = Timer(db)
    
    print("\n1. Creating task hierarchy...")
    work_id = task_manager.add_task('Work')
    client1_id = task_manager.add_task('Client 1', work_id)
    feature_a_id = task_manager.add_task('Feature A', client1_id)
    feature_b_id = task_manager.add_task('Feature B', client1_id)
    client2_id = task_manager.add_task('Client 2', work_id)
    playtech_id = task_manager.add_task('Playtech', client2_id)
    bugfix_id = task_manager.add_task('Bug Fixes', playtech_id)
    
    print("\n2. Task tree structure:")
    tree = task_manager.get_task_tree()
    for task_id, name, level in tree:
        print(f"   {name}")
    
    print("\n3. Tracking time on 'Feature A'...")
    feature_a_path = task_manager.get_task_path(feature_a_id)
    print(f"   Task path: {feature_a_path}")
    
    timer.start(feature_a_id)
    print(f"   Timer started at: {timer.start_time}")
    
    # Simulate work for 3 seconds
    for i in range(3):
        time.sleep(1)
        print(f"   Elapsed: {timer.format_elapsed_time()}")
    
    timer.stop()
    print("   Timer stopped!")
    
    print("\n4. Tracking time on 'Bug Fixes'...")
    bugfix_path = task_manager.get_task_path(bugfix_id)
    print(f"   Task path: {bugfix_path}")
    
    timer.start(bugfix_id)
    time.sleep(2)
    print(f"   Elapsed: {timer.format_elapsed_time()}")
    timer.stop()
    print("   Timer stopped!")
    
    print("\n5. Summary of hours by task:")
    for task_id, name, level in tree:
        hours = db.get_task_total_hours(task_id, include_children=True)
        if hours > 0:
            print(f"   {name}: {hours:.4f} hours")
    
    print("\n6. All recorded timespans:")
    timespans = db.get_all_timespans()
    for ts in timespans:
        print(f"   Task: {ts['task_name']}")
        print(f"   Start: {ts['start_time']}")
        print(f"   End: {ts['end_time']}")
        print()
    
    # Cleanup
    db.close()
    
    print("=" * 60)
    print("Demo completed!")
    print("Database saved as: demo.db")
    print("Run 'python app.py' to use the GUI application.")
    print("=" * 60)


if __name__ == '__main__':
    demo()
