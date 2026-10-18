class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(5, 10)

area = rectangle.calculate_area()
perimeter = rectangle.calculate_perimeter()

print(f"Площа прямокутника: {area}")
print(f"Периметр прямокутника: {perimeter}")
