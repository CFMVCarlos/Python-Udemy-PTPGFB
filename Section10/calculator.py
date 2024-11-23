class Calculator:
    def __init__(self, version: int = 1) -> None:
        self.version: int = version

    @staticmethod
    def add(*numbers: float) -> float:
        return sum(numbers)

    def get_version(self) -> int:
        return self.version


if __name__ == "__main__":
    calc: Calculator = Calculator()
    print(calc.add(1, 2, 3, 4, 5))
    print(calc.get_version())

    print(Calculator.add(1, 2, 3, 4, 5))
