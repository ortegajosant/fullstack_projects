import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius**2)


def main():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"The area of the circle is: {circle.get_area():.2f}")


if __name__ == "__main__":
    main()
