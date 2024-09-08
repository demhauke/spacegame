import math
from inventar import Inventar

class Rakete(Inventar):
    def __init__(self):
        super().__init__()
        self.druids = []

        self.start_planet = None
        self.destination_planet = None

        self.start_time = 0

        self.velocity = 5000

        self.inventar_ = self.get_inventar()

    def get_landet(self, time):
        if time >= self.landing_time:
            print(f"lande bei {self.destination_planet.name}")
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

        self.landing_time = current_time + math.sqrt((old.get_x(current_time) - new.get_x(current_time)) ** 2 + (old.get_y(current_time) - new.get_y(current_time)) ** 2) / self.velocity

        self.angle = (-1) * math.atan2((self.destination_planet.get_y(self.start_time) - self.start_planet.get_y(self.start_time)) , (self.destination_planet.get_x(self.start_time) - self.start_planet.get_x(self.start_time)))
        print(f"starte bei {old.name}")

    def update(self):
        self.inventar_ = self.get_inventar()