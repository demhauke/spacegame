from entity import Entity
from inventar import Inventar
from settings import TILESIZE
import pygame


class Druid(Entity, Inventar):
    def __init__(self, x, y, color, group, planet, items=False, tools=False, image="Steine"):
        super().__init__(x, y, color, group, image=image)
        Inventar().__init__(items, tools)
        self.direction = pygame.math.Vector2()

        if items:
            self.items = items
        else:
            self.items = {
                "Steine": 0,
                "Kupfer": 0,
                "Gold": 0,
                "Eisen": 0
            }
        if tools:
            self.tools = tools
        else:
            self.tools = {
                "Spitzhacke": False
            }

        self.planet = planet


    def get_keyboardinput(self):

        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_UP]:
            self.direction[1] = -1
        elif keys[pygame.K_DOWN]:
            self.direction[1] = 1
        else:
            self.direction[1] = 0

        if keys[pygame.K_LEFT]:
            self.direction[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.direction[0] = 1
        else:
            self.direction[0] = 0

        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        collision_sprite = self.check_collision(self.planet.all_action_items)

        self.check_action_e(keys, collision_sprite)

    def check_action_e(self, keys, collision_sprite):
        if keys[pygame.K_e] == False:
            return

        if collision_sprite != False:

            collision_sprite.do_action(self)

            #if collision_sprite.item in self.items.keys():

             #   self.append_items(collision_sprite.item, 5)
              #  self.planet.kill_on_map(collision_sprite.rect.x / TILESIZE, collision_sprite.rect.y / TILESIZE)
               # collision_sprite.kill()
                #
            self.planet.update_inventory_gui(self.get_inventar_amount())
                #return
            

            if collision_sprite.item == "rakete":
                collision_sprite.func()
            


    def update(self):
        self.get_keyboardinput()
        super().update()