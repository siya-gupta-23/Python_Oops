#1. What are the five key concepts of Object-Oriented Programming (OOP)?


'''The five key concepts of Object-Oriented Programming (OOP) are:

Encapsulation: This is the concept of bundling the data (attributes) and the methods (functions) that operate on the data into a single unit, called a class. Encapsulation also restricts direct access to some of an object’s components, which is a way of preventing accidental interference and misuse of the methods and data.

Abstraction: Abstraction involves hiding the complex implementation details of a system and exposing only the essential features to the user. This allows users to interact with objects at a high level without needing to understand the inner workings.

Inheritance: Inheritance allows a new class (subclass or derived class) to inherit properties and behavior (methods) from an existing class (superclass or base class). This promotes code reusability and establishes a natural hierarchy between classes.

Polymorphism: Polymorphism means "many forms," and it allows objects of different classes to be treated as objects of a common superclass. It also enables a single method to be defined in multiple ways, depending on the object that is calling it.

Classes and Objects: These are the fundamental building blocks of OOP. A class is a blueprint or template for creating objects, which are instances of the class. Objects contain both data (attributes) and behaviors (methods) defined by the class.'''

#2. Write a Python class for a `Car` with attributes for `make`, `model`, and `year`. #Include a method to display 

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display(self):
        print(f"Car Information: {self.year} {self.make} {self.model}")

car1 = Car("Mahindra", "XUV 3XO", 2023)
car1.display_info()

#3. Explain the difference between instance methods and class methods. Provide an example of each.

# Instance Method -->  

#Instance methods are functions defined within a class that operate on instances.
#(objects) of that class. They have access to the instance through the self parameter, #which allows them to modify the object’s state (i.e., instance variables).
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
p1 = Person("Siya", 20)
p1.greet()  # Output: Hello, my name is John and I am 30 years old.


# Class Method--->
# Class methods are functions defined within a class that operate on the class itself, 
# rather than on instances of the class. They use the @classmethod decorator and take cls # as their first parameter, which represents the class itself.
   
   class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def greet(cls, name, age):
        """Class method to greet with provided name and age."""
        print(f"Hello, my name is {name} and I am {age} years old.")

# Call the class method directly on the class
#Person.greet("Siya", 20)  # Output: Hello, my name is Siya and I am 20 years old.

#Difference--->
#Instance Methods operate on instances and can access/modify instance variables.
#Class Methods operate on the class itself and can access/modify class variables or #provide alternative ways to instantiate the class.

#4. How does Python implement method overloading? Give an example.

 # method OVerloading --->Two and more methods with same name with different  parameters.#but by default python does not support overloading like other languages. 
 #you can use it using defualt parameter.

 def product(a, b, c=None):
    if c is None:
        p = a * b
    else:
        p = a * b * c
    print(p)

# Calls the function with two arguments
product(4, 5)

# Calls the function with three arguments
product(4, 5, 6)


#5. What are the three types of access modifiers in Python? How are they denoted.

# In Python, access modifiers are used to control the visibility and accessibility of #class members (attributes and methods). Python does not have strict access control like #some other languages, but it uses naming conventions to indicate the intended level of #access. The three main types of access modifiers in Python are:

#1. Public-->

#Denoted by: No special prefix.
#Description: Public members are accessible from anywhere, both inside and outside the #class. By default, all members in Python are public unless otherwise specified.

class MyClass:
    def __init__(self):
        self.public_attr = 5  # Public attribute

    def public_method(self):
        print("This is a public method.")

obj = MyClass()
print(obj.public_attr)  # Accessible
obj.public_method()     # Accessible

#2. Protected
#Denoted by: Single underscore (_) prefix.
#Description: Protected members are intended to be accessed only within the class and its #subclasses. While they can be accessed from outside the class, it's generally #discouraged.


class MyClass:
    def __init__(self):
        self._protected_attr = 10  # Protected attribute

    def _protected_method(self):
        print("This is a protected method.")

