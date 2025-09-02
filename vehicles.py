class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

class Bike(Vehicle):
    def move(self):
        print("Pedaling 🚴")

# Create objects
vehicles = [
    Car(),
    Plane(),
    Boat(),
    Bike()
]

# Use polymorphism
for vehicle in vehicles:
    vehicle.move()
