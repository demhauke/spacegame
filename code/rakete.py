import math

class Rakete():
    def __init__(self):
        self.items = {
            "Steine": 0
        }
        self.humans = []

        self.x = 0
        self.y = 0

        self.start_planet = None
        self.destination_planet = None

        self.start_time = 0

        self.velocity = 5000

    def get_landet(self, time):
        if self.get_x(time) ** 2 + self.get_y(time) ** 2 >= self.destination_planet.get_x(time) ** 2 + self.destination_planet.get_y(time) ** 2:
            return True
        return False

    def get_x(self, time):
        return self.start_planet.get_x(self.start_time) + (time - self.start_time) * self.velocity * math.cos(self.angle) + self.destination_planet.get_x(time) - self.destination_planet.get_x(self.start_time)

    def get_y(self, time):
        return self.start_planet.get_y(self.start_time) - (time - self.start_time) * self.velocity * math.sin(self.angle) + self.destination_planet.get_y(time) - self.destination_planet.get_y(self.start_time)

    def fly(self, old, new, current_time):
        self.start_time = current_time
        self.start_planet = old
        self.destination_planet = new

        self.angle = -1* math.atan(math.atan((self.destination_planet.get_y(self.start_time) - self.start_planet.get_y(self.start_time)) / (self.destination_planet.get_x(self.start_time) - self.start_planet.get_x(self.start_time))))
        print(f"starte bei {old.name}")
        if self in old.station.fahrzeuge:
            old.station.fahrzeuge.remove(self)
        print(f"lande bei {new.name}")