class SubClass(MyClass):
    def __init__(self):
        super().__init__()
        print(self._protected_attr)  # Accessible in subclass
        self._protected_method()     # Accessible in subclass

obj = MyClass()
print(obj._protected_attr)  # Accessible but discouraged
obj._protected_method()     # Accessible but discouraged


# 3. Private-->
#Denoted by: Double underscore (__) prefix.
#Description: Protected members are intended to be accessed only within the class and its #subclasses. While they can be accessed from outside the class.

class MyClass:
    def __init__(self):
        self.__private_attr = 20  # Private attribute

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print(self.__private_attr)  # Accessible within the class
        self.__private_method()     # Accessible within the class

obj = MyClass()
obj.public_method()          # Works fine, prints the private attribute and method
print(obj.__private_attr)    # Raises an AttributeError
obj.__private_method()       # Raises an AttributeError


#6 . Describe the five types of inheritance in Python. Provide a simple example of multiple inheritance.
'''
Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

Syntax
In Python, multiple inheritance is implemented by specifying multiple parent classes in the class definition, separated by commas.

class ChildClass(ParentClass1, ParentClass2, ParentClass3):
    # class body
In this example, the ChildClass inherits attributes and methods from all three parent classes: ParentClass1, ParentClass2, and ParentClass3.

It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.'''

Example
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Mammal:
    def __init__(self, name, fur_color):
        self.name = name
        self.fur_color = fur_color
        
class Dog(Animal, Mammal):
    def __init__(self, name, breed, fur_color):
        Animal.__init__(self, name, species="Dog")
        Mammal.__init__(self, name, fur_color)
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
#In this example, the Dog class inherits from both the Animal and Mammal classes,   
# so we can attributes and methods from both parent classes.

 '''7. What is the Method Resolution Order (MRO) in Python? How can you retrieve it       programmatically?'''

''' The Method Resolution Order (MRO) in Python is the order in which methods are inherited from classes in a class hierarchy. It determines the sequence in which base classes are searched when calling a method or accessing an attribute. This is particularly important in multiple inheritance scenarios where a class inherits from multiple base classes.

Retrieving the MRO Programmatically---> 

You can retrieve the MRO of a class using the __mro__ attribute or the mro() method of the class. Here’s how you can do it:

Using __mro__ Attribute--->
The __mro__ attribute is a tuple that contains the classes in the MRO, with the class itself being the first entry.'''

Example-->
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

#Using mro() Method-->
#The mro() method returns a list of classes in the MRO:

#Example-->

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())  # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
#oth methods provide the MRO of a class, showing the sequence in which classes are #considered when looking for a method or attribute.


 #8. Create an abstract base class `Shape` with an abstract method `area()`. Then create # two subclasses `Circle` and `Rectangle` that implement the `area()` method.


from abc import ABC, abstractmethod
import math

# Define the abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Define the Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Define the Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

if __name__ == "__main__":
    circle = Circle(radius=5)
    print(f"Circle area: {circle.area()}")  # Circle area: 78.53981633974483

    rectangle = Rectangle(width=4, height=6)
    print(f"Rectangle area: {rectangle.area()}")  # Rectangle area: 24


 # 9. Demonstrate polymorphism by creating a function that can work with different shape objects to calculate and print their areas.

 import math

# Base class
class Shape:
    def area(self):
        pass  

# Subclass for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Subclass for Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Subclass for Triangle
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Function to calculate and print area
def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")

# Creating objects of different shapes
circle = Circle(5)          # Circle with radius 5
rectangle = Rectangle(4, 6) # Rectangle with width 4 and height 6
triangle = Triangle(3, 7)   # Triangle with base 3 and height 7

# Demonstrating polymorphism
print_area(circle)    # Calls area method of Circle
print_area(rectangle) # Calls area method of Rectangle
print_area(triangle)  # Calls area method of Triangle


