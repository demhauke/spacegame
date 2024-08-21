import math
from station import Station


class Planet():
    def __init__(self, name, info):
        self.name = name
        if name == "Erde":
            print("ja")
        self.T = info["T"]

        self.p = info["a"] * (1 - info["e"])
        self.a = info["a"] * (1 + info["e"])


        self.station = Station(name, info['buildings'])

        self.radius = info["radius"] * 80

    def get_x(self, time):
        return self.a * math.cos(time * 2 * math.pi / self.T)
    
    def get_y(self, time):
        return self.p * math.sin(time * 2 * math.pi / self.T)
    
    def check_collision(self, pos, time, radius):
        if (self.get_x(time) - pos[0]) ** 2 + (self.get_y(time) - pos[1]) ** 2 <= radius ** 2:
            return True
        return False







        