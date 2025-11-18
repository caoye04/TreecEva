import math
from collections import namedtuple

# Define a Light with position (x,y) and intensity
Light = namedtuple('Light', ['x', 'y', 'intensity'])

# Active lights in the installation
active_lights = frozenset([
    Light(3, 4, 2),
    Light(-2, 5, 3),
    Light(1, -1, 1),
    Light(-4, -3, 4),
    Light(0, 2, 2)
])

# Define a square region for analysis: from (-3,-3) to (4,5)
x_min, x_max = -3, 4
y_min, y_max = -3, 5

# Function to calculate distance from origin
def distance_from_origin(light):
    return math.sqrt(light.x**2 + light.y**2)

# Function to check if a light is within the defined region
def is_within_region(light):
    return x_min <= light.x <= x_max and y_min <= light.y <= y_max

# Calculate total luminosity for lights in the region
region_luminosity = 0
for luminaire in active_lights:
    if is_within_region(luminaire):
        luminosity_component = distance_from_origin(luminaire) * luminaire.intensity
        region_luminosity += luminosity_component

print(f"Result: {round(region_luminosity)}")