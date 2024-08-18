from rakete import Rakete

class Station():
    def __init__(self, name):
        self.items = {
            "Steine": 0
        }
        self.name = name
        self.humans = [0, 1, 22]
        self.buildings = []
        self.fahrzeuge = []
        self.raketen = []

        self.aktivitäten = ["sammle_steine", "create_rocket"]

    def do_activities(self, index):
        print(index + 10)
        getattr(self, self.aktivitäten[index])()

    def get_fahrzeug_names(self):
        return 

    def create_rocket(self):
        self.fahrzeuge.append(Rakete())

    def sammle_steine(self):
        self.items["Steine"] += 1
        print(f"Steine: {self.items['Steine']}")

    def change_item(self, old, new, item, amount):
        old.items[item] -= amount
        new.items[item] += amount

    def get_activitys(self):
        return ["sammle_steine", "create_rocket"]

    def print_info(self, name):
        for i in (self.humans, self.buildings, self.fahrzeuge):
            if i != []:
                print(f"{name}: {i}")