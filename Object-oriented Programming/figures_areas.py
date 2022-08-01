class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sideLength):
        super().__init__(sideLength, sideLength)


class Cube():
    def __init__(self, square: Square):
        self.square = square
        self.height = square.height

    def count_surface_area(self):
        return self.square.count_surface_area() * 6


class Cuboid():
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height


cuboid = Cuboid(Rectangle(3, 5), 7)

print(cuboid.count_volume())
