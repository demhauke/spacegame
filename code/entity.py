from tile import Tile
import pygame

class Entity(Tile):
    def __init__(self, x, y, color, group, image="Steine"):
        super().__init__(x, y, color, group, image=image)

        self.speed = 4

        self.direction = pygame.math.Vector2()

    
    def move(self):
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed

    def check_collision(self, group):
        for sprite in group:
            if pygame.Rect.colliderect(self.rect, sprite.rect):
                return sprite
        
        return False


    def update(self):
        super().update()
        self.move()



