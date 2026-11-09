def input_temperature(temp_str: str) -> int:
    print(f"\nInput data is '{temp_str}'")
    try:
        num = int(temp_str)
        print(f"Temperature is now {num}°C")
        return num

    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
        return 0


def test_temperature() -> None:
    input_temperature("25")
    input_temperature("abc")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    test_temperature()
    print("\nAll tests completed — program didn't crash!")
