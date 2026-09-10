

def ft_water_reminder():
    elapsed_time = int(input("Days since last watering: "))
    if (elapsed_time > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
