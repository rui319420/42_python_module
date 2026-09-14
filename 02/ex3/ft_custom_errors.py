

class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print()
    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print()
    print("Testing catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    main()
