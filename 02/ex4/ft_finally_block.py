class PlantError(Exception):
    def __str__(self, invalid_name: str) -> str:
        return f"Invalid plant name to water: '{invalid_name}'"


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
        water_plant(plants)
    except PlantError as e:
        print("Caught PlantError: {e}")
    finally:
        print("Closing watering system")
    print()
    print("Testing invalid plants...")
    plants = ["Tomato", "lettuce"]


def main():
    test_watering_system()


if __name__ == "__main__":
    main()
