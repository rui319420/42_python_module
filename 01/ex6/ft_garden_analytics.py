

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def grow(self) -> None:
            self._grow_count += 1

        def age(self) -> None:
            self._age_count += 1

        def show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        if height >= 0:
            self._height: float = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0

        if age >= 0:
            self._age: int = age
        else:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        self._stats: Plant.Statistics = self.Statistics()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats.show()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.grow()
        if self._name == "Rose":
            increment = 0.8
        elif self._name == "Cactus":
            increment = 0.3
        elif self._name == "Sunflower":
            increment = 1.5
        elif self._name == "Tomato":
            increment = 2.1
        else:
            increment = 0.5
        self._height = round(self._height + increment, 1)

    def age(self) -> None:
        self._stats.age()
        self._age += 1

    def set_height(self, new_height: float) -> None:
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, new_age: int) -> None:
        if new_age >= 0:
            self._age = new_age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> "Plant.Statistics":
        return self._stats

    def get_name(self) -> str:
        return self._name


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._is_blooming:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int, color: str, seeds: int = 0
    ) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = seeds

    def bloom(self) -> None:
        super().bloom()
        if self._seeds == 0:
            self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Tree(Plant):
    class TreeStatistics(Plant.Statistics):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def produce_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: float = trunk_diameter
        self._tree_stats = self.TreeStatistics()
        self._stats = self._tree_stats

    def produce_shade(self) -> None:
        self._tree_stats.produce_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: float = 0.0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self.nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value:g}")


def display_plant_statistics(plant: Plant) -> None:
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old ===")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"[statistics for {rose.get_name()}]")
    display_plant_statistics(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print(f"[statistics for {rose.get_name()}]")
    display_plant_statistics(rose)

    print("=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak.get_name()}]")
    display_plant_statistics(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak.get_name()}]")
    display_plant_statistics(oak)

    print("=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print(f"[statistics for {sunflower.get_name()}]")
    display_plant_statistics(sunflower)

    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age()
    sunflower.bloom()
    sunflower.show()
    print(f"[statistics for {sunflower.get_name()}]")
    display_plant_statistics(sunflower)

    print("=== Anonymous ===")
    unknown = Plant.create_anonymous()
    unknown.show()
    print(f"[statistics for {unknown.get_name()}]")
    display_plant_statistics(unknown)


if __name__ == "__main__":
    main()
