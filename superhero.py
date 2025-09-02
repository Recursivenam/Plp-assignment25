class Superhero:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Health: {self.health}")

    def attack(self):
        print(f"{self.name} is attacking with {self.power}!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Remaining health: {self.health}")

class FlyingSuperhero(Superhero):
    def __init__(self, name, power, health, flight_speed):
        super().__init__(name, power, health)
        self.flight_speed = flight_speed

    def fly(self):
        print(f"{self.name} is flying at {self.flight_speed} km/h!")

    def display_info(self):
        super().display_info()
        print(f"Flight Speed: {self.flight_speed} km/h")

# Create objects
superman = FlyingSuperhero("Superman", "Heat Vision", 100, 1000)
batman = Superhero("Batman", "Martial Arts", 80)

# Use methods
superman.display_info()
superman.fly()
superman.attack()
superman.take_damage(20)

print("\n")

batman.display_info()
batman.attack()
batman.take_damage(10)
