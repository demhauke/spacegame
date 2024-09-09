import pygame
from settings import TILESIZE

class Camera(pygame.sprite.Group):
    def __init__(self, display):
        super().__init__()

        #self.display_surface = pygame.display.get_surface()
        self.display_surface = display

        self.offset = pygame.math.Vector2()

        self.display_half_w = self.display_surface.get_size()[0] / 2
        self.display_half_h = self.display_surface.get_size()[1] / 2

    def draw(self, center_target):

        self.offset.x = center_target.rect.centerx - self.display_half_w
        self.offset.y = center_target.rect.centery - self.display_half_h

        for sprite in self.sprites():
            sprite_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, sprite_pos)



class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, group, item=None, func=None, image="Steine"):
        super().__init__(group)
        
        #self.image = pygame.Surface((TILESIZE, TILESIZE))
        #self.image.fill(color)
        self.image = pygame.image.load(f"spacegame/graphics/{image}.png")
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        
        self.rect = self.image.get_rect()

        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        self.item = item
        self.func = func

    def do_action(self, kill=False, func=None):
        if func != None:
            func()
        
        if kill == True:
            self.kill()

    def update(self):
        pass

class Rocket_Station(Tile):
    def __init__(self, x, y, color, group, item=None):
        super().__init__(x, y, color, group, item)

        self.rockets = []

