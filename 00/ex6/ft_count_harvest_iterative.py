

def ft_count_harvest_iterative():
    required_days = int(input("Days until harvest: "))
    for i in range(1, required_days + 1):
        print(f"Day {i}")
    print("Harvest time!")
