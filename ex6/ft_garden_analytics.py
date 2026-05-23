#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def grow(self) -> None:
        self._height += 42
        self._stats.grow_count += 1

    def get_older(self) -> None:
        self._age += 20
        self._stats.age_count += 1
        
    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)
    
    class Stats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self) -> None:
            print(f"Stats: {self.grow_count} grow, "
                  f"{self.age_count} age, {self.show_count} show")

    def show(self) -> None:
        self._stats.show_count += 1
        print(f"{self.name}: {self._height}cm, {self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = (f"Tree {self.name} now produces a shade of "
                 f"{self._height}cm long and {self.trunk_diameter}cm wide.")
        print(shade)

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.nutritional_value: int = 0
        self.harvest_season = harvest_season

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 10

    def get_older(self) -> None:
        super().get_older()
        self.nutritional_value += 10

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

def show_stats(plant: "Plant") -> None:
    plant._stats.display()

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    oak = Tree("Oak", 200.0, 365, 5.0)
    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    rose.bloom()
    print("[statistic for Rose]")
    show_stats(rose)
    rose.show()
    print("[statistic for Rose]")
    show_stats(rose)
    print("=== Tree")
    oak.show()
    print("[statistics for Oak]")
    show_stats(oak)
    oak.produce_shade()
    print("statistics for Oak")
    show_stats(oak)
    print("=== Vegetable")
    tomato.show()
    tomato.grow()
    tomato.get_older()
    tomato.show()
