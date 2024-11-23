class Animal:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def drink(self) -> None:
        print(f"{self.name} is drinking")

    def eat(self) -> None:
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def bark(self) -> None:
        print(f"{self.name}: bark bark!")

    def routine(self) -> None:
        self.eat()
        self.bark()
        self.drink()


class Cat(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def meow(self) -> None:
        print(f"{self.name}: meow meow!")

    def routine(self) -> None:
        self.eat()
        self.meow()
        self.drink()


if __name__ == "__main__":
    dog: Dog = Dog("Doggy")
    cat: Cat = Cat("Kitty")

    dog.bark()
    cat.meow()

    dog.eat()
    cat.eat()
