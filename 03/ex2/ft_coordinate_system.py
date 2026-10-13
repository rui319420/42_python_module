import math


class ParseError(Exception):
    def __init__(self, message: str = "Invalid syntax") -> None:
        self.message = message

    def __str__(self) -> str:
        return self.message


def get_player_pos() -> tuple[float, float, float]:

    while True:
        src = input("Enter new coordinates as floats in format 'x,y,z': ")
        array = src.split(",")
        if len(array) != 3:
            print("Invalid syntax")
            continue
        x = array[0]
        y = array[1]
        z = array[2]
        try:
            x = float(x)
            y = float(y)
            z = float(z)
            res = (x, y, z)
            return res
        except ValueError as e:
            print(f"Error on parameter '': {e}")


def main() -> None:
    print("=== Game Coordinate System ===\n")

    coordinate: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {coordinate}")
    X = coordinate[0]
    Y = coordinate[1]
    Z = coordinate[2]
    print(
        f"It includes: X={coordinate[0]}, Y={coordinate[1]}, Z={coordinate[2]}")
    center = round(math.sqrt(X ** 2 + Y ** 2 + Z ** 2), 4)
    print(f"Distance to center: {center}")

    print("\nGet a second set of coordinates")
    coordinate2: tuple[float, float, float] = get_player_pos()
    X2 = coordinate2[0]
    Y2 = coordinate2[1]
    Z2 = coordinate2[2]
    distance = round(
        math.sqrt((X2 - X) ** 2 + (Y2 - Y) ** 2 + (Z2 - Z) ** 2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
