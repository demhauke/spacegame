import math
import pygame
from station import Station
from tile import Tile
from druid import Druid
from settings import *


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

        self.selected = False

        self.all_sprites = pygame.sprite.Group()
        self.all_collactebles = pygame.sprite.Group()
        self.all_druids = pygame.sprite.Group()

    

    def create_map(self):
        for y, x_values in enumerate(planet_map):
            for x , value in enumerate(x_values):
                #Tile(x, y, 60, "gray", [self.all_sprites])
                #if value == 1:
                #    pass
                    #Tile(x, y, 60, "gray", self.all_sprites)
                if value == 2:
                    Tile(x, y, "red", [self.all_sprites, self.all_collactebles], "Steine")
                elif value == 3:
                    Tile(x, y, "purple", self.all_sprites)

        #self.create_druid(2, 2, "white", [self.all_sprites, self.all_druids])
        Druid(2, 2, "white", [self.all_sprites, self.all_druids], self)


    def get_x(self, time):
        return self.a * math.cos(time * 2 * math.pi / self.T)
    
    def get_y(self, time):
        return self.p * math.sin(time * 2 * math.pi / self.T)
    
    def check_collision(self, pos, time, radius):
        if (self.get_x(time) - pos[0]) ** 2 + (self.get_y(time) - pos[1]) ** 2 <= radius ** 2:
            return True
        return False
    
    def create_druid(self, x, y, color, group):
        Druid(x, y, color, group, self)
    
    def update(self, game):
        self.all_sprites.update()
        game.screen.fill("gray")
        self.all_sprites.draw(game.screen)
        #self.all_druids.draw(game.screen)







        