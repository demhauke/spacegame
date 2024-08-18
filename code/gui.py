import pygame
import time

def nothing(a=1):
    print(a)

class GUI:
    def __init__(self, game):    
        self.screen = game.screen
        self.all_elements = []

        self.game = game

        self.font = pygame.font.SysFont(None, 48)

    def create_button(self, pos, text, func=nothing, color="black", display_not = ""):
        self.all_elements.append(Button(pos, text, self.font, color, func, display_not))

    def create_text(self, pos, text, color="black", display_not = ""):
        self.all_elements.append(Text(pos, text, self.font, color, display_not))

    def create_list_of_elements(self, pos, get_liste, color="black", get_pressed=nothing):
        self.all_elements.append(List_of_elements(pos, get_liste, "Type", self.font, color, get_pressed))

    def update(self):
        for element in self.all_elements:
            element.update()

    def render(self):
        self.screen.fill("black")
        self.game.gui = self
        for element in self.all_elements:
            element.render(self.screen, self.game.current_planet.station)

class Text:
    def __init__(self, pos, text, font, color, display_not, background=None,):
        self.pos = pos
        self.text = text
        self.font = font
        self.color = color
        self.background = background

        self.display_not = display_not

        self.offset = 3
        
    def render(self, screen, info):
        try: 
            
            value = str(getattr(info, self.text))
        except:
            value = self.text
        
        if value == self.display_not:
            return
        self.rendered_text = self.font.render(value, True, self.color, self.background) 
        self.rect = self.rendered_text.get_rect(topleft=self.pos)
        #self.rect.update(self.pos[0] - self.rendered_text.get_width() / 2 - self.offset, -self-of)
        self.rect.x = self.pos[0] - self.rendered_text.get_width() / 2
        self.rect = self.rect.inflate(self.offset, self.offset)
        pygame.draw.rect(screen, "gray", self.rect)
        #self.pos[0] = screen.get_width() / 2 - self.rendered_text.get_width() / 2
        screen.blit(self.rendered_text, (self.pos[0] - self.rendered_text.get_width() / 2, self.pos[1]))

    def update(self):
        pass


class Button(Text):
    def __init__(self, pos, text, font, color, func, display_not):
        super().__init__(pos, text, font, color, display_not)
        self.func = func

    def update(self):
        if  not pygame.mouse.get_pressed()[0]:
            return
        
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            
            self.func()
            time.sleep(0.1)

class List_of_elements():
    def __init__(self, pos, get_liste, Type, font, color, get_pressed):
        self.pos = pos
        self.get_liste = get_liste
        self.Type = Type
        
        self.font = font
        self.color = color

        self.get_pressed = get_pressed


        
    def render(self, screen, reference):
        self.all_elements = []
        liste = getattr(reference, self.get_liste)
        print(liste)

        x = self.pos[0]

        for index, value in enumerate(liste):
            value = str(value)
            value += " "
            print(value)
            self.all_elements.append(Text((x, self.pos[1]), str(value), self.font, self.color, ""))

            self.all_elements[index].render(screen, reference)

            x += self.all_elements[index].rendered_text.get_width() + 10



    def update(self):
        if  not pygame.mouse.get_pressed()[0]:
            return
        for index, element in enumerate(self.all_elements):
            if element.rect.collidepoint(pygame.mouse.get_pos()):
            
                self.get_pressed(index)

        
        
        
