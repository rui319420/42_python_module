

def ft_plant_age():
    elapsed_days = int(input("Enter plant age in days: "))
    if (elapsed_days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
