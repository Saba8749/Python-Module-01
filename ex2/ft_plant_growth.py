#!/usr/bin/env python3
class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.age: int = 0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self) -> None:
        self.height += 0.6

    def get_older(self) -> None:
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant()
    rose.name = "Rose"
    rose.height = 24
    rose.age = 29
    start_height = rose.height
    for i in range(7):
        rose.grow()
        rose.get_older()
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")
