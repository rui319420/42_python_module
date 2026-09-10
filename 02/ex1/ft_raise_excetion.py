

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    elif temp < 0:
        raise ValueError(
            f"{temp}°C is too cold for plants (min 0°C)")
    else:
        raise ValueError(
            f"{temp}°C is too hot for plants (max 40°C)")


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    inputs = ["25", "abc", "100", "-50"]
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
