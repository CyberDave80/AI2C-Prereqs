class Spacecraft:
    def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency

    def add_fuel(self, amount: float) -> None:
        self.fuel_level += amount

    def calculate_required_fuel(self, distance: float) -> float:
        return distance / self.fuel_efficiency

    def check_fuel(self, distance: float) -> bool:
        return self.fuel_level >= self.calculate_required_fuel(distance)

    def launch(self, distance: float) -> None:
        if self.check_fuel(distance):
            self.fuel_level -= self.calculate_required_fuel(distance)
            print(f"{self.name} has successfully traveled {distance} units!")
        else:
            print(f"{self.name} does not have enough fuel to travel {distance} units.")
