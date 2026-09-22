def garden_operations(operation_number: int):
    print(f"Testing operation {operation_number}...")
    if operation_number == 0:
        int("abc")
    if operation_number == 1:
        43 / 0
    if operation_number == 2:
        open("/non/existent/file")
    if operation_number == 3:
        "abc" + 123


def test_error_types():
    for i in [0, 1, 2, 3, 4]:
        try:
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
    print("Operation completed successfully")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")
