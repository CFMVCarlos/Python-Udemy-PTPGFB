from abc import ABC, abstractmethod  # ABC is Abstract Base Class


class Appliance(ABC):
    def __init__(self, brand: str, version_no: int) -> None:
        self.brand: str = brand
        self.version_no: int = version_no
        self.is_turned_on: bool = False

    @abstractmethod
    def turn_on(self) -> None: ...

    @abstractmethod
    def turn_off(self) -> None: ...


class Lamp(Appliance):
    def __init__(self, brand: str, version_no: int) -> None:
        super().__init__(brand, version_no)

    def turn_on(self) -> None:
        if self.is_turned_on:
            print(f"{self.brand} Lamp is already turned on")
            return

        self.is_turned_on = True
        print(f"{self.brand} Lamp is turned on")

    def turn_off(self) -> None:
        if not self.is_turned_on:
            print(f"{self.brand} Lamp is already turned off")
            return

        self.is_turned_on = False
        print(f"{self.brand} Lamp is turned off")


class Oven(Appliance):
    def __init__(self, brand: str, version_no: int) -> None:
        super().__init__(brand, version_no)

    def turn_on(self) -> None:
        raise NotImplementedError("Need to add functionality for turn_on()")

    def turn_off(self) -> None:
        raise NotImplementedError("Need to add functionality for turn_off()")


if __name__ == "__main__":
    lamp = Lamp("Philips", 1)
    lamp.turn_on()
    lamp.turn_on()
    lamp.turn_off()
    lamp.turn_off()
    lamp.turn_on()
    lamp.turn_off()

    print()

    oven = Oven("Samsung", 2)
    oven.turn_on()
    oven.turn_off()
