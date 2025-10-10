"""
Function Examples - Basic to Advanced Function Usage

This module demonstrates various aspects of Python functions.
"""

import functools
import time


def basic_functions_examples():
    """Demonstrate basic function concepts."""
    print("=" * 50)
    print("BASIC FUNCTIONS")
    print("=" * 50)
    
    def greet(name):
        """Simple function with one parameter."""
        return f"Hello, {name}!"
    
    def add(a, b):
        """Function with multiple parameters."""
        return a + b
    
    def get_user_info():
        """Function returning multiple values."""
        return "Alice", 25, "Engineer"
    
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")
    
    name, age, profession = get_user_info()
    print(f"\nUser info: {name}, {age}, {profession}")


def default_arguments_examples():
    """Demonstrate default and keyword arguments."""
    print("\n" + "=" * 50)
    print("DEFAULT AND KEYWORD ARGUMENTS")
    print("=" * 50)
    
    def power(base, exponent=2):
        """Calculate power with default exponent of 2."""
        return base ** exponent
    
    print(f"2^2 = {power(2)}")
    print(f"2^3 = {power(2, 3)}")
    print(f"3^4 = {power(base=3, exponent=4)}")
    
    def create_profile(name, age, city="Unknown", country="Unknown"):
        """Create a user profile with some default values."""
        return {
            'name': name,
            'age': age,
            'city': city,
            'country': country
        }
    
    profile1 = create_profile("Alice", 25)
    profile2 = create_profile("Bob", 30, city="New York", country="USA")
    
    print(f"\nProfile 1: {profile1}")
    print(f"Profile 2: {profile2}")


def args_kwargs_examples():
    """Demonstrate *args and **kwargs."""
    print("\n" + "=" * 50)
    print("*ARGS AND **KWARGS")
    print("=" * 50)
    
    def sum_all(*args):
        """Sum any number of arguments."""
        return sum(args)
    
    print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
    print(f"Sum of 1, 2, 3, 4, 5: {sum_all(1, 2, 3, 4, 5)}")
    
    def print_info(**kwargs):
        """Print keyword arguments."""
        for key, value in kwargs.items():
            print(f"  {key}: {value}")
    
    print("\nUser information:")
    print_info(name="Alice", age=25, city="Boston")
    
    def full_function(required, *args, default="default", **kwargs):
        """Function using all parameter types."""
        print(f"\n  Required: {required}")
        print(f"  Args: {args}")
        print(f"  Default: {default}")
        print(f"  Kwargs: {kwargs}")
    
    print("\nCalling function with mixed arguments:")
    full_function("must_have", 1, 2, 3, default="custom", extra="value", another="key")


def decorators_examples():
    """Demonstrate function decorators."""
    print("\n" + "=" * 50)
    print("DECORATORS")
    print("=" * 50)
    
    def timer_decorator(func):
        """Decorator to measure function execution time."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"  {func.__name__} took {end_time - start_time:.6f} seconds")
            return result
        return wrapper
    
    def logger_decorator(func):
        """Decorator to log function calls."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"  Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"  {func.__name__} returned {result}")
            return result
        return wrapper
    
    @timer_decorator
    def slow_function():
        """Simulate a slow operation."""
        time.sleep(0.1)
        return "Done"
    
    @logger_decorator
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b
    
    print("Using timer decorator:")
    slow_function()
    
    print("\nUsing logger decorator:")
    multiply(3, 4)


def lambda_examples():
    """Demonstrate lambda functions."""
    print("\n" + "=" * 50)
    print("LAMBDA FUNCTIONS")
    print("=" * 50)
    
    # Basic lambda
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with multiple arguments
    add = lambda a, b: a + b
    print(f"3 + 7 = {add(3, 7)}")
    
    # Lambda with map
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"\nOriginal: {numbers}")
    print(f"Squared: {squared}")
    
    # Lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")
    
    # Lambda with sorted
    students = [
        {'name': 'Alice', 'grade': 85},
        {'name': 'Bob', 'grade': 92},
        {'name': 'Charlie', 'grade': 78}
    ]
    sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)
    print(f"\nStudents sorted by grade:")
    for student in sorted_students:
        print(f"  {student['name']}: {student['grade']}")


def type_hints_examples():
    """Demonstrate type hints."""
    print("\n" + "=" * 50)
    print("TYPE HINTS")
    print("=" * 50)
    
    def greet(name: str) -> str:
        """Greet a person by name."""
        return f"Hello, {name}!"
    
    def add_numbers(a: int, b: int) -> int:
        """Add two integers."""
        return a + b
    
    def process_items(items: list[str]) -> dict[str, int]:
        """Count the length of each item."""
        return {item: len(item) for item in items}
    
    print(greet("World"))
    print(f"5 + 3 = {add_numbers(5, 3)}")
    
    result = process_items(['apple', 'banana', 'cherry'])
    print(f"\nItem lengths: {result}")


if __name__ == "__main__":
    basic_functions_examples()
    default_arguments_examples()
    args_kwargs_examples()
    decorators_examples()
    lambda_examples()
    type_hints_examples()
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)
