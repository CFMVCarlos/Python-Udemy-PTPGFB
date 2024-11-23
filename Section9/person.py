class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


if __name__ == "__main__":
    mario: Person = Person("Mario", 27)
    print(mario)
    print(repr(mario))
