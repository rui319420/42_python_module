

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height >= 0:
            self._height: float = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0

        if age >= 0:
            self._age: int = age
        else:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        if self._name == "Rose":
            increment = 0.8
        elif self._name == "Cactus":
            increment = 0.3
        elif self._name == "Sunflower":
            increment = 1.5
        else:
            increment = 0.5
        self._height = round(self._height + increment, 1)

    def age(self) -> None:
        self._age += 1

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


def main() -> None:
    print("=== Garden Security System ===")
    plant = Plant("Rose", 15.0, 10)
    print(
        f"Plant created: {plant._name}: "
        f"{plant.get_height():.1f}cm, {plant.get_age()} days old"
    )
    plant.set_height(25)
    plant.set_age(30)
    plant.set_height(-5)
    plant.set_age(-10)
    print(
        f"Current state: {plant._name}: "
        f"{plant.get_height():.1f}cm, {plant.get_age()} days old"
    )


if __name__ == "__main__":
    main()
