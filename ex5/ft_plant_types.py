#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = height
        self._age = age

    def grow(self) -> None:
        self._height += 42

    def get_older(self) -> None:
        self._age += 20

    def show(self) -> None:
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
            print(f"{self.name} is not blooming yet.")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide")
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
        self.nutritional_value += 1
    def get_older(self) -> None:
        super().get_older()
        self.nutritional_value += 1
    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")
        

if __name__ == "__main__":
    tomato = Vegetable("Tomato", 5.0, 10, "April")