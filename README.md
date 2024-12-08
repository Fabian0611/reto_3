# Reto_3
## Tabla de Contenido
- [Restaurant](#restaurant)
  - [Class Diagram](#class-diagram)
  - [Python Code](#python-code)
  - [Output](#output-with-discount)
- [Line](#linerectangule)
  - [Python Code](#python-code2)
  - [Output](#output)
# Restaurant
1. Restaurant scenario: You want to design a program to calculate the bill for a customer's order in a restaurant.
+ Define a base class MenuItem: This class should have attributes like name, price, and a method to calculate the total price.
+ Create subclasses for different types of menu items: Inherit from MenuItem and define properties specific to each type (e.g., Beverage, Appetizer, MainCourse).
+ Define an Order class: This class should have a list of MenuItem objects and methods to add items, calculate the total bill amount, and potentially apply specific discounts based on the order composition.

Create a class diagram with all classes and their relationships. The menu should have at least 10 items. The code should follow PEP8 rules.

## Class Diagram
La clase base o padre es Order, ya que esta compuesta por "objetos" de la clase MenuItem, a su vez MenuItem hereda los atributos de **name** y **price** a las subclases: Beverage, Appetizer y MainCourse 
```mermaid
classDiagram
        class Order {
        +items: list
        +add_item(menu_item)
        +calculate_total(): float
        +apply_discount(): float
        +print_receipt(): str
        +__init__()
    }

    class MenuItem {
        +str name
        +float price 
        +calculate_price(): float
        +__init__(name, price)
    }

    class Beverage {
        +str size
        +__init__(name, price, size)
        +__str__(): string
    }

    class Appetizer {
        +bool spicy
        +__init__(name, price, spicy)
        +__str__(): string
    }

    class MainCourse {
        +bool vegetarian
        +__init__(name, price, vegetarian)
        +__str__(): string
    }

    MenuItem <|-- Beverage
    MenuItem <|-- Appetizer
    MenuItem <|-- MainCourse
    Order *-- MenuItem : contiene

```
## Python Code

```python
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self):
        return self.price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Beverage(MenuItem):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"{self.name} ({self.size}): ${self.price:.2f}"


class Appetizer(MenuItem):
    def __init__(self, name, price, spicy=False):
        super().__init__(name, price)
        self.spicy = spicy

    def __str__(self):
        spice = "Spicy" if self.spicy else "Non-Spicy"
        return f"{self.name} ({spice}): ${self.price:.2f}"


class MainCourse(MenuItem):
    def __init__(self, name, price, vegetarian=False):
        super().__init__(name, price)
        self.vegetarian = vegetarian

    def __str__(self):
        type_of_dish = "Vegetarian" if self.vegetarian else "Non-Vegetarian"
        return f"{self.name} ({type_of_dish}): ${self.price:.2f}"


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def calculate_total(self):
        return sum(item.calculate_price() for item in self.items)

    # If there's more than 5 items on the order, it will apply a 10% discount
    def apply_discount(self):
        total = self.calculate_total()
        if len(self.items) > 5:
            total *= 0.10
        return total

    def print_receipt(self):
        print("Order Receipt:")
        for item in self.items:
            print(f"- {item}")
        print(f"\nSubtotal: ${self.calculate_total():.2f}")
        Subtotal = self.calculate_total()
        discounted_total = self.apply_discount()
        if discounted_total != Subtotal:
            print(f"Discounted Total: ${discounted_total:.2f}")
            Total = self.calculate_total() - discounted_total
            print(f"Total: $ {Total:.2f}")
        else:
            print(f"Total: $ {Subtotal:.2f}")


# It creates the order with all the food, and then prints the receipt
if __name__ == "__main__":
    order = Order()
    order.add_item(Beverage("Coke", 2.0, "small"))
    order.add_item(Beverage("Tamarindo", 3.0, "medium"))
    order.add_item(Beverage("Jamaica", 2.5, "Large"))
    order.add_item(Appetizer("Tacos de al pastor", 3.0, True))
    order.add_item(Appetizer("Flauta", 6.5, False))
    order.add_item(Appetizer("Tamal", 3.5, False))
    order.add_item(Appetizer("Elote", 4.5, False))
    order.add_item(MainCourse("Veggie Burrito", 8.0, True))
    order.add_item(MainCourse("Enchilada", 12.0, True))
    order.add_item(MainCourse("Tomato Soup", 12.0, True))

    order.print_receipt()
```
## Output (with discount)
Al tener mas de 5 productos, se aplica un descuento del 10%
```bash
Order Receipt:
- Coke (small): $2.00
- Tamarindo (medium): $3.00
- Jamaica (Large): $2.50
- Tacos de al pastor (Spicy): $3.00
- Flauta (Non-Spicy): $6.50
- Tamal (Non-Spicy): $3.50
- Elote (Non-Spicy): $4.50
- Veggie Burrito (Vegetarian): $8.00
- Enchilada (Vegetarian): $12.00
- Tomato Soup (Vegetarian): $12.00

Subtotal: $57.00
Discounted Total: $5.70
Total: $ 51.30
```
## Output (without discount)
Al no tener mas de 5 productos el descuento no se aplica
```bash
Order Receipt:
- Coke (small): $2.00
- Tacos de al pastor (Spicy): $3.00
- Burrito (Non-Vegetarian): $8.00
- Ceviche (Non-Vegetarian): $12.00

Subtotal: $25.00
Total: $ 25.00
```
# Line/Rectangule
- Redefine the class Rectangle, adding a new method of initialization using 4 Lines (composition at its best, a rectangle is compose of 4 lines).

## Python Code2
Se añade la clase **Line** al ejercicio anteriormente hecho de **Rectangule**
```python
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

```
## Output
```bash
Line length: 4.47213595499958
Line slope: 63.43494882292201
Intersects X-axis: True
Intersects Y-axis: False
Rectangle area: 12.0
Rectangle perimeter: 14.0
```
