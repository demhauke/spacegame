

class Inventar:
    def __init__(self):
        self.items = {
            "Steine": 0,
            "Gold": 0,
            "Eisen": 0
        }

    def get_inventar(self):
        inventar = []
        for key in self.items.keys():
            inventar.append(f"{key}: {self.items[key]}")
        return inventar
    
    def change_item(self, old, new, item, amount):
        if old.items[item] - amount < 0:
            return

        old.items[item] -= amount
        new.items[item] += amount

    def append_items(self, item, amount):
        self.items[item] += amount