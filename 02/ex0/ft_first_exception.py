

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    inputs = ["25", "abc"]
    for i in inputs:
        print()
        print(f"Input data is '{i}")
        try:
            res = input_temperature(i)
            print(f"Temperature is now {res}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
