class GardenTemperatureError(Exception):
    def __init__(self, temp: int) -> None:
        if temp > 40:
            msg = f"{temp}°C is too hot for plants (max 40°C)"
        if temp < 0:
            msg = f"{temp}°C is too cold for plants (min 0°C)"
        super().__init__(msg)


def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")
    try:
        num = int(temp_str)
        if not (0 <= num <= 40):
            raise GardenTemperatureError(num)
        print(f"Temperature is now {num}°C")
        return num

    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return 0

    except GardenTemperatureError as e:
        print(f"Caught input_temperature error: {e}")
        return 0


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll tests completed — program didn't crash!")
