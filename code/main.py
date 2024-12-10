from settings import *
from planet import Planet
from gui import GUI
import pygame

class Game():
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.starttime = 160000
        self.mousebuttonpressed = False


        self.screen_width = 1500
        self.screen_height = 500
        
        self.all_planets = []
        self.all_rockets = []


        self.speed = 100000
        self.map_scale = 1


        self.create_gui()
        self.create_planets()

        self.current_planet = self.all_planets[2]
        self.selected_planet_index = 2


        self.current_mode = self.space_overview
        #self.current_mode = self.planet_station

        self.click_on_planet = self.change_to_planet_view

        self.planet_fly_planer = [False, False]


        self.space_overview_gui.render()

        self.enter_pressed = self.enter_pressed_space_view



    def run(self):
        running = True
        while running:
            self.update()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.tab_pressed()

                    elif event.key == pygame.K_LEFT:
                        self.left_pressed()

                    elif event.key == pygame.K_RIGHT:
                        self.right_pressed()

                    elif event.key == pygame.K_e or event.key == pygame.K_RETURN:
                        self.enter_pressed()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: 
                        self.mousebuttonpressed = True
                else:
                    self.mousebuttonpressed = False


                self.check_inputs(event)

    def update(self):
        self.current_mode()
        pygame.display.flip()
        self.clock.tick(60)

    def change_game_mode(self, direction):
        pass

    def check_inputs(self, event):
        if event.type == pygame.MOUSEWHEEL:
            self.map_scale += event.y

            if self.map_scale == 0:
                self.map_scale = 1

        if event.type == pygame.K_LEFT:
            self.change_game_mode(-1)

        if event.type == pygame.K_RIGHT:
            self.change_game_mode(1)

    def create_planets(self):
        for planet in planeten.keys():
            self.all_planets.append(Planet(planet, planeten[planet], self))

    def get_planet(self, name):
        for planet in self.all_planets:
            if planet.name == name:
                return planet

    def get_name_of_selected_planet(self):
        return self.all_planets[self.selected_planet_index].name
    
    def get_name_of_current_planet(self):
        return self.current_planet.name
    
    def get_current_druid_items(self):
        return self.current_planet.get_druid().items

    def create_gui(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.planet_station_gui = GUI(self)
        self.inventory_gui = GUI(self)

        self.space_overview_gui = GUI(self)

        self.gui = self.space_overview_gui


        #self.space_overview_gui.create_button)

        self.space_overview_gui.create_text([self.screen_width / 2, 20], "Planet", getter=self.get_name_of_selected_planet)


        self.planet_station_gui.create_text([self.screen_width / 2, 20], "name", getter=self.get_name_of_current_planet)

        self.planet_station_gui.create_button([self.screen_width / 2, self.screen_height - 100], "Map", func=self.change_to_space_view)



        self.inventory_gui.create_text([self.screen_width / 2, 20], "Inventar")

        self.inventory_gui.create_surface(0, 0, self.screen_width, self.screen_height, (255, 255, 255, 150))

        self.inventory_gui.create_list_of_elements({
                "Steine": 0,
                "Kupfer": 0,
                "Gold": 0,
                "Eisen": 0
            },
            self.get_current_druid_items,
            [100, self.screen_height - 100]
            )

        self.inventory_gui.create_list_of_elements({
                "Steine": 0,
                "Kupfer": 0,
                "Gold": 0,
                "Eisen": 0
            },
            self.get_current_druid_items,
            [100, 100]      
            )

    def tab_pressed(self):
        if self.gui == self.planet_station_gui:
            self.gui = self.inventory_gui
            self.gui.render()
            self.render_inventar_gui(self.current_planet.druids[0].get_inventar_amount())           
            return
        
        self.gui = self.planet_station_gui

    def left_pressed(self):
        if self.current_mode != self.space_overview:
            return
        if self.selected_planet_index > 0:
            self.selected_planet_index += -1

        self.render_gui()

    def right_pressed(self):
        if self.current_mode != self.space_overview:
            return
        if self.selected_planet_index < len(self.all_planets) - 1: 
            self.selected_planet_index += 1

        self.render_gui()

    def enter_pressed(self):
        print("enter")

    def render_inventar_gui(self, inventar):
        print(inventar)
        self.inventory_gui.all_elements[-1].render_list(inventar)

    def render_gui(self):
        self.gui.render()

    def planet_station(self):
        self.gui.update(self)
        self.current_planet.update(self)
        self.gui.draw()

    def space_overview(self):
        time = (pygame.time.get_ticks() + self.starttime) / self.speed

        self.screen.fill("black")

        
        pygame.draw.circle(self.screen, "white", (self.screen_width / 2, self.screen_height / 2), 20 / self.map_scale)

        for rakete in self.all_rockets:
            pygame.draw.circle(self.screen, "red", (self.screen_width / 2 + rakete.get_x(time) / self.map_scale, self.screen_height / 2 + rakete.get_y(time) / self.map_scale), 5 / self.map_scale)


            if rakete.get_landet(time):
                rakete.destination_planet.fahrzeuge.append(rakete)
                for druid in rakete.druids:
                    rakete.destination_planet.druids.append(druid)

                self.current_planet = rakete.destination_planet
                self.all_rockets.remove(rakete)
                

        x, y = pygame.mouse.get_pos()
        x = (x - self.screen_width / 2)
        y = (y - self.screen_height / 2)

        for planet in self.all_planets:
            pygame.draw.circle(self.screen, "white", (self.screen_width / 2 + planet.get_x(time) / self.map_scale, self.screen_height / 2 + planet.get_y(time) / self.map_scale), planet.radius / self.map_scale)

            if planet.druids != []:
                pygame.draw.circle(self.screen, "purple", (self.screen_width / 2 + planet.get_x(time) / self.map_scale, self.screen_height / 2 + planet.get_y(time) / self.map_scale), planet.radius / self.map_scale * 2, 1)

            if self.mousebuttonpressed == False:
                continue

            if planet.check_collision((x, y), time, planet.radius):
                print("collision")
                self.click_on_planet(planet)
                self.mousebuttonpressed = False
                break

        pygame.draw.circle(self.screen, "blue", (self.screen_width / 2 + self.all_planets[self.selected_planet_index].get_x(time) / self.map_scale, self.screen_height / 2 + self.all_planets[self.selected_planet_index].get_y(time) / self.map_scale), self.all_planets[self.selected_planet_index].radius / self.map_scale * 3, 1)

        self.gui.draw()

        if self.planet_fly_planer[0] == False:
            return
        
        if self.planet_fly_planer[1] == False:
            pygame.draw.line(self.screen, "white", (self.screen_width / 2 + self.planet_fly_planer[0].get_x(time) / self.map_scale, self.screen_height / 2 + self.planet_fly_planer[0].get_y(time) / self.map_scale), (x + self.screen_width / 2, y + self.screen_height / 2))
            return
        
        #pygame.draw.line(self.screen, "white", (self.screen_width / 2 + self.planet_fly_planer[0].get_x(time) / self.map_scale, self.screen_height / 2 + self.planet_fly_planer[0].get_y(time) / self.map_scale), (self.screen_width / 2 + self.planet_fly_planer[1].get_x(time) / self.map_scale, self.screen_height / 2 + self.planet_fly_planer[1].get_y(time) / self.map_scale))
        
        self.all_rockets.append(self.planet_fly_planer[0].raketen[0])
        self.planet_fly_planer[0].raketen[0].fly(self.planet_fly_planer[0], self.planet_fly_planer[1], time)

        self.planet_fly_planer = [False, False]


        self.click_on_planet = self.change_to_planet_view



        #self.all_rockets.append(self.planet_fly_planer[0].station.raketen[0])


    def select_for_fly(self, planet):
        if self.planet_fly_planer[0] == False:
            self.planet_fly_planer = [planet, False]
        elif self.planet_fly_planer[0] != planet:
            self.planet_fly_planer = [self.planet_fly_planer[0], planet]

        print(self.planet_fly_planer)

    def change_to_planet_view(self, planet):
        self.current_planet = planet
        self.current_mode = self.planet_station
        planet.create_map()
        self.planet_station_gui.render()
        self.gui = self.planet_station_gui

        self.enter_pressed = self.enter_pressed_planet_view

    def change_to_space_view(self):
        for sprite in self.current_planet.all_sprites:
            sprite.kill()
        self.current_mode = self.space_overview
        self.space_overview_gui.render()
        self.gui = self.space_overview_gui

        self.enter_pressed = self.enter_pressed_space_view

    def enter_pressed_space_view(self):
        self.change_to_planet_view(self.all_planets[self.selected_planet_index])

    def enter_pressed_planet_view(self):
        print("Enter")
        

game = Game()
game.run()

