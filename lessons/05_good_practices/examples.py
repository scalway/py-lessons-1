"""
Good Practices and Patterns - Writing Better Python Code

This module demonstrates best practices and common design patterns.
"""

from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Protocol, List, Dict, Optional


def pep8_examples():
    """Demonstrate PEP 8 style guidelines."""
    print("=" * 50)
    print("PEP 8 STYLE GUIDELINES")
    print("=" * 50)
    
    # Good naming conventions
    class UserAccount:  # Class names: CapWords
        """User account class."""
        
        MAX_LOGIN_ATTEMPTS = 3  # Constants: UPPERCASE
        
        def __init__(self, username: str):
            """Initialize user account."""
            self.username = username  # Instance variables: lowercase
            self._failed_attempts = 0  # Private: single underscore
        
        def check_password(self, password: str) -> bool:
            """Method names: lowercase with underscores."""
            return password == "secret"
    
    # Good variable names
    user_count = 10  # Descriptive, lowercase with underscores
    is_active = True  # Boolean: is/has prefix
    total_price = 99.99  # Clear and descriptive
    
    print("PEP 8 Guidelines:")
    print("  - Class names: CapWords (e.g., UserAccount)")
    print("  - Function/variable names: lowercase_with_underscores")
    print("  - Constants: UPPERCASE_WITH_UNDERSCORES")
    print("  - Private attributes: _leading_underscore")
    print("  - Use 4 spaces for indentation")
    print("  - Max line length: 79 characters")
    print("  - Two blank lines between top-level definitions")


def documentation_examples():
    """Demonstrate good documentation practices."""
    print("\n" + "=" * 50)
    print("DOCUMENTATION BEST PRACTICES")
    print("=" * 50)
    
    def calculate_rectangle_area(width: float, height: float) -> float:
        """
        Calculate the area of a rectangle.
        
        Args:
            width: The width of the rectangle in units
            height: The height of the rectangle in units
        
        Returns:
            The area of the rectangle
        
        Raises:
            ValueError: If width or height is negative
        
        Examples:
            >>> calculate_rectangle_area(5, 10)
            50.0
        """
        if width < 0 or height < 0:
            raise ValueError("Dimensions must be positive")
        return width * height
    
    print("Good documentation includes:")
    print("  - Clear docstrings for modules, classes, and functions")
    print("  - Type hints for parameters and return values")
    print("  - Examples in docstrings when helpful")
    print("  - Explanation of parameters, returns, and exceptions")
    
    print(f"\nExample: Area of 5x10 rectangle = {calculate_rectangle_area(5, 10)}")


def singleton_pattern():
    """Demonstrate the Singleton pattern."""
    print("\n" + "=" * 50)
    print("SINGLETON PATTERN")
    print("=" * 50)
    
    class DatabaseConnection:
        """Singleton database connection class."""
        
        _instance = None
        
        def __new__(cls):
            """Ensure only one instance exists."""
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance.connection = "Connected to database"
            return cls._instance
        
        def query(self, sql: str) -> str:
            """Execute a query."""
            return f"Executing: {sql}"
    
    # Create two instances
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"db1 is db2: {db1 is db2}")  # True - same instance
    print(f"db1.connection: {db1.connection}")
    print(f"Query result: {db1.query('SELECT * FROM users')}")


def factory_pattern():
    """Demonstrate the Factory pattern."""
    print("\n" + "=" * 50)
    print("FACTORY PATTERN")
    print("=" * 50)
    
    class Vehicle(ABC):
        """Abstract vehicle class."""
        
        @abstractmethod
        def drive(self) -> str:
            """Drive the vehicle."""
            pass
    
    class Car(Vehicle):
        """Car implementation."""
        
        def drive(self) -> str:
            return "Driving a car on the road"
    
    class Boat(Vehicle):
        """Boat implementation."""
        
        def drive(self) -> str:
            return "Sailing a boat on water"
    
    class VehicleFactory:
        """Factory for creating vehicles."""
        
        @staticmethod
        def create_vehicle(vehicle_type: str) -> Vehicle:
            """Create a vehicle based on type."""
            if vehicle_type == "car":
                return Car()
            elif vehicle_type == "boat":
                return Boat()
            else:
                raise ValueError(f"Unknown vehicle type: {vehicle_type}")
    
    car = VehicleFactory.create_vehicle("car")
    boat = VehicleFactory.create_vehicle("boat")
    
    print(f"Car: {car.drive()}")
    print(f"Boat: {boat.drive()}")


