class PlantError(Exception):
    def __init__(self, invalid_name: str) -> None:
        self.invalid_name = invalid_name

    def __str__(self) -> str:
        return f"Invalid plant name to water: '{self.invalid_name}'"


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print()
    print("Testing valid plants...")
    print("Opening watering system")
    plants = ["Tomato", "Lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")

    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    plants = ["Tomato", "lettuce", "Carrots"]
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


def main():
    test_watering_system()
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
