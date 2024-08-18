from settings import *
from planet import Planet
from gui import GUI
import pygame

mousebuttonpressed = False


class Game():
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.starttime = 160000


        self.screen_width = 1500
        self.screen_height = 500
        
        self.all_planets = []
        self.all_rockets = []


        self.speed = 100000
        self.map_scale = 1


        self.create_planets()

        self.current_planet = self.all_planets[2]


        self.create_gui()

        self.test_to_mars()

        self.current_mode = self.space_overview


    def run(self):
        running = True
        while running:
            self.update()
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


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
            self.all_planets.append(Planet(planet, planeten[planet]))

    def get_planet(self, name):
        for planet in self.all_planets:
            if planet.name == name:
                return planet

    def create_gui(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        self.planet_station_actions_gui = GUI(self)
        self.planet_station_gui = GUI(self)


        self.gui = self.planet_station_gui

        # plaet view
        #self.planet_station_gui = GUI(self.screen)

        self.planet_station_gui.create_text([self.screen_width / 2, 20], "name")
        self.planet_station_gui.create_text([self.screen_width / 2, 100], "fahrzeuge", display_not="[]")

        self.planet_station_gui.create_button([self.screen_width / 2, self.screen_height - 100], "Map", self.change_to_space_view)
        self.planet_station_gui.create_button([100, self.screen_height - 100], "actions" , self.planet_station_actions_gui.render)

        # planet actions
        #self.planet_station_actions_gui = GUI(self.screen)
        self.planet_station_actions_gui.create_button([100, self.screen_height - 100], "zurück", self.planet_station_gui.render)

        self.planet_station_actions_gui.create_list_of_elements((300, 300), "aktivitäten", get_pressed=self.station_do_activities)
        self.planet_station_actions_gui.create_list_of_elements((300, 100), "humans")

    def planet_station(self):
        #print(self.current_planet.name)

        self.gui.update()

    def space_overview(self):
        time = (pygame.time.get_ticks() + self.starttime) / self.speed

        self.screen.fill("black")

        
        pygame.draw.circle(self.screen, "white", (self.screen_width / 2, self.screen_height / 2), 20 / self.map_scale)

        for rakete in self.all_rockets:
            pygame.draw.circle(self.screen, "red", (self.screen_width / 2 + rakete.get_x(time) / self.map_scale, self.screen_height / 2 + rakete.get_y(time) / self.map_scale), 5 / self.map_scale)

            #if rakete.destination_planet.check_collision((rakete.get_x(time), rakete.get_y(time)), time, rakete.destination_planet.radius):
            #    rakete.destination_planet.station.fahrzeuge.append(rakete)
            #    self.all_rockets.remove(rakete)

            if rakete.get_landet(time):
                rakete.destination_planet.station.fahrzeuge.append(rakete)
                self.all_rockets.remove(rakete)

        for planet in self.all_planets:
            pygame.draw.circle(self.screen, "white", (self.screen_width / 2 + planet.get_x(time) / self.map_scale, self.screen_height / 2 + planet.get_y(time) / self.map_scale), planet.radius / self.map_scale)
            #pygame.draw.circle(self.screen, "white", (self.screen_width / 2 + planet.get_x(time) / self.map_scale, self.screen_height / 2 + planet.get_y(time) / self.map_scale), planet.radius / self.map_scale + 3, 1)
            #pygame.draw.circle(self.screen, )

            if  not pygame.mouse.get_pressed()[0]:
                continue

            x, y = pygame.mouse.get_pos()
            x = (x - self.screen_width / 2)
            y = (y - self.screen_height / 2)

            if planet.check_collision((x, y), time, planet.radius):
                print("collision")
                self.change_to_planet_view(planet)
                break

    def station_do_activities(self, index):
        self.current_planet.station.do_activities(index)

    def change_to_planet_view(self, planet):
        self.current_planet = planet
        self.current_mode = self.planet_station
        self.planet_station_gui.render()

    def change_to_space_view(self):
        self.current_mode = self.space_overview
        



    def test_to_mars(self):
        erde = self.get_planet("Erde")
        mars = self.get_planet("Mars")
        time = (pygame.time.get_ticks() + self.starttime) / self.speed

        erde.station.create_rocket()
        rakete = erde.station.fahrzeuge[0]

        print(mars.station.fahrzeuge)
        print(erde.station.fahrzeuge)
        print(erde.station.fahrzeuge)

        rakete.fly(erde, mars, time)
        self.all_rockets.append(rakete)

        print(erde.station.fahrzeuge)
        print(mars.station.fahrzeuge)

        print(mars.station.items)
        mars.station.sammle_steine()
        print(mars.station.items)

        #greift hier auf rakete zu diese ist aber noch gar nicht auf den mars
        #bitte später fixen
        mars.station.change_item(mars.station, rakete, "Steine", 1)

        print(mars.station.items)
        print(rakete.items)

        print(rakete.get_x(time))
        print(rakete.get_y(time))


        


game = Game()
game.run()


