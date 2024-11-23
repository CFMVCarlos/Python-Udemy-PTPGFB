class Fruit:
    def __init__(self, name: str, grams: float) -> None:
        self.name: str = name
        self.grams: float = grams

    def eat(self) -> None:
        print(f"Eating {self.grams}g of {self.name}...")


if __name__ == "__main__":
    apple: Fruit = Fruit("Apple", 25)
    print(apple.name)
    apple.eat()

    print()

    banana: Fruit = Fruit("Banana", 10)
    print(banana.name)
    banana.eat()
