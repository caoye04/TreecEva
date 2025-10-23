import re
from math import pi

class ParkFeature:
    def __init__(self, location_str):
        self.location_str = location_str

# Extract coordinates using regex
feature = ParkFeature('15,20')
coords_match = re.match(r'(\d+),(\d+)', feature.location_str)
x, y = map(int, coords_match.groups())

# Calculate area using lambda
area_calculator = lambda radius: pi * radius ** 2
fountain_area = area_calculator(7)

print(f'Result: {round(fountain_area)}')