

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        if self.name == "Rose":
            increment = 0.8
        elif self.name == "Cactus":
            increment = 0.3
        elif self.name == "Sunflower":
            increment = 1.5
        else:
            increment = 0.5
        self.height = round(self.height + increment, 1)

    def age(self) -> None:
        self._age += 1


def main() -> None:
    rose = Plant("Rose", 25, 30)
    oak = Plant("Oak", 200, 365)
    cactus = Plant("Cactus", 5, 90)
    sunflower = Plant("Sunflower", 80, 45)
    fern = Plant("Fern", 15, 120)
    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()


if __name__ == "__main__":
    main()
