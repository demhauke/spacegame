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

    def create_button(self, pos, text, func=nothing, color="black", display_not = "", background_color=(0, 0, 0, 125), selection_possible=False):
        self.all_elements.append(Button(pos, text, self.font, color, func, display_not, background_color, selection_possible))

    def create_text(self, pos, text, color="black", display_not = "", background_color=(0, 0, 0)):
        self.all_elements.append(Text(pos, text, self.font, color, display_not, background_color))

    def create_list_of_elements(self, pos, get_liste, get_selection_index, color="black", get_pressed=nothing, display_not = "", background_color=(0, 0, 0)):
        self.all_elements.append(List_of_elements(pos, get_liste, "Type", self.font, color, get_pressed, display_not, background_color, get_selection_index))

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
        
    def render(self, info):
        try: 
            
            value = str(getattr(info, self.text))
        except:
            value = self.text
        
        if value == self.display_not:
            return
        self.rendered_text = self.font.render(value, True, self.color, None) #check this None
        self.rect = self.rendered_text.get_rect(topleft=self.pos)
        self.surface = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        self.surface.fill((255, 255, 255, 200))
        self.rect.x = self.pos[0] - self.rendered_text.get_width() / 2
        self.rect = self.rect.inflate(self.offset, self.offset)

    def draw(self, screen):
        #self.surface.fill((255, 255, 255, 128))
        #pygame.draw.rect(screen, self.background_color, self.rect)
        screen.blit(self.surface, self.rect.topleft)
        screen.blit(self.rendered_text, (self.pos[0] - self.rendered_text.get_width() / 2, self.pos[1]))
        

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

class List_of_elements():
    def __init__(self, pos, get_liste, Type, font, color, get_pressed, display_not, background_color, get_selection_index):
        self.pos = pos
        self.get_liste = get_liste
        self.Type = Type
        
        self.font = font
        self.color = color

        self.get_pressed = get_pressed
        self.get_selection_index = get_selection_index

        self.display_not = display_not

        self.background_color = background_color


        
    def render(self, screen, reference):

        self.screen = screen
        self.reference = reference

        self.all_elements = []
        liste = getattr(reference, self.get_liste)
        print(liste)

        x = self.pos[0]

        for index, value in enumerate(liste):
            value = str(value)
            value += " "
            print(value)
            self.all_elements.append(Text((x, self.pos[1]), str(value), self.font, self.color, self.display_not, self.background_color))

            self.all_elements[index].render(screen, reference)

            x += self.all_elements[index].rendered_text.get_width() * 1.5

    def check_selected(self, index, element):
        element.background_color = "gray"

        try:

            if index == getattr(self.reference, self.get_selection_index):
                element.background_color = "pink"
        except:
            pass

    def update(self, game):
        if  not pygame.mouse.get_pressed()[0]:
            return
        
        #self.check_selected()

        for index, element in enumerate(self.all_elements):
            if element.rect.collidepoint(pygame.mouse.get_pos()):
            
                self.get_pressed(index)
                #print(index)
                #element.background_color = "pink"

            self.check_selected(index, element)

            self.reference.update()

            if not self in game.gui.all_elements:
                return
            element.render(self.screen, self.reference)
        
        
        
