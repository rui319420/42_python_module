

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        omg = 1 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        impossible = "str" + 1


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
        except FileNotFoundError as e:
            print(f"{e}")
        except TypeError as e:
            print(f"{e}")
        print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
