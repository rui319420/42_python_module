

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        omg = 1 / 0


def test_error_types():
    print("=== Garden Error Types Demo ===")
    operation_numbers = [0, 1, 2, 3]

    for n in operation_numbers:
        try:
            print(f"Testing operation {n}...")
            garden_operations(n)
        except ValueError as e:
            print(f"{e}")
        except ZeroDivisionError as e:
            print(f"{e}")


if __name__ == "__main__":
    test_error_types()
