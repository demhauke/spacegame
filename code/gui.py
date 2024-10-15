import pygame
import time
from settings import item_to_path


def nothing(a=1):
    print(a)


class GUI:
    def __init__(self, game):    
        self.screen = game.screen
        self.all_elements = []

        self.game = game

        self.font = pygame.font.SysFont(None, 48)

    def create_button(self, pos, text, func=nothing, color="black", display_not = "", background_color=(0, 0, 0, 125), selection_possible=False):
        self.all_elements.append(Button(pos, text, self.font, color, func, display_not, background_color, selection_possible))

    def create_text(self, pos, text, color="black", display_not = "", background_color=(0, 0, 0)):
        self.all_elements.append(Text(pos, text, self.font, color, display_not, background_color))

    def create_list_of_elements(self, item_list, start_pos):
        self.all_elements.append(List_of_Elements(item_list, start_pos, self.font))

    def create_surface(self, x, y, width, height, color):
        self.all_elements.append(Surface(x, y, width, height, color))

    def update(self, game):
        for element in self.all_elements:
            element.update(game)

    def render(self):
        #self.screen.fill("black")
        self.game.gui = self
        for element in self.all_elements:
            element.render(self.game.current_planet)

    def draw(self):
        for element in self.all_elements:
            element.draw(self.screen)

class Text:
    def __init__(self, pos, text, font, color, display_not, background_color):
        self.pos = pos
        self.text = text
        self.font = font
        self.color = color
        self.background_color = background_color

        self.display_not = display_not

        self.offset = 3
        
    def render(self, info, text=False):
        if text != False:
            value = text
        else:
            try: 
                
                value = str(getattr(info, self.text))
            except:
                value = self.text
            
            if value == self.display_not:
                return
            
        self.rendered_text = self.font.render(value, True, self.color, None) #check this None
        self.rect = self.rendered_text.get_rect(topleft=self.pos)
        self.rect.x = self.pos[0] - self.rendered_text.get_width() / 2
        self.rect = self.rect.inflate(self.offset, self.offset)

        self.surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.surface.fill((255, 255, 255, 150))

    def draw(self, screen):
        #self.surface.fill((255, 255, 255, 128))
        #pygame.draw.rect(screen, self.background_color, self.rect)
        screen.blit(self.surface, self.rect.topleft)
        screen.blit(self.rendered_text, (self.pos[0] - self.rendered_text.get_width() / 2, self.pos[1]))

    def get_width(self):
        return self.rect.width
        

    def update(self, game):
        pass


class Button(Text):
    def __init__(self, pos, text, font, color, func, display_not, background_color, selection_possible):
        super().__init__(pos, text, font, color, display_not, background_color)
        self.func = func

        self.selection_possible = selection_possible    

    def update(self, game):
        if  not pygame.mouse.get_pressed()[0]:
            return
        
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            
            self.func()
            time.sleep(0.1)

class List_of_Elements():
    def __init__(self, item_list, start_pos, font):
        self.all_elements = []
        self.all_text_elements = []
        self.all_surface = []
        x = start_pos[0]
        y = start_pos[1]

        for item in item_list.items():
            print(item)
            self.all_surface.append(Surface(x - 30, y - 20, 10, 10, "gray", item_to_path[item[0]]))
            self.all_text_elements.append(Text([x, y], str(item[1]), font, "black", "", (0, 0, 0)))

            x += 150

        self.all_elements = self.all_surface + self.all_text_elements

    def render(self, info):
        for element in self.all_elements:
            element.render(info)

    def render_list(self, info):
        for index, element in enumerate(self.all_text_elements):
            print(index, element)
            print(info[index])
            element.render("s", text=info[index])

        self.all_elements = self.all_surface + self.all_text_elements

    def draw(self, screen):
        for element in self.all_elements:
            element.draw(screen)

    def update(self, game):
        for element in self.all_elements:
            element.update(game)
        
class Surface():
    def __init__(self, x, y, width, height, color, image=False):
        #self.rect = pygame.rect.Rect(x, y, width, height)

        if image != False:
            print("Bild")
            print(x, y)
            self.surface = pygame.image.load(image)
            self.rect = pygame.rect.Rect(x, y, self.surface.get_width(), self.surface.get_height())
        else:
            self.rect = pygame.rect.Rect(x, y, width, height)
            self.surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)   

            self.surface.fill(color)

    def draw(self, screen):
        screen.blit(self.surface, self.rect.topleft)

    def render(self, info):
        pass

    def update(self, info):
        pass
