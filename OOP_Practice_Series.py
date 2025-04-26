#______________________________________________________________________
# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student1 = Student("Alice", 92)
student1.display()

#______________________________________________________________________
# 2. Using cls
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

obj1 = Counter()
obj2 = Counter()
Counter.display_count()

#______________________________________________________________________
# 3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} car is starting.")

car1 = Car("Toyota")
print(car1.brand)
car1.start()

#______________________________________________________________________
# 4. Class Variables and Class Methods
class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 = Bank()
bank2 = Bank()

print(bank1.bank_name)
Bank.change_bank_name("XYZ Bank")
print(bank2.bank_name)

#______________________________________________________________________
# 5. Static Variables and Static Methods
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))

#______________________________________________________________________
# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger Created")

    def __del__(self):
        print("Logger Destroyed")

logger = Logger()
del logger

#______________________________________________________________________
# 7. Access Modifiers: Public, Protected, Private
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

emp = Employee("John", 50000, "123-45-6789")

print(emp.name)
print(emp._salary)
# print(emp.__ssn)  # This will cause an error
print(emp._Employee__ssn)  # Accessing private 

#______________________________________________________________________
# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher = Teacher("Alice", "Math")
print(teacher.name, teacher.subject)

#______________________________________________________________________
# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(rect.area())

#______________________________________________________________________
# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

dog = Dog("Buddy", "Golden Retriever")
dog.bark()

#______________________________________________________________________
# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

#______________________________________________________________________
# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(0))

#______________________________________________________________________
# 13. Composition
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start()

#______________________________________________________________________
# 14. Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("John")
dept = Department(emp)
print(dept.employee.name)

#______________________________________________________________________
# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        print("A's show")

class B(A):
    def show(self):
        print("B's show")

class C(A):
    def show(self):
        print("C's show")

class D(B, C):
    pass

d = D()
d.show()
print(D.mro())

#______________________________________________________________________
# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

#______________________________________________________________________
# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())

#______________________________________________________________________
# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

prod = Product(100)
print(prod.price)
prod.price = 200
print(prod.price)
del prod.price

#______________________________________________________________________
# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

mult = Multiplier(3)
print(callable(mult))
print(mult(10))

#______________________________________________________________________
# 20. Creating a Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

try:
    check_age(16)
except InvalidAgeError as e:
    print(e)

#______________________________________________________________________
# 21. Make a Custom Class Iterable
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

countdown = Countdown(5)
for number in countdown:
    print(number)

#__________________________________ Assignment by Zahira Khan _________________________________
#______________________________________________________________________________________________