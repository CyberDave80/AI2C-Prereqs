class Car():
    def __init__(self,color,year,model):
        self.color = color
        self.year = year
        self.model = model
    
    def __str__(self):
        return f"{self.color} {self.year} {self.model}"
    
    def move_forward(self):
        return "Car is moving forward..."
    
    def move_backward(self):
        return "Car is moving backward..."

class Car_dealership():
    def __init__(self):
        self.inventory = {}  # {car: price}
    
    def add_car(self):
        color = input("Enter car color: ")
        year = input("Enter car year: ")
        model = input("Enter car model: ")
        car = Car(color, year, model)
        price = int(input("Enter car price: $"))
        self.inventory[car] = price
    
    def get_price(self, car):
        return self.inventory.get(car)
    
    def set_price(self, car, new_price):
        if car in self.inventory:
            self.inventory[car] = new_price
    
    def view_cars(self):
        for car, price in self.inventory.items():
            print(f"{car} - ${price}")
    
    def remove_car(self, car):
        if car in self.inventory:
            del self.inventory[car]

def menu():
    dealership = Car_dealership()
    
    while True:
        print("\nWelcome to the Car Dealership!")
        print("1. View Cars")
        print("2. Add a Car")
        print("3. Update Car Price")
        print("0. Exit")
        
        choice = int(input("Please choose an option: "))
        match choice:
            case 1:
                print("Viewing Cars...")
                dealership.view_cars()
            case 2:
                print("Adding a Car...")
                dealership.add_car()
            case 3:
                print("Updating Car Price...")
            case 0:
                print("Exiting...")
                break
            case _:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()
