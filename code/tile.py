import pygame
from settings import TILESIZE

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, group, item=None):
        super().__init__(group)
        
        self.image = pygame.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.item = item

    def do_action(self, kill=False, func=None):
        if func != None:
            func()
        
        if kill == True:
            self.kill()

    def update(self):
        pass