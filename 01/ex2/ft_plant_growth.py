# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rishiyam <rishiyam@student.42tokyo.jp>     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/09/07 15:31:20 by rishiyam          #+#    #+#              #
#    Updated: 2026/09/07 16:33:44 by rishiyam         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self._age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        if self.name == "Rose":
            increment = 0.8
        elif self.name == "Cactus":
            increment = 0.3
        elif self.name == "Sunflower":
            increment = 1.5
        else:
            increment = 0.5
        self.height = round(self.height + increment, 1)

    def age(self) -> None:
        self._age += 1


def main() -> None:
    target = Plant("Cactus", 15, 20)
    print("=== Garden Plant Growth ===")
    target.show()
    before_height = target.height
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        target.grow()
        target.age()
        target.show()
    total_growth = round(target.height - before_height, 1)
    print(f"Growth this week: {total_growth:.1f}cm")


if __name__ == "__main__":
    main()
