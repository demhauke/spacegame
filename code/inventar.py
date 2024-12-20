from settings import item_rezepte

class Inventar:
    def __init__(self, items=False, tools=False):
        if items:
            self.items = items
        else:
            self.items = {
                "Steine": 0,
                "Kupfer": 0,
                "Gold": 0,
                "Eisen": 0
            }
        if tools:
            self.tools = tools
        else:
            self.tools = {
                "Spitzhacke": False
            }

    def check_if_able_to_craft(self, item_to_craft):
        for item in item_rezepte[item_to_craft]:
            if item[1] > self.items[item[0]]:
                return False
        
        return True


    def get_inventar(self):
        inventar = []
        for key in self.items.keys():
            inventar.append(f"{key}: {self.items[key]}")
        return inventar
    
    def get_inventar_amount(self):
        inventar = []
        for key in self.items.keys():
            inventar.append(str(self.items[key]))
        return inventar
    
    def change_item(self, old, new, item, amount):
        if old.items[item] - amount < 0:
            return

        old.items[item] -= amount
        new.items[item] += amount

    def append_items(self, item, amount):
        self.items[item] += amount