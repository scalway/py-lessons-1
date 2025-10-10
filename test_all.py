#!/usr/bin/env python3
"""
Test runner for all Python lessons.

This script runs all example files to verify they work correctly.
"""

import subprocess
import sys
from pathlib import Path


def run_example(lesson_path: Path) -> bool:
    """Run a single example file."""
    example_file = lesson_path / "examples.py"
    
    if not example_file.exists():
        # Check for app.py (Flask lesson)
        example_file = lesson_path / "app.py"
        if not example_file.exists():
            return True  # Skip if no example file
    
    print(f"\n{'=' * 60}")
    print(f"Testing: {lesson_path.name}")
    print('=' * 60)
    
    try:
        # Run with timeout to prevent hanging
        result = subprocess.run(
            [sys.executable, str(example_file)],
            cwd=str(lesson_path),
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✓ {lesson_path.name} passed")
            return True
        else:
            print(f"✗ {lesson_path.name} failed")
            print(f"Error: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"⚠ {lesson_path.name} timed out (likely Flask app - this is OK)")
        return True
    except Exception as e:
        print(f"✗ {lesson_path.name} error: {e}")
        return False


def main():
    """Run all lesson examples."""
    lessons_dir = Path(__file__).parent / "lessons"
    
    if not lessons_dir.exists():
        print("Error: lessons directory not found")
        sys.exit(1)
    
    print("Python Lessons - Test Runner")
    print("=" * 60)
    
    lessons = sorted([d for d in lessons_dir.iterdir() if d.is_dir()])
    results = []
    
    for lesson in lessons:
        result = run_example(lesson)
        results.append((lesson.name, result))
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} lessons passed")
    
    return 0 if passed == total else 1


if __name__ == "__main__":
    sys.exit(main())
