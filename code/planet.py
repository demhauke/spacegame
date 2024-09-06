import math
import pygame
from tile import Tile
from druid import Druid
from inventar import Inventar
from rakete import Rakete
from settings import *


class Planet():
    def __init__(self, name, info, game):
        self.name = name
        self.T = info["T"]

        self.p = info["a"] * (1 - info["e"])
        self.a = info["a"] * (1 + info["e"])


        self.radius = info["radius"] * 80

        self.map = info['map']

        self.selected = False

        self.raketen = []
        self.druids = []
        self.fahrzeuge = []



        self.all_sprites = pygame.sprite.Group()
        self.all_action_items = pygame.sprite.Group()
        self.all_druids = pygame.sprite.Group()

        self.game = game

        self.create_rocket()

        if name == "Erde":
            self.druids.append(Inventar())

    def create_rocket(self):
        self.raketen.append(Rakete())

    def start_fly(self):
        if self.raketen == []:
            return
        
        self.raketen[0].druids.append(Inventar(self.druid.items))
        self.druid.kill()
        self.druids = []
        self.game.planet_fly_planer[0] = self
        self.game.change_to_space_view()
        self.game.click_on_planet = self.game.select_for_fly

    

    def create_map(self):
        for y, x_values in enumerate(self.map):
            for x , value in enumerate(x_values):
                #Tile(x, y, 60, "gray", [self.all_sprites])
                #if value == 1:
                #    pass
                    #Tile(x, y, 60, "gray", self.all_sprites)
                if value == 2:
                    Tile(x, y, "red", [self.all_sprites, self.all_action_items], "Steine")
                elif value == 3:
                    Tile(x, y, "purple", [self.all_sprites, self.all_action_items], "rakete", self.start_fly)
                elif value == 4:
                    Tile(x, y, "yellow", [self.all_sprites, self.all_action_items], "Gold")

        #self.create_druid(2, 2, "white", [self.all_sprites, self.all_druids])

        for druid in self.druids:
            print(druid.items)
            self.druid = Druid(2, 2, "white", [self.all_sprites, self.all_druids], self, druid.items)


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

    def kill_on_map(self, x, y):
        self.map[int(y)][int(x)] = 0
    
    def update(self, game):
        self.all_sprites.update()
        game.screen.fill("gray")
        self.all_sprites.draw(game.screen)
        #self.all_druids.draw(game.screen)



