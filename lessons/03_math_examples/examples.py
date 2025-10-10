"""
Math Examples - Arithmetic and Mathematical Operations

This module demonstrates mathematical operations and the math module.
"""

import math
import random
import statistics


def basic_arithmetic_examples():
    """Demonstrate basic arithmetic operations."""
    print("=" * 50)
    print("BASIC ARITHMETIC")
    print("=" * 50)
    
    a, b = 10, 3
    
    print(f"Numbers: a = {a}, b = {b}")
    print(f"\nAddition: {a} + {b} = {a + b}")
    print(f"Subtraction: {a} - {b} = {a - b}")
    print(f"Multiplication: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Integer Division: {a} // {b} = {a // b}")
    print(f"Modulo: {a} % {b} = {a % b}")
    print(f"Exponentiation: {a} ** {b} = {a ** b}")
    
    # Order of operations
    result = 2 + 3 * 4
    result_with_parens = (2 + 3) * 4
    print(f"\n2 + 3 * 4 = {result}")
    print(f"(2 + 3) * 4 = {result_with_parens}")


def math_module_examples():
    """Demonstrate the math module."""
    print("\n" + "=" * 50)
    print("MATH MODULE")
    print("=" * 50)
    
    # Constants
    print(f"Pi: {math.pi}")
    print(f"E (Euler's number): {math.e}")
    
    # Rounding functions
    x = 4.7
    print(f"\nNumber: {x}")
    print(f"Ceiling: {math.ceil(x)}")
    print(f"Floor: {math.floor(x)}")
    print(f"Round: {round(x)}")
    
    # Power and roots
    print(f"\nSquare root of 16: {math.sqrt(16)}")
    print(f"2^8: {math.pow(2, 8)}")
    print(f"Cube root of 27: {27 ** (1/3)}")
    
    # Trigonometric functions
    angle = math.pi / 4  # 45 degrees
    print(f"\nAngle: {angle} radians (45 degrees)")
    print(f"sin({angle}): {math.sin(angle):.4f}")
    print(f"cos({angle}): {math.cos(angle):.4f}")
    print(f"tan({angle}): {math.tan(angle):.4f}")
    
    # Logarithms
    print(f"\nlog(100, base=10): {math.log10(100)}")
    print(f"ln(e): {math.log(math.e)}")
    
    # Absolute value and sign
    print(f"\nAbsolute value of -5: {abs(-5)}")
    print(f"Factorial of 5: {math.factorial(5)}")


def random_examples():
    """Demonstrate random number generation."""
    print("\n" + "=" * 50)
    print("RANDOM NUMBERS")
    print("=" * 50)
    
    # Set seed for reproducibility (optional)
    random.seed(42)
    
    # Random float between 0 and 1
    print(f"Random float [0, 1): {random.random()}")
    
    # Random integer
    print(f"Random int [1, 10]: {random.randint(1, 10)}")
    
    # Random choice from a list
    colors = ['red', 'green', 'blue', 'yellow']
    print(f"Random color: {random.choice(colors)}")
    
    # Random sample (multiple items without replacement)
    print(f"Random sample of 2 colors: {random.sample(colors, 2)}")
    
    # Shuffle a list
    numbers = list(range(1, 6))
    print(f"\nOriginal: {numbers}")
    random.shuffle(numbers)
    print(f"Shuffled: {numbers}")
    
    # Random float in a range
    print(f"\nRandom float [10, 20]: {random.uniform(10, 20):.2f}")


def number_formatting_examples():
    """Demonstrate number formatting."""
    print("\n" + "=" * 50)
    print("NUMBER FORMATTING")
    print("=" * 50)
    
    pi = math.pi
    large_num = 1234567.89
    
    # Decimal places
    print(f"Pi: {pi}")
    print(f"Pi (2 decimals): {pi:.2f}")
    print(f"Pi (4 decimals): {pi:.4f}")
    
    # Thousands separator
    print(f"\nLarge number: {large_num}")
    print(f"With separator: {large_num:,.2f}")
    
    # Percentage
    percentage = 0.857
    print(f"\nDecimal: {percentage}")
    print(f"Percentage: {percentage:.1%}")
    
    # Scientific notation
    small_num = 0.00000123
    print(f"\nSmall number: {small_num}")
    print(f"Scientific: {small_num:.2e}")
    
    # Padding and alignment
    num = 42
    print(f"\nNumber: {num}")
    print(f"Padded (5 spaces): '{num:5d}'")
    print(f"Zero-padded: '{num:05d}'")


def statistics_examples():
    """Demonstrate statistics calculations."""
    print("\n" + "=" * 50)
    print("STATISTICS")
    print("=" * 50)
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"Data: {data}")
    print(f"\nMean: {statistics.mean(data)}")
    print(f"Median: {statistics.median(data)}")
    print(f"Mode: {statistics.mode([1, 1, 2, 3, 3, 3, 4])}")
    print(f"Standard Deviation: {statistics.stdev(data):.2f}")
    print(f"Variance: {statistics.variance(data):.2f}")
    
    # Min and max (built-in functions)
    print(f"\nMinimum: {min(data)}")
    print(f"Maximum: {max(data)}")
    print(f"Sum: {sum(data)}")


def practical_examples():
    """Demonstrate practical math applications."""
    print("\n" + "=" * 50)
    print("PRACTICAL EXAMPLES")
    print("=" * 50)
    
    # Calculate circle area and circumference
    radius = 5
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    print(f"Circle with radius {radius}:")
    print(f"  Area: {area:.2f}")
    print(f"  Circumference: {circumference:.2f}")
    
    # Distance between two points
    x1, y1 = 0, 0
    x2, y2 = 3, 4
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"\nDistance from ({x1}, {y1}) to ({x2}, {y2}): {distance}")
    
    # Compound interest
    principal = 1000
    rate = 0.05  # 5%
    time = 10  # years
    amount = principal * (1 + rate) ** time
    print(f"\nCompound Interest:")
    print(f"  Principal: ${principal}")
    print(f"  Rate: {rate:.1%}")
    print(f"  Time: {time} years")
    print(f"  Final Amount: ${amount:.2f}")
    print(f"  Interest Earned: ${amount - principal:.2f}")


if __name__ == "__main__":
    basic_arithmetic_examples()
    math_module_examples()
    random_examples()
    number_formatting_examples()
    statistics_examples()
    practical_examples()
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)
