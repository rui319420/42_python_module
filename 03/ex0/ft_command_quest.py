import sys


def main():
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    i = 1
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        for _ in sys.argv[1:]:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {i}")


if __name__ == "__main__":
    main()