# 10. Implement encapsulation in a `BankAccount` class with private attributes for `balance` and `account_number`. Include methods for deposit, withdrawal, and balance inquiry.
  
  class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number  # Private attribute for account number
        self.__balance = initial_balance        # Private attribute for balance

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account if sufficient funds are available."""
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        """Returns the current balance of the account."""
        return self.__balance

    def get_account_number(self):
        """Returns the account number."""
        return self.__account_number

# Example usage:
account = BankAccount("123456789", 500)  # Creating a BankAccount object with an initial balance of $500

# Performing operations on the account
account.deposit(200)        # Deposits $200 into the account
account.withdraw(100)       # Withdraws $100 from the account
print(f"Balance: ${account.get_balance():.2f}") 

# Attempting invalid operations
account.withdraw(700)       # Tries to withdraw $700, which should fail due to insufficient funds
account.deposit(-50)        # Tries to deposit a negative amount, which should fail


# 11. Write a class that overrides the __str__ and __add__ magic methods. What will these methods allow you to do?

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1)         # Output: Vector(2, 3)
print(v2)         # Output: Vector(4, 5)

v3 = v1 + v2      # Using the __add__ method
print(v3)         # Output: Vector(6, 8)



# 12.  Create a decorator that measures and prints the execution time of a function.
'''
import time

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function {func._name_} took {execution_time:.4f} seconds to execute")
        return result
    return wrapper

# Example usage
@measure_execution_time
def calculate_multiply(numbers):
    tot = 1
    for x in numbers:
        tot *= x
    return tot
    
# Call the decorated function
result = calculate_multiply([1, 2, 3, 4, 5])
print("Result:", result)

'''
# 13. Explain the concept of the Diamond Problem in multiple inheritance. How does Python resolve it?
'''
The Diamond Problem in Multiple Inheritance
The Diamond Problem is a challenge that occurs in object-oriented programming languages that support multiple inheritance. It arises when a class inherits from two or more classes that have a common ancestor, leading to ambiguity in method.

Example of the Diamond Problem-->

Consider the following class hierarchy:

Class A: The base class (ancestor).
Class B and Class C: Both inherit from Class A.
Class D: Inherits from both Class B and Class C.
 
 The main problem is When class D inherits from both B and C, and both B and C inherit from A, it creates ambiguity about which method or attribute from A should be used in D.

 Python addresses the Diamond Problem using the Method Resolution Order (MRO). The MRO is determined by the C3 Linearization algorithm, which provides a consistent order in which classes are searched when invoking methods.

 Python resolves it using Method Resolution Order (MRO) and the super() function.

class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")
        super().method()  # Calls the method from the next class in the MRO

class C(A):
    def method(self):
        print("Method in C")
        super().method()  # Calls the method from the next class in the MRO

class D(B, C):
    def method(self):
        print("Method in D")
        super().method()  # Calls the method from the next class in the MRO

# Creating an instance of D
d = D()
d.method()

# Checking the Method Resolution Order
print(D.__mro__)

1. d.method() first calls the method in D, printing "Method in D".
2. D's super().method() calls B's method, printing "Method in B".
3. B's super().method() calls C's method, printing "Method in C".
4. C's super().method() calls A's method, printing "Method in A".
5. The print(D.__mro__) statement shows the order Python follows to resolve methods, which ensures there is no ambiguity.
'''

 #14. Write a class method that keeps track of the number of instances created from a class.
 '''
  class ObjectTracker:
    total_objects = 0  # Class-level variable to keep track of the total number of objects created

    def __init__(self):
        ObjectTracker.total_objects += 1  # Increment the total_objects count when a new instance is created

    @classmethod
    def get_total_objects(cls):
        return cls.total_objects  # Return the current total number of objects

# Creating instances of the class
item1 = ObjectTracker()
item2 = ObjectTracker()
item3 = ObjectTracker()
item4 = ObjectTracker()


print(ObjectTracker.get_total_objects())  '''
# output : 4

#15. Implement a static method in a class that checks if a given year is a leap year.
'''
class YearChecker:
    @staticmethod
    def is_leap_year(year):
        """Returns True if the given year is a leap year, False otherwise."""
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

# Example usage:
print(YearChecker.is_leap_year(2024))  # Output: True
'''
















 



















