class GardenError(Exception):
    def __init__(self, msg="Unknown garden error"):
        super().__init__(msg)
    pass


class PlantError(GardenError):
    def __init__(self, msg="Unknown plant error"):
        super().__init__(msg)
    pass


def water_plant(plant_name):
    if plant_name != str.capitalize(plant_name):
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants: list[str]):
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("\nTesting valid plants...")
    plants = ["Tomato", "Lettuce", "Carrots"]
    test_watering_system(plants)

    print("\nTesting invalid plants...")
    plants = ["Tomato", "lettuce", "carrots"]
    test_watering_system(plants)
    print("\nCleanup always happens, even with errors!")
