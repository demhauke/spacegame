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


        self.create_planets()

        self.current_planet = self.all_planets[2]


        self.create_gui()

        self.current_mode = self.space_overview

        self.click_on_planet = self.change_to_planet_view

        self.planet_fly_planer = [False, False]


    def run(self):
        running = True
        while running:
            self.update()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

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

    def create_gui(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.planet_station_gui = GUI(self)

        self.gui = self.planet_station_gui


        self.planet_station_gui.create_text([self.screen_width / 2, 20], "name")

        self.planet_station_gui.create_button([self.screen_width / 2, self.screen_height - 100], "Map", self.change_to_space_view)

    def planet_station(self):
        self.gui.update(self)
        self.current_planet.station.update()
        self.current_planet.update(self)
        self.gui.render()

    def space_overview(self):
        time = (pygame.time.get_ticks() + self.starttime) / self.speed

        self.screen.fill("black")

        
        pygame.draw.circle(self.screen, "white", (self.screen_width / 2, self.screen_height / 2), 20 / self.map_scale)

        for rakete in self.all_rockets:
            pygame.draw.circle(self.screen, "red", (self.screen_width / 2 + rakete.get_x(time) / self.map_scale, self.screen_height / 2 + rakete.get_y(time) / self.map_scale), 5 / self.map_scale)


            if rakete.get_landet(time):
                rakete.destination_planet.station.fahrzeuge.append(rakete)
                for druid in rakete.druids:
                    rakete.destination_planet.station.druids.append(druid)
                self.all_rockets.remove(rakete)

        x, y = pygame.mouse.get_pos()
        x = (x - self.screen_width / 2)
        y = (y - self.screen_height / 2)

        for planet in self.all_planets:
            pygame.draw.circle(self.screen, "white", (self.screen_width / 2 + planet.get_x(time) / self.map_scale, self.screen_height / 2 + planet.get_y(time) / self.map_scale), planet.radius / self.map_scale)

            if self.mousebuttonpressed == False:
                continue

            if planet.check_collision((x, y), time, planet.radius):
                print("collision")
                self.click_on_planet(planet)
                self.mousebuttonpressed = False
                break

        if self.planet_fly_planer[0] == False:
            return
        
        if self.planet_fly_planer[1] == False:
            pygame.draw.line(self.screen, "white", (self.screen_width / 2 + self.planet_fly_planer[0].get_x(time) / self.map_scale, self.screen_height / 2 + self.planet_fly_planer[0].get_y(time) / self.map_scale), (x + self.screen_width / 2, y + self.screen_height / 2))
            return
        
        #pygame.draw.line(self.screen, "white", (self.screen_width / 2 + self.planet_fly_planer[0].get_x(time) / self.map_scale, self.screen_height / 2 + self.planet_fly_planer[0].get_y(time) / self.map_scale), (self.screen_width / 2 + self.planet_fly_planer[1].get_x(time) / self.map_scale, self.screen_height / 2 + self.planet_fly_planer[1].get_y(time) / self.map_scale))
        
        self.all_rockets.append(self.planet_fly_planer[0].station.raketen[0])
        self.planet_fly_planer[0].station.raketen[0].fly(self.planet_fly_planer[0], self.planet_fly_planer[1], time)

        self.planet_fly_planer = [False, False]


        self.click_on_planet = self.change_to_planet_view



        #self.all_rockets.append(self.planet_fly_planer[0].station.raketen[0])

    def station_do_activity(self):
        self.current_planet.station.do_activity()
        self.gui.render()

    def station_select_activity(self, index):
        self.current_planet.station.select_activity(index)

    def station_select_human(self, index):
        self.current_planet.station.select_human(index)

    def station_select_rakete(self, index):
        self.current_planet.station.select_rakete(index)

    def station_change_item_from_rocket_to_station(self, index):
        self.current_planet.station.change_item_at_station(index, self.current_planet.station.raketen[self.current_planet.station.selected_raketen_index], self.current_planet.station)
        self.gui.render()

    def station_change_item_from_station_to_rocket(self, index):
        self.current_planet.station.change_item_at_station(index, self.current_planet.station, self.current_planet.station.raketen[self.current_planet.station.selected_raketen_index])
        self.gui.render()

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



    def change_to_space_view(self):
        for sprite in self.current_planet.all_sprites:
            sprite.kill()
        self.current_mode = self.space_overview

        

game = Game()
game.run()