def strategy_pattern():
    """Demonstrate the Strategy pattern."""
    print("\n" + "=" * 50)
    print("STRATEGY PATTERN")
    print("=" * 50)
    
    class PaymentStrategy(Protocol):
        """Payment strategy protocol."""
        
        def pay(self, amount: float) -> str:
            """Process payment."""
            ...
    
    class CreditCardPayment:
        """Credit card payment strategy."""
        
        def pay(self, amount: float) -> str:
            return f"Paid ${amount:.2f} with credit card"
    
    class PayPalPayment:
        """PayPal payment strategy."""
        
        def pay(self, amount: float) -> str:
            return f"Paid ${amount:.2f} with PayPal"
    
    class CryptoPayment:
        """Cryptocurrency payment strategy."""
        
        def pay(self, amount: float) -> str:
            return f"Paid ${amount:.2f} with cryptocurrency"
    
    class ShoppingCart:
        """Shopping cart using payment strategies."""
        
        def __init__(self):
            self.items: List[float] = []
            self.payment_strategy: Optional[PaymentStrategy] = None
        
        def add_item(self, price: float):
            """Add item to cart."""
            self.items.append(price)
        
        def set_payment_strategy(self, strategy: PaymentStrategy):
            """Set payment method."""
            self.payment_strategy = strategy
        
        def checkout(self) -> str:
            """Process checkout."""
            if not self.payment_strategy:
                return "No payment method set"
            total = sum(self.items)
            return self.payment_strategy.pay(total)
    
    cart = ShoppingCart()
    cart.add_item(29.99)
    cart.add_item(49.99)
    
    print("Trying different payment methods:")
    cart.set_payment_strategy(CreditCardPayment())
    print(f"  {cart.checkout()}")
    
    cart.set_payment_strategy(PayPalPayment())
    print(f"  {cart.checkout()}")
    
    cart.set_payment_strategy(CryptoPayment())
    print(f"  {cart.checkout()}")


def error_handling_examples():
    """Demonstrate error handling best practices."""
    print("\n" + "=" * 50)
    print("ERROR HANDLING")
    print("=" * 50)
    
    # Custom exception
    class ValidationError(Exception):
        """Custom validation error."""
        pass
    
    def validate_age(age: int):
        """Validate age with custom exception."""
        if age < 0:
            raise ValidationError("Age cannot be negative")
        if age > 150:
            raise ValidationError("Age seems unrealistic")
        return True
    
    # Try-except-else-finally
    def safe_divide(a: float, b: float) -> Optional[float]:
        """Safely divide two numbers."""
        try:
            result = a / b
        except ZeroDivisionError:
            print(f"  Error: Cannot divide by zero")
            return None
        except TypeError:
            print(f"  Error: Invalid types for division")
            return None
        else:
            print(f"  Division successful: {a} / {b} = {result}")
            return result
        finally:
            print(f"  Division operation completed")
    
    print("Safe division examples:")
    safe_divide(10, 2)
    safe_divide(10, 0)
    
    print("\nCustom exception example:")
    try:
        validate_age(25)
        print("  Age 25 is valid")
        validate_age(-5)
    except ValidationError as e:
        print(f"  ValidationError: {e}")


def context_manager_examples():
    """Demonstrate context managers."""
    print("\n" + "=" * 50)
    print("CONTEXT MANAGERS")
    print("=" * 50)
    
    @contextmanager
    def timer(name: str):
        """Context manager for timing code blocks."""
        import time
        start = time.time()
        print(f"  Starting {name}...")
        try:
            yield
        finally:
            end = time.time()
            print(f"  {name} completed in {end - start:.4f} seconds")
    
    print("Using context manager:")
    with timer("Example operation"):
        total = sum(range(1000000))
    
    # File handling with context manager
    print("\nFile handling is better with context managers:")
    print("  with open('file.txt', 'r') as f:")
    print("      content = f.read()")
    print("  # File automatically closed")


def dry_principle():
    """Demonstrate Don't Repeat Yourself principle."""
    print("\n" + "=" * 50)
    print("DRY PRINCIPLE (Don't Repeat Yourself)")
    print("=" * 50)
    
    # Bad: Repetitive code
    print("Bad approach (repetitive):")
    print("  calculate_tax(price1, 0.08)")
    print("  calculate_tax(price2, 0.08)")
    print("  calculate_tax(price3, 0.08)")
    
    # Good: Reusable function
    print("\nGood approach (DRY):")
    
    TAX_RATE = 0.08
    
    def calculate_total_with_tax(prices: List[float]) -> float:
        """Calculate total with tax for multiple items."""
        subtotal = sum(prices)
        tax = subtotal * TAX_RATE
        return subtotal + tax
    
    prices = [10.00, 25.50, 8.99]
    total = calculate_total_with_tax(prices)
    print(f"  Prices: {prices}")
    print(f"  Total with tax: ${total:.2f}")


if __name__ == "__main__":
    pep8_examples()
    documentation_examples()
    singleton_pattern()
    factory_pattern()
    strategy_pattern()
    error_handling_examples()
    context_manager_examples()
    dry_principle()
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)
