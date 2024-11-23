from dataclasses import InitVar, dataclass, field


@dataclass
class Coin:
    name: str
    value: float
    id: str


class Coin2:
    def __init__(self, name: str, value: float, coin_id: str) -> None:
        self.name: str = name
        self.value: float = value
        self.id: str = coin_id

    def __str__(self) -> str:
        return f"{self.name} ({self.id}): {self.value}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Coin2):
            return False

        return (
            self.name == other.name
            and self.value == other.value
            and self.id == other.id
        )


@dataclass
class Fruit:
    name: str
    grams: float
    price_per_kg: float
    edible: bool = True
    related_fruits: list[str] = field(default_factory=list)
    initial_total_price: float = field(init=False)
    is_rare: InitVar[bool | None] = None

    def __post_init__(self, is_rare: bool | None) -> None:
        if is_rare:
            self.price_per_kg *= 2
        self.initial_total_price = self.grams * self.price_per_kg / 1000

    def describe(self) -> None:
        print(f"{self.grams}g of {self.name} costs ${self.total_price:.2f}")

    @property
    def total_price(self) -> float:
        return self.grams * self.price_per_kg / 1000


if __name__ == "__main__":
    bitcoin: Coin = Coin("Bitcoin", 10_000, "BTC")
    bitcoin2: Coin = Coin("Bitcoin", 10_000, "BTC")
    ripple: Coin = Coin("Ripple", 200, "XRP")

    print(bitcoin)
    print(ripple)
    print(bitcoin == bitcoin2)
    print(bitcoin == ripple)

    print()

    apple: Fruit = Fruit("Apple", 100, 5)
    pear: Fruit = Fruit("Pear", 250, 10, related_fruits=["Apple", "Orange"])
    print(apple)
    print(pear)
    print(pear.related_fruits)

    print()

    apple.describe()
    pear.describe()

    print()

    passion_fruit: Fruit = Fruit("Passion Fruit", 100, 50, is_rare=True)
    passion_fruit.describe()
    print(passion_fruit)

    print()

    passion_fruit.price_per_kg = 1000
    passion_fruit.describe()
    print(passion_fruit)
