import math
from functools import reduce

def circle_area(radius):
    return math.pi * radius ** 2

park_radii = [10, 15, 20, 12]
park_areas = list(map(circle_area, park_radii))
total_green_space = reduce(lambda x, y: x + y, park_areas)

print(f'Result: {round(total_green_space)}')