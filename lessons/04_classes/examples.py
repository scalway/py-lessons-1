"""
Class Examples - Object-Oriented Programming

This module demonstrates OOP concepts in Python.
"""


def basic_class_examples():
    """Demonstrate basic class concepts."""
    print("=" * 50)
    print("BASIC CLASSES")
    print("=" * 50)
    
    class Dog:
        """A simple Dog class."""
        
        # Class attribute (shared by all instances)
        species = "Canis familiaris"
        
        def __init__(self, name, age):
            """Initialize a Dog instance."""
            self.name = name
            self.age = age
        
        def bark(self):
            """Make the dog bark."""
            return f"{self.name} says Woof!"
        
        def get_info(self):
            """Return dog information."""
            return f"{self.name} is {self.age} years old"
    
    # Create instances
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Lucy", 5)
    
    print(f"Dog 1: {dog1.get_info()}")
    print(f"Dog 2: {dog2.get_info()}")
    print(f"\n{dog1.bark()}")
    print(f"{dog2.bark()}")
    print(f"\nSpecies: {Dog.species}")


def inheritance_examples():
    """Demonstrate inheritance."""
    print("\n" + "=" * 50)
    print("INHERITANCE")
    print("=" * 50)
    
    class Animal:
        """Base Animal class."""
        
        def __init__(self, name, species):
            """Initialize an Animal."""
            self.name = name
            self.species = species
        
        def make_sound(self):
            """Generic sound method."""
            return "Some sound"
        
        def get_info(self):
            """Return animal information."""
            return f"{self.name} is a {self.species}"
    
    class Dog(Animal):
        """Dog class inheriting from Animal."""
        
        def __init__(self, name, breed):
            """Initialize a Dog."""
            super().__init__(name, "Dog")
            self.breed = breed
        
        def make_sound(self):
            """Override make_sound for dogs."""
            return "Woof!"
        
        def get_info(self):
            """Override get_info to include breed."""
            return f"{self.name} is a {self.breed} {self.species}"
    
    class Cat(Animal):
        """Cat class inheriting from Animal."""
        
        def __init__(self, name, color):
            """Initialize a Cat."""
            super().__init__(name, "Cat")
            self.color = color
        
        def make_sound(self):
            """Override make_sound for cats."""
            return "Meow!"
    
    # Create instances
    dog = Dog("Max", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    
    print(f"Dog: {dog.get_info()}")
    print(f"Dog sound: {dog.make_sound()}")
    
    print(f"\nCat: {cat.get_info()}")
    print(f"Cat sound: {cat.make_sound()}")


def magic_methods_examples():
    """Demonstrate magic methods."""
    print("\n" + "=" * 50)
    print("MAGIC METHODS")
    print("=" * 50)
    
    class Book:
        """A Book class with magic methods."""
        
        def __init__(self, title, author, pages):
            """Initialize a Book."""
            self.title = title
            self.author = author
            self.pages = pages
        
        def __str__(self):
            """String representation for users."""
            return f"'{self.title}' by {self.author}"
        
        def __repr__(self):
            """String representation for developers."""
            return f"Book('{self.title}', '{self.author}', {self.pages})"
        
        def __len__(self):
            """Return the number of pages."""
            return self.pages
        
        def __eq__(self, other):
            """Check if two books are equal."""
            return (self.title == other.title and 
                   self.author == other.author)
    
    book1 = Book("Python Basics", "John Doe", 300)
    book2 = Book("Python Basics", "John Doe", 300)
    book3 = Book("Advanced Python", "Jane Smith", 450)
    
    print(f"str(book1): {str(book1)}")
    print(f"repr(book1): {repr(book1)}")
    print(f"len(book1): {len(book1)} pages")
    
    print(f"\nbook1 == book2: {book1 == book2}")
    print(f"book1 == book3: {book1 == book3}")


def operator_overloading_examples():
    """Demonstrate operator overloading."""
    print("\n" + "=" * 50)
    print("OPERATOR OVERLOADING")
    print("=" * 50)
    
    class Vector:
        """A 2D vector class with operator overloading."""
        
        def __init__(self, x, y):
            """Initialize a Vector."""
            self.x = x
            self.y = y
        
        def __str__(self):
            """String representation."""
            return f"Vector({self.x}, {self.y})"
        
        def __add__(self, other):
            """Add two vectors."""
            return Vector(self.x + other.x, self.y + other.y)
        
        def __sub__(self, other):
            """Subtract two vectors."""
            return Vector(self.x - other.x, self.y - other.y)
        
        def __mul__(self, scalar):
            """Multiply vector by a scalar."""
            return Vector(self.x * scalar, self.y * scalar)
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1: {v1}")
    print(f"v2: {v2}")
    print(f"v1 + v2: {v1 + v2}")
    print(f"v1 - v2: {v1 - v2}")
    print(f"v1 * 3: {v1 * 3}")


def class_static_methods_examples():
    """Demonstrate class and static methods."""
    print("\n" + "=" * 50)
    print("CLASS AND STATIC METHODS")
    print("=" * 50)
    
    class Pizza:
        """A Pizza class with class and static methods."""
        
        def __init__(self, ingredients):
            """Initialize a Pizza."""
            self.ingredients = ingredients
        
        def __str__(self):
            """String representation."""
            return f"Pizza with {', '.join(self.ingredients)}"
        
        @classmethod
        def margherita(cls):
            """Create a Margherita pizza."""
            return cls(['mozzarella', 'tomatoes', 'basil'])
        
        @classmethod
        def pepperoni(cls):
            """Create a Pepperoni pizza."""
            return cls(['mozzarella', 'tomatoes', 'pepperoni'])
        
        @staticmethod
        def is_valid_ingredient(ingredient):
            """Check if an ingredient is valid."""
            invalid = ['pineapple']  # Controversial!
            return ingredient.lower() not in invalid
    
    pizza1 = Pizza.margherita()
    pizza2 = Pizza.pepperoni()
    
    print(f"Pizza 1: {pizza1}")
    print(f"Pizza 2: {pizza2}")
    
    print(f"\nIs 'mushroom' valid? {Pizza.is_valid_ingredient('mushroom')}")
    print(f"Is 'pineapple' valid? {Pizza.is_valid_ingredient('pineapple')}")


def properties_examples():
    """Demonstrate properties and setters."""
    print("\n" + "=" * 50)
    print("PROPERTIES")
    print("=" * 50)
    
    class Temperature:
        """Temperature class with property validation."""
        
        def __init__(self, celsius):
            """Initialize temperature."""
            self._celsius = celsius
        
        @property
        def celsius(self):
            """Get temperature in Celsius."""
            return self._celsius
        
        @celsius.setter
        def celsius(self, value):
            """Set temperature in Celsius with validation."""
            if value < -273.15:
                raise ValueError("Temperature below absolute zero!")
            self._celsius = value
        
        @property
        def fahrenheit(self):
            """Get temperature in Fahrenheit."""
            return self._celsius * 9/5 + 32
        
        @fahrenheit.setter
        def fahrenheit(self, value):
            """Set temperature in Fahrenheit."""
            self.celsius = (value - 32) * 5/9
    
    temp = Temperature(25)
    print(f"Temperature: {temp.celsius}°C = {temp.fahrenheit:.1f}°F")
    
    temp.celsius = 0
    print(f"Updated: {temp.celsius}°C = {temp.fahrenheit:.1f}°F")
    
    temp.fahrenheit = 100
    print(f"Set via Fahrenheit: {temp.celsius:.1f}°C = {temp.fahrenheit}°F")


def composition_example():
    """Demonstrate composition."""
    print("\n" + "=" * 50)
    print("COMPOSITION")
    print("=" * 50)
    
    class Engine:
        """Engine class."""
        
        def __init__(self, horsepower):
            """Initialize engine."""
            self.horsepower = horsepower
        
        def start(self):
            """Start the engine."""
            return "Engine started"
    
    class Car:
        """Car class using composition."""
        
        def __init__(self, make, model, horsepower):
            """Initialize car with an engine."""
            self.make = make
            self.model = model
            self.engine = Engine(horsepower)
        
        def start(self):
            """Start the car."""
            return f"{self.make} {self.model}: {self.engine.start()}"
        
        def get_info(self):
            """Get car information."""
            return f"{self.make} {self.model} ({self.engine.horsepower} HP)"
    
    car = Car("Tesla", "Model 3", 283)
    print(f"Car: {car.get_info()}")
    print(car.start())


if __name__ == "__main__":
    basic_class_examples()
    inheritance_examples()
    magic_methods_examples()
    operator_overloading_examples()
    class_static_methods_examples()
    properties_examples()
    composition_example()
    print("\n" + "=" * 50)
    print("All examples completed!")
    print("=" * 50)
