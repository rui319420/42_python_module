import math


def get_player_pos():
    print("Get a first set of coordinates")
    input("Enter new coordinate as floats in format 'x,y,z': ")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    get_player_pos()


if __name__ == "__main__":
    main()
