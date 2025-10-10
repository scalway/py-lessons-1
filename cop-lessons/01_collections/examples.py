"""
Collection Examples - Lists, Tuples, Sets, and Dictionaries

This module demonstrates the usage of Python's built-in collection types.
"""


def lists_examples():
    """Demonstrate list operations."""
    print("=" * 50)
    print("LISTS EXAMPLES")
    print("=" * 50)
    
    # Creating lists
    fruits = ['apple', 'banana', 'cherry']
    numbers = [1, 2, 3, 4, 5]
    mixed = [1, 'hello', 3.14, True]
    
    print(f"Fruits: {fruits}")
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed}")
    
    # List methods
    fruits.append('orange')
    print(f"\nAfter append: {fruits}")
    
    fruits.insert(1, 'blueberry')
    print(f"After insert at index 1: {fruits}")
    
    fruits.remove('banana')
    print(f"After removing banana: {fruits}")
    
    last_fruit = fruits.pop()
    print(f"Popped: {last_fruit}, Remaining: {fruits}")
    
    # List slicing
    print(f"\nFirst two fruits: {fruits[:2]}")
    print(f"Last two fruits: {fruits[-2:]}")
    
    # List comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"\nSquares using list comprehension: {squares}")
    
    even_numbers = [x for x in range(1, 11) if x % 2 == 0]
    print(f"Even numbers: {even_numbers}")


def tuples_examples():
    """Demonstrate tuple operations."""
    print("\n" + "=" * 50)
    print("TUPLES EXAMPLES")
    print("=" * 50)
    
    # Creating tuples
    coordinates = (10, 20)
    single_item = (42,)  # Note the comma for single-item tuple
    
    print(f"Coordinates: {coordinates}")
    print(f"Single item tuple: {single_item}")
    
    # Tuple unpacking
    x, y = coordinates
    print(f"\nUnpacked - x: {x}, y: {y}")
    
    # Tuples are immutable
    person = ('John', 30, 'Engineer')
    name, age, profession = person
    print(f"\nPerson info - Name: {name}, Age: {age}, Profession: {profession}")
    
    # Named tuple for better readability
    from collections import namedtuple
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(11, 22)
    print(f"\nNamed tuple: {p}, x={p.x}, y={p.y}")


def sets_examples():
    """Demonstrate set operations."""
    print("\n" + "=" * 50)
    print("SETS EXAMPLES")
    print("=" * 50)
    
    # Creating sets
    colors = {'red', 'green', 'blue'}
    numbers = {1, 2, 3, 4, 5}
    
    print(f"Colors: {colors}")
    print(f"Numbers: {numbers}")
    
    # Sets automatically remove duplicates
    duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    unique = set(duplicates)
    print(f"\nOriginal list with duplicates: {duplicates}")
    print(f"Set (duplicates removed): {unique}")
    
    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"\nSet 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference (set1 - set2): {set1 - set2}")
    print(f"Symmetric difference: {set1 ^ set2}")


def dictionaries_examples():
    """Demonstrate dictionary operations."""
    print("\n" + "=" * 50)
    print("DICTIONARIES EXAMPLES")
    print("=" * 50)
    
    # Creating dictionaries
    student = {
        'name': 'Alice',
        'age': 20,
        'grade': 'A',
        'courses': ['Math', 'Physics', 'Chemistry']
    }
    
    print(f"Student: {student}")
    print(f"Name: {student['name']}")
    print(f"Age: {student.get('age')}")
    
    # Adding and modifying
    student['email'] = 'alice@example.com'
    student['age'] = 21
    print(f"\nUpdated student: {student}")
    
    # Dictionary methods
    print(f"\nKeys: {list(student.keys())}")
    print(f"Values: {list(student.values())}")
    print(f"Items: {list(student.items())}")
    
    # Dictionary comprehension
    squares_dict = {x: x**2 for x in range(1, 6)}
    print(f"\nSquares dictionary: {squares_dict}")
    
    # Nested dictionaries
    classroom = {
        'student1': {'name': 'Alice', 'grade': 'A'},
        'student2': {'name': 'Bob', 'grade': 'B'},
        'student3': {'name': 'Charlie', 'grade': 'A'}
    }
    print(f"\nClassroom: {classroom}")
    print(f"Student1's grade: {classroom['student1']['grade']}")


if __name__ == "__main__":
    lists_examples()
    tuples_examples()
    sets_examples()
    dictionaries_examples()
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)
