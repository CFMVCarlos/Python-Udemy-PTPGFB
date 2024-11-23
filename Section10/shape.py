from typing import override


class Shape:
    def __init__(self, name: str, sides: int) -> None:
        self.name: str = name
        self.sides: int = sides

    def describe(self) -> None:
        print(f"{self.name} ({self.sides} sides)")

    def shape_method(self) -> None:
        print(f"{self.name}: shape_method()")


class Square(Shape):
    def __init__(self, size: float) -> None:
        super().__init__("Square", 4)
        self.size: float = size

    @override
    def describe(self) -> None:
        print(f"I am a {self.name} with a size of {self.size}")


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        super().__init__("Rectangle", 4)
        self.width: float = width
        self.height: float = height

    @override
    def describe(self) -> None:
        print(f"{self.name} ({self.width}x{self.height})")


if __name__ == "__main__":
    square: Square = Square(20)
    square.describe()
    square.shape_method()

    print()

    rectangle: Rectangle = Rectangle(10, 20)
    rectangle.describe()
    rectangle.shape_method()
