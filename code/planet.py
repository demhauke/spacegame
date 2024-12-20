import math
import pygame
from tile import *
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



        self.all_sprites = Camera(game.screen)
        self.all_action_items = pygame.sprite.Group()
        self.all_druids = pygame.sprite.Group()

        self.game = game

        self.create_rocket()

        if name == "Erde":
            self.druids.append(Inventar())

        #self.druids.append(Inventar())

        

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
                match value:
                    case 2:
                        Sampling(x, y, "red", [self.all_sprites, self.all_action_items], "Steine", image="Steine sampling")
                    case 3:
                        self.druid =  Tile(x, y, "purple", [self.all_sprites, self.all_action_items], "rakete", self.start_fly, image="Rocket")

                        for druid in self.druids:
                            self.druid = Druid(x, y + 1, "white", [self.all_sprites, self.all_druids], self, druid.items, image="Rover")

                    case 4:
                        Sampling(x, y, "yellow", [self.all_sprites, self.all_action_items], "Kupfer", image="Kupfer sampling")

                    case 5:
                        Sampling(x, y, "yellow", [self.all_sprites, self.all_action_items], "Kupfer", image="Kohle sampling")
                    case 6:
                        Erz(x, y, "yellow", [self.all_sprites, self.all_action_items], "Kupfer", image="Kupfer")
                    case 7:
                        Erz(x, y, "red", [self.all_sprites, self.all_action_items], "Steine", image="Steine")
                    case 8:
                        Erz(x, y, "yellow", [self.all_sprites, self.all_action_items], "Kupfer", image="Kohle")

        #self.create_druid(2, 2, "white", [self.all_sprites, self.all_druids])

  #      for druid in self.druids:
 #           print(druid.items)
#            self.druid = Druid(4, 4, "white", [self.all_sprites, self.all_druids], self, druid.items, image="Rover")


    def get_x(self, time):
        return self.a * math.cos(time * 2 * math.pi / self.T)
    
    def get_y(self, time):
        return self.p * math.sin(time * 2 * math.pi / self.T)
    
    def get_druid(self):
        return self.druid
    
    def check_collision(self, pos, time, radius):
        if (self.get_x(time) - pos[0]) ** 2 + (self.get_y(time) - pos[1]) ** 2 <= radius ** 2:
            return True
        return False
    
    def create_druid(self, x, y, color, group):
        Druid(x, y, color, group, self)

    def kill_on_map(self, x, y):
        self.map[int(y)][int(x)] = 0

    def update_inventory_gui(self, inventar):
        self.game.render_inventar_gui(inventar)


    
    def update(self, game):
        self.all_sprites.update()
        game.screen.fill(backgroundcolor_per_planet[self.name])
        self.all_sprites.draw(self.druid)
        
        #self.all_druids.draw(self.game.screen)



