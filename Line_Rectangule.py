import math

class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.x = 0
        self.y = 0

class Line:
    def __init__(self, start, end):
        if not all(isinstance(point, Point) for point in (start, end)):
            raise TypeError("Start and end must be instances of Point.")
        self.start = start
        self.end = end

    def compute_length(self):
        return math.sqrt((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)

    def compute_slope(self):
        try:
            return math.degrees(math.atan2(self.end.y - self.start.y, self.end.x - self.start.x))
        except ZeroDivisionError:
            return 90.0

    def compute_horizontal_cross(self):
    # Comprobación: y=0 debe estar entre los valores de inicio y fin
        return self.start.y * self.end.y <= 0 and self.start.y != self.end.y

    def compute_vertical_cross(self):
    # Comprobación: x=0 debe estar entre los valores de inicio y fin
        return self.start.x * self.end.x <= 0 and self.start.x != self.end.x


class Rectangle:
    def __init__(self, method, *args):
        if method == 1:
            bottom_left, self.width, self.height = args
            self.bottom_left = bottom_left
            self.center = Point(
                bottom_left.x + self.width / 2,
                bottom_left.y + self.height / 2
            )
        elif method == 2:
            self.center, self.width, self.height = args
            self.bottom_left = Point(
                self.center.x - self.width / 2,
                self.center.y - self.height / 2
            )
        elif method == 3:
            bottom_left, upper_right = args
            self.width = upper_right.x - bottom_left.x
            self.height = upper_right.y - bottom_left.y
            self.bottom_left = bottom_left
            self.center = Point(
                bottom_left.x + self.width / 2,
                bottom_left.y + self.height / 2
            )
        elif method == 4:
            lines = args[0]
            if len(lines) != 4 or not all(isinstance(line, Line) for line in lines):
                raise ValueError("You must provide exactly 4 lines to define a rectangle.")
            self.lines = lines
            self.bottom_left = lines[0].start
            self.width = lines[0].compute_length()
            self.height = lines[1].compute_length()
            self.center = Point(
                self.bottom_left.x + self.width / 2,
                self.bottom_left.y + self.height / 2
            )
        else:
            raise ValueError("Invalid method. Use 1, 2, 3, or 4.")

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, method, *args):
        if method == 1 or method == 3:
            point, side_length = args
            super().__init__(method, point, side_length, side_length)
        elif method == 2:
            center, side_length = args
            super().__init__(method, center, side_length, side_length)
        else:
            raise ValueError("Invalid method. Use 1, 2, or 3.")

# Se ejecuta el codigo y se imprimen los diferentes valores
if __name__ == "__main__":
    p1 = Point(1, 0)
    p2 = Point(3, 4)
    line = Line(p1, p2)
    print("Line length:", line.compute_length())
    print("Line slope:", line.compute_slope())
    print("Intersects X-axis:", line.compute_horizontal_cross())
    print("Intersects Y-axis:", line.compute_vertical_cross())

    bl = Point(1, 1)
    br = Point(5, 1)
    tl = Point(1, 4)
    tr = Point(5, 4)
    lines = [Line(bl, br), Line(bl, tl), Line(tl, tr), Line(br, tr)]
    rect = Rectangle(4, lines)
    print("Rectangle area:", rect.compute_area())
    print("Rectangle perimeter:", rect.compute_perimeter())
