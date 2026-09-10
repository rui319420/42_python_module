

def display_days(n):
    if n <= 0:
        return
    else:
        display_days(n - 1)
        print(f"Day {n}")


def ft_count_harvest_recursive():
    required_days = int(input("Days until harvest: "))
    display_days(required_days)
    print("Harvest time!")
