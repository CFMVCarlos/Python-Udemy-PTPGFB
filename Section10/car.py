class Car:
    LIMITER: int = 200
    __YEAR: int = 2000

    def __init__(
        self, brand: str, max_speed: int, *, fuel_type: str = "gasoline"
    ) -> None:
        self.brand: str = brand
        self.max_speed: int = max_speed
        self.__fuel_type: str = fuel_type
        self.var: str = "red"

    def drive(self) -> None:
        print(f"{self.brand} is driving")

    def __get_description(self) -> str:
        return f"{self.brand}: ({self.__fuel_type})"

    def display_colour(self) -> None:
        print(f"{self.brand} is '{self.var.capitalize()}'")

    @classmethod
    def change_limit(cls, new_limit: int) -> None:
        cls.LIMITER = new_limit

    @classmethod
    def autogenerate_max_speed(cls, brand: str) -> "Car":
        lowered_brand: str = brand.lower()
        max_speed: int = 200

        if lowered_brand == "toyota":
            max_speed = 270
        elif lowered_brand == "bmw":
            max_speed = 290
        elif lowered_brand == "volvo":
            max_speed = 300

        return cls(lowered_brand, max_speed)

    def display_info(self) -> None:
        print(f"{self.brand} (max={self.max_speed}, limiter={self.LIMITER})")


if __name__ == "__main__":
    car1: Car = Car("Toyota", 180)
    car1.display_info()

    car2: Car = Car("BMW", 250)
    car2.display_info()

    Car.change_limit(220)

    car1.display_info()
    car2.display_info()

    print()

    volvo: Car = Car.autogenerate_max_speed("Volvo")
    volvo.display_info()
    ferrari: Car = Car.autogenerate_max_speed("Ferrari")
    ferrari.display_info()

    print()

    car: Car = Car("Toyota", 180, fuel_type="Electric")
    car.drive()
    car.display_colour()
    print(car._Car__get_description())
    print(car._Car__YEAR)
