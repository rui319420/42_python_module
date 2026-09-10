

class Plant:
    class Statistics:
        def __init__(self) -> None:
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0

        def increment_grow(self) -> None:
            self._grow_count += 1

        def increment_age(self) -> None:
            self._age_count += 1

        def increment_show(self) -> None:
            self._show_count += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, "
                f"{self._age_count} age, "
                f"{self._show_count} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name
        self._height: float = height if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0
        self._stats: Plant.Statistics = self.Statistics()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def show(self) -> None:
        self._stats.increment_show()
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.increment_grow()
        if self._name == "Rose":
            increment = 8.0
        elif self._name == "Sunflower":
            increment = 30.0
        else:
            increment = 0.5
        self._height = round(self._height + increment, 1)

    def age(self) -> None:
        self._stats.increment_age()
        self._age += 20 if self._name == "Sunflower" else 1

    def get_stats(self) -> "Plant.Statistics":
        return self._stats

    def get_name(self) -> str:
        return self._name


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
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

        def increment_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter: float = trunk_diameter
        self._tree_stats = self.TreeStatistics()
        self._stats = self._tree_stats

    def produce_shade(self) -> None:
        self._tree_stats.increment_shade()
        print(
            f"Tree {self._name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter:.1f}cm")


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
