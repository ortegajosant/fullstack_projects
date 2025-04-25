from abc import ABC, abstractmethod
import math


# Abstract class Shape
class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate_area(self):
        return math.pi * self.radius**2


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

    def calculate_area(self):
        return self.side_length**2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


def main():
    # Create instances of each shape
    circle = Circle(radius=5)
    square = Square(side_length=4)
    rectangle = Rectangle(width=3, height=6)

    # Test Circle
    print("Circle:")
    print(f"Perimeter: {circle.calculate_perimeter()}")
    print(f"Area: {circle.calculate_area()}")

    # Test Square
    print("\nSquare:")
    print(f"Perimeter: {square.calculate_perimeter()}")
    print(f"Area: {square.calculate_area()}")

    # Test Rectangle
    print("\nRectangle:")
    print(f"Perimeter: {rectangle.calculate_perimeter()}")
    print(f"Area: {rectangle.calculate_area()}")


if __name__ == "__main__":
    main()
