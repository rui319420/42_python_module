import math


class


def get_player_pos() -> tuple[float, float, float]:
    src = input("Enter new coordinates as floats in format 'x,y,z': ")
    try:
        x, y, z = src.split(",")
    except:

    try:
        x = int(x)
        y = int(y)
        z = int(z)
        x, y, z =
    except TypeError as e:
        TypeError()
    except


def main() -> None:
    print("=== Game Coordinate System ===\n")

    coordinate = get_player_pos()


if __name__ == "__main__":
    main()
