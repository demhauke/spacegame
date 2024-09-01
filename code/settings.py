
#planet_map = [
#    [1, 1, 1],
##    [1, 2, 1],
#    [1, 1, 1]
#]

import random

# Map-Größe definieren
tiles_x = 25  # Anzahl der Kacheln in der Breite
tiles_y = 9   # Anzahl der Kacheln in der Höhe

# Zufällige planet_map erstellen
planet_map = [[random.choice([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]) for _ in range(tiles_x)] for _ in range(tiles_y)]

planet_map[random.randint(0, tiles_y - 1)][random.randint(0, tiles_x - 1)] = 3

TILESIZE = 64


planeten = {
    "Merkur": {'a': 57.91, 'T': 0.24, 'e': 0.2056, 'radius': 0.03504, 'buildings': []},
    "Venus": {'a': 108.2, 'T': 0.62, 'e': 0.0067, 'radius': 0.08690, 'buildings': []},
    "Erde": {'a': 149.6, 'T': 1.0, 'e': 0.0167, 'radius': 0.09152, 'buildings': ["raketen bauen"]},
    "Mars": {'a': 227.9, 'T': 1.88, 'e': 0.0934, 'radius': 0.04868, 'buildings': []},
    "Jupiter": {'a': 778.5, 'T': 11.86, 'e': 0.0484, 'radius': 1.00488, 'buildings': []},
    "Saturn": {'a': 1434, 'T': 29.46, 'e': 0.0542, 'radius': 0.83643, 'buildings': []},
    "Uranus": {'a': 2871, 'T': 84.01, 'e': 0.0472, 'radius': 0.36425, 'buildings': []},
    "Neptun": {'a': 4495, 'T': 164.79, 'e': 0.0086, 'radius': 0.35364, 'buildings': []}
}


