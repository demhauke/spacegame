from rakete import Rakete
from inventar import Inventar
import pygame

class Station(Inventar):
    def __init__(self, name, buildings):
        super().__init__()

        self.activity_name_to_method = {
            "Steine Sammeln": self.sammle_steine

        }

        self.name = name
        self.druids = []
        self.buildings = buildings
        self.fahrzeuge = []
        self.raketen = []
        self.raketen_anzeige = [5,4, 3]

        self.selected_human_index = 0
        self.selected_aktivität_index: int
        self.selected_raketen_index = 0

        self.update()

        #self.selected_raketen_inventar = []

        self.time0 = pygame.time.get_ticks()

        self.create_rocket()

        if name == "Erde":
            self.druids.append(Inventar())

    def do_activity(self):
        try:
            if self.humans[self.selected_human_index] <= 0:

                #self.humans[self.selected_human_index] += 10

                print(self.selected_aktivität_index + 10)
                self.activity_name_to_method[self.aktivitäten[self.selected_aktivität_index]]()
                #getattr(self, self.aktivitäten[self.selected_aktivität_index])()
        except:
            pass
    
        self.update()

    def select_activity(self, index):
        self.selected_aktivität_index = index

    def select_human(self, index):
        self.selected_human_index = index

    def select_rakete(self, index):
        self.selected_raketen_index = index

    def get_fahrzeug_names(self):
        return 

    def create_rocket(self):
        self.raketen.append(Rakete())

    def sammle_steine(self):
        self.items["Steine"] += 1
        print(f"Steine: {self.items['Steine']}")

    def change_item(self, old, new, item, amount):
        if old.items[item] - amount < 0:
            return

        old.items[item] -= amount
        new.items[item] += amount


    def change_item_at_station(self, index, old, new):
        for index_key, value in enumerate(self.items.keys()):
            if index_key == index:
                item = value
        self.change_item(old, new, item, 1)

    def get_selected_raketen_inventar(self):
        try:
            return self.raketen[self.selected_raketen_index].get_inventar()
        except:
            return []

    def get_activitys(self):
        aktivitäten = ["Steine Sammeln"]
        if "raketen bauen" in self.buildings:
            aktivitäten.append("create_rocket")
        if len(self.druids) >= 1 and len(self.raketen) >= 1:
            aktivitäten.append("fliegen")
        return aktivitäten
    
    def get_raketen(self):
        raketen = []
        for rakete in self.raketen:
            raketen.append("Rakete")

        return raketen

    def print_info(self, name):
        for i in (self.humans, self.buildings, self.fahrzeuge):
            if i != []:
                print(f"{name}: {i}")

    def time_update(self):
        delta_time = (pygame.time.get_ticks() - self.time0) / 1000

        print(pygame.time.get_ticks())
        print(delta_time)

        for index, human in enumerate(self.humans):
            if human <= 0:
                self.humans[index] = 0
                continue
            self.humans[index] -= delta_time

        self.time0 = pygame.time.get_ticks()

    def update(self):
        
        self.aktivitäten = self.get_activitys()
        self.raketen_liste = self.get_raketen()
        self.inventar_ = self.get_inventar()
        self.selected_raketen_inventar = self.get_selected_raketen_inventar()
        #self.time_update()

