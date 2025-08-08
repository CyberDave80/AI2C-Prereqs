class Spacecraft:
    def __init__(self, name = "bobross", fuel_level = 0, fuel_efficiency = 0):
        self.name = name
        self.fuel_level = fuel_level
        self.fuel_efficiency = fuel_efficiency

    def add_fuel(self, fuel: int) -> int:
        self.fuel_level += fuel
        return self.fuel_level

    def calc_fuel_eff(self, difficulty: int):
        if difficulty == 1:
            self.fuel_efficiency = 1.0
        elif difficulty == 2:
            self.fuel_efficiency = 0.8
        elif difficulty == 3:
            self.fuel_efficiency = 0.5

    def check_fuel(self):
        if self.fuel_level <= 0:
            print("Out of fuel!")
            return False
        else:
            return self.fuel_level

    def launch(self, has_fuel: bool):
        if has_fuel:
            print(f"{self.name} launched successfully!")


class Planet:
    def __init__(
        self,
        name = "plant bob",
        coordinates = [0,0,0],
        danger = 0,
        resources = 0,
        atmosphere = "Hot",
    ):
        self.name = name
        self.coordinates = coordinates
        self.danger = danger
        self.resources = resources
        self.atmosphere = atmosphere

    def __str__(self):
        return f"Planet: {self.name} at {self.coordinates}"
    
    def calc_fuel_required(self, coordinates: list, fuel_eff: int):
        self.coordinates = coordinates
        distance = sum(abs(coord) for coord in coordinates)
        fuel_required = distance * fuel_eff
        return fuel_required


class Player:
    def __init__(self, name = "bob", difficulty = 1):
        self.name = name
        self.difficulty = difficulty
        self.spacecraft = None
        self.planets = []
        self.credits = 0
        self.fuel = 0
        self.mission_rewards = []

    def visited_planets(self):
        return [planet.name for planet in self.planets]

    def buy_fuel(self):
        fuel = 0
        if self.credits > 0:
            fuel = int(input("How much fuel would you like to buy? "))
            self.fuel += fuel
            self.credits -= fuel * 10
        else:
            print("You do not have enough credits to buy fuel.")
            return self.fuel

    def calc_score(self):
        score = len(self.visited_planets()) + self.credits + self.fuel
        return score
    
    def display_status(self):
        print(f"Player: {self.name}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Credits: {self.credits}")
        print(f"Fuel: {self.fuel}")
        print(f"Visited Planets: {', '.join(self.visited_planets())}")
        print(f"Rewards: {self.mission_rewards}")
        if self.spacecraft:
            print(f"Spacecraft: {self.spacecraft.name} with fuel level {self.spacecraft.fuel_level}")
        else:
            print("No spacecraft assigned.")

    def simulate_mission(self):
        if not self.planets:
            print("No planets available. Add planets first.")
            return
        if not self.spacecraft:
            print("No spacecraft assigned. Please assign a spacecraft before launching a mission.")
            return
        
        print("Available planets:")
        for i, planet in enumerate(self.planets, 1):
            print(f"{i}. {planet.name}")
        
        choice = input("Choose a planet (enter name): ")
        selected_planet = None
        for planet in self.planets:
            if planet.name == choice:
                selected_planet = planet
                break
        
        if selected_planet:
            print(f"Launching mission to {selected_planet.name}...")
            fuel_required = selected_planet.calc_fuel_required(selected_planet.coordinates, self.spacecraft.fuel_efficiency)
            if self.spacecraft.fuel_level >= fuel_required:
                self.spacecraft.fuel_level -= fuel_required
                self.credits += 100
                print(f"Mission successful! Earned 100 credits.")
            else:
                print(f"Not enough fuel! Need {fuel_required}, have {self.spacecraft.fuel_level}")
        else:
            print("Planet not found.")

def menu():
    player = Player()
    spacecraft = Spacecraft()
    planet = Planet()

    while True:
        print("\nWelcome to Space Exploration")
        print("1. View Planets")
        print("2. Check Fuel")
        print("3. Add Fuel")
        print("4. Display Stats")
        print("5. Launch Mission")
        print("6. Add planets")
        print("7: Add Player")
        print("8: Add Space Craft")
        print("0. Exit")
        
        choice = int(input("Please choose an option: "))
        match choice:
            case 1:
                print(planet)
            case 2:
                print(f"Fuel level: {spacecraft.fuel_level}")
            case 3:
                fuel_to_add = int(input("How much fuel to add? "))
                spacecraft.add_fuel(fuel_to_add)
            case 4:
                player.display_status()
            case 5:
                print("Launching mission...")
                #player.simulate_mission()
            case 6:
                planet_name = input("New Planet name: ")
                coordinates = list(map(int, input("Coordinates (space-separated): ").split()))
                danger = int(input("Danger level: "))
                resources = int(input("Resources: "))
                atmosphere = input("Atmosphere description: ")
                new_planet = Planet(planet_name, coordinates, danger, resources, atmosphere)
                player.planets.append(new_planet)
                print(f"Planet {new_planet.name} added.")
            case 7:
                player_name = input("Player's name: ")
                difficulty = int(input("Difficulty (1-3): "))
                player = Player(player_name, difficulty)
            case 8:
                craft_name = input("Spacecraft name: ")
                fuel_level = int(input("Fuel Level: "))
                fuel_efficiency = float(input("Fuel efficiency: "))
                spacecraft = Spacecraft(craft_name, fuel_level, fuel_efficiency)
                player.spacecraft = spacecraft
                print(f"Spacecraft {spacecraft.name} added.")
            case 0:
                print("Goodbye!")
                break
            case _:
                print("Invalid option. Please try again.") 

if __name__ == "__main__":
    menu()