class GardenError(Exception):
    def __str__(self) -> str:
        return "Unknown plant error"


class PlantError(GardenError):
    def __str__(self) -> str:
        return f"The tomato plant is wilting!"


class WaterError(GardenError):
    def __str__(self) -> str:
        return "Not enough water in the tank!"


def main():
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError:{e}")


if __name__ == "__main__":
    main()
