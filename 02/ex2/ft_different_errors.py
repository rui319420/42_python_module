

def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        raise ZeroDivisionError


def test_error_types():
    print("=== Garden Error Types Demo ===")
    operation_numbers = [0, 1, 2, 3]

    try:
        for n in operation_numbers:
            print(f"Testing operation {n}...")
            garden_operations(n)
    except:
        print(ZeroDivisionError)


if __name__ == "__main__":
    test_error_types()
