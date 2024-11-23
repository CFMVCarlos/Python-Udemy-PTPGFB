class Car:
    SPEED_LIMIT_KM: float = 140

    def __init__(
        self, brand: str, card_id: int = 0, colour: str = "red", wheels: int = 4
    ) -> None:
        self.brand: str = brand
        self.card_id: int = card_id
        self.colour: str = colour
        self.wheels: int = wheels

    def __eq__(self, other: "Car") -> bool:
        # return self.card_id == other.card_id
        return self.__dict__ == other.__dict__

    def turn_on(self) -> None:
        print(f"Turning on: {self.brand}")

    def turn_off(self) -> None:
        print(f"Turning off: {self.brand}")

    def drive_km(self, km: float) -> None:
        print(f"Driving: {self.brand} for {km} km")

    def drive_speed(self, *, speed: float) -> None:
        if speed > Car.SPEED_LIMIT_KM:
            print(f"Limiter activated: Driving at {Car.SPEED_LIMIT_KM} km/h")
        else:
            print(f"Driving at {speed} km/h")

    def describe(self) -> None:
        print(f"{self.brand} is a car with {self.wheels} wheels")


if __name__ == "__main__":
    bmw = Car("BMW")
    bmw.turn_on()
    bmw.drive_km(10)
    bmw.turn_off()
    bmw.describe()

    print()

    volvo = Car("Volvo")
    volvo.turn_on()
    volvo.drive_km(20)
    volvo.turn_off()
    volvo.describe()

    print()

    toyota = Car("Toyota")
    toyota.drive_speed(speed=200)

    print()

    car1: Car = Car("Ferrari", 1, "black")
    car2: Car = Car("Ferrari", 1, "black")
    print(car1 == car2)
