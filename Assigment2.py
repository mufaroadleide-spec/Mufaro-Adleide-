#Question 1
class Vehicle:
    def __init__(self, brand, model):
        self.brand= brand
        self.model= model
    def selby(self):
        return f'This {self.brand} {self.model} there are cars and bikes.'
class Car(Vehicle):
    def selby(self):
        return f'The car {self.brand} {self.model} is moving ahead.'
class Bike(Vehicle):
    def selby(self):
        return f'The bike {self.brand} {self.model} is being ridden by a professional.'
vehicle= Vehicle('vehicle' , 'class')
car= Car('Mazda', 'MX_5 Roadster')
bike= Bike('Royal' , 'Enfield Classic')

print(vehicle.selby())
print(car.selby())
print(bike.selby())

#Question 2
import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length


def total_area(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

mumu = Circle(6), Rectangle(10, 20), Circle(2), Rectangle(3, 8)

print(f"Total area:", total_area(mumu))

#Question 3

class Shape:
    def __init__(self, name="GenericShape"):
        self.name = name
        print(f"Shape.__init__ called: Initialized shape with name '{self.name}'")

    def calculate_area(self):
        print("Shape.calculate_area called (does nothing)")

class Rectangle(Shape):
    def __init__(self, name, width, length):
        super().__init__(name)
        self.width = width
        self.length = length

    def calculate_area(self):
        super().__init__("RectangleFromArea")

        super().calculate_area()

        area = self.width * self.length
        print(f"Rectangle.calculate_area: width={self.width}, height={self.length}, area={area}")
        return area

rect = Rectangle("MyRectangle", 6, 10)
print(f"Initial name: {rect.name}")

area1 = rect.calculate_area()
print(f"Area: {area1}")
print(f"Name after calculate_area: {rect.name}")


#Question 4

def process_sound(sound_object):
    print("Processing sound...")
    sound_object.make_sound()  # No need to check type

class Dog:
    @staticmethod
    def make_sound():
        print("Woof!")

class Cat:
    @staticmethod
    def make_sound():
        print("Meow!")

dog = Dog()
cat = Cat()
process_sound(dog)
process_sound(cat)

#Quesstion 5
from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self, file_path):
        """Read data from a file"""
        pass

    @abstractmethod
    def write(self, file_path, data):
        """Write data to a file"""
        pass

class TextFileHandler(FileHandler):

    def read(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content

    def write(self, file_path, data):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)

class BinaryFileHandler(FileHandler):

    def read(self, file_path):
        with open(file_path, 'rb') as file:
            content = file.read()
        return content

    def write(self, file_path, data):
        with open(file_path, 'wb') as file:
            file.write(data)

if __name__ == "__main__":
    text_handler = TextFileHandler()
    binary_handler = BinaryFileHandler()

    text_handler.write("example.txt", "Hello, is today a good or day like any other")
    print(text_handler.read("example.txt"))

    binary_handler.write("example.bin", b"\x01\x010\x010")
    print(binary_handler.read("example.bin"))
