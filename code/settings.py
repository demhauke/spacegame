
#planet_map = [
#    [1, 1, 1],
##    [1, 2, 1],
#    [1, 1, 1]
#]

import random

# Map-Größe definieren
tiles_x = 200  # Anzahl der Kacheln in der Breite
tiles_y = 100   # Anzahl der Kacheln in der Höhe

# Zufällige planet_map erstellen

def create_planet_map():
    # Gewichtete Wahrscheinlichkeiten für die Zufallswahl von Feldern
    choices = [
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,  # Sehr häufig
        2, 2, 4, 4,  # Mittel häufig
        5, 6  # Selten
    ]

    # Karte erstellen
    planet_map = [[random.choice(choices) for _ in range(tiles_x)] for _ in range(tiles_y)]

    # Ein Feld mit Wert 3 (nur einmal)
    planet_map[random.randint(0, tiles_y - 1)][random.randint(0, tiles_x - 1)] = 3

    return planet_map

def create_planet_map():
    # Karte initialisieren
    planet_map = [[1 for _ in range(tiles_x)] for _ in range(tiles_y)]

    # Seltene Items in kleinere Cluster platzieren
    rare_items = [6, 7, 8]
    map_area = tiles_x * tiles_y
    cluster_density = 0.005  # Anteil der Cluster zur Gesamtfläche (z. B. 0,5% der Felder starten Cluster)
    num_clusters = int(map_area * cluster_density)
    cluster_size = 8   # Maximale Anzahl der Felder pro Cluster

    for _ in range(num_clusters):
        rare_item = random.choice(rare_items)
        start_x = random.randint(0, tiles_x - 1)
        start_y = random.randint(0, tiles_y - 1)

        # Flood-Fill-Algorithmus
        queue = [(start_x, start_y)]
        visited = set()
        cluster_count = 0

        while queue and cluster_count < cluster_size:
            x, y = queue.pop(0)
            if (x, y) in visited or not (0 <= x < tiles_x and 0 <= y < tiles_y):
                continue

            visited.add((x, y))
            planet_map[y][x] = rare_item
            cluster_count += 1

            # Nachbarn zufällig hinzufügen
            neighbors = [
                (x + 1, y), (x - 1, y),
                (x, y + 1), (x, y - 1)
            ]
            random.shuffle(neighbors)
            queue.extend(neighbors)

    # Zufällige Platzierung von 2 und 4
    common_items = [2, 4, 5]
    num_common_items = int(map_area * 0.1)  # 10% der Karte mit 2 und 4

    for _ in range(num_common_items):
        x = random.randint(0, tiles_x - 1)
        y = random.randint(0, tiles_y - 1)
        planet_map[y][x] = random.choice(common_items)

    # Ein Feld mit Wert 3 (nur einmal)
    planet_map[random.randint(0, tiles_y - 1)][random.randint(0, tiles_x - 1)] = 3

    return planet_map


    

planet_map = [[random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 4]) for _ in range(tiles_x)] for _ in range(tiles_y)]

planet_map[random.randint(0, tiles_y - 1)][random.randint(0, tiles_x - 1)] = 3

TILESIZE = 64


item_to_path = {
    "Steine": "spacegame/graphics/Steine.png",
    "Steine sampling": "spacegame/graphics/Steine sampling.png",
    "Rocket": "spacegame/graphics/Rocket.png",
    "Rover": "spacegame/graphics/Rover.png",
    "Kupfer": "spacegame/graphics/Kupfer.png",
    "Kupfer sampling": "spacegame/graphics/Kupfer sampling.png",
    "Gold": "spacegame/graphics/Steine.png",
    "Eisen": "spacegame/graphics/Steine.png",
    "Kohle": "spacegame/graphics/Kohle.png",
    "Kohle sampling": "spacegame/graphics/Kohle sampling.png"
}


item_rezepte = {
    "Spitzhacke": [["Kupfer", 10]]
}


planeten = {
    "Merkur": {'a': 57.91, 'T': 0.24, 'e': 0.2056, 'radius': 0.03504, 'buildings': [], 'map': create_planet_map()},
    "Venus": {'a': 108.2, 'T': 0.62, 'e': 0.0067, 'radius': 0.08690, 'buildings': [], 'map': create_planet_map()},
    "Erde": {'a': 149.6, 'T': 1.0, 'e': 0.0167, 'radius': 0.09152, 'buildings': ["raketen bauen"], 'map': create_planet_map()},
    "Mars": {'a': 227.9, 'T': 1.88, 'e': 0.0934, 'radius': 0.04868, 'buildings': [], 'map': create_planet_map()},
    "Jupiter": {'a': 778.5, 'T': 11.86, 'e': 0.0484, 'radius': 1.00488, 'buildings': [], 'map': create_planet_map()},
    "Saturn": {'a': 1434, 'T': 29.46, 'e': 0.0542, 'radius': 0.83643, 'buildings': [], 'map': create_planet_map()},
    "Uranus": {'a': 2871, 'T': 84.01, 'e': 0.0472, 'radius': 0.36425, 'buildings': [], 'map': create_planet_map()},
    "Neptun": {'a': 4495, 'T': 164.79, 'e': 0.0086, 'radius': 0.35364, 'buildings': [], 'map': create_planet_map()}
}

backgroundcolor_per_planet = {
    "Merkur": (176, 176, 176),  # Graubraun
    "Venus": (229, 192, 123),   # Gelblich-beige
    "Erde": (34, 139, 34),      # Natürliches Grün (Wälder, Natur)
    "Mars": (211, 84, 0),       # Rötlich-orange
    "Jupiter": (212, 160, 23),  # Gelblich-braun
    "Saturn": (245, 208, 132),  # Hellbeige-gelb
    "Uranus": (136, 192, 208),  # Hellblau
    "Neptun": (30, 59, 161)     # Dunkelblau
}


