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
    print(coordinate)


if __name__ == "__main__":
    main()
