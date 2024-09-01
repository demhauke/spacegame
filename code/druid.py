from entity import Entity
from inventar import Inventar
import pygame


class Druid(Entity, Inventar):
    def __init__(self, x, y, color, group, planet):
        super().__init__(x, y, color, group)
        Inventar().__init__()
        self.direction = pygame.math.Vector2()

        self.items = {
            "Steine": 0,
            "Gold": 0,
            "Eisen": 0
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

        collision_sprite = self.check_collision(self.planet.all_collactebles)

        self.check_action_e(keys, collision_sprite)

    def check_action_e(self, keys, collision_sprite):
        if keys[pygame.K_e] == False:
            return

        if collision_sprite != False:

            self.append_items(collision_sprite.item, 5)
            collision_sprite.kill()

            print(self.get_inventar())
        



    def update(self):
        self.get_keyboardinput()
        super().update()