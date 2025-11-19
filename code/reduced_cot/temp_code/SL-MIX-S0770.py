from collections import defaultdict
import math

def tokenize_lots(lot_string):
    return [tuple(map(int, lot.split('x'))) for lot in lot_string.split(',')]

def calculate_max_footprint(width, depth, zoning_modifier):
    base_area = width * depth
    if zoning_modifier > 0.8:
        return base_area * 0.75
    elif zoning_modifier > 0.6:
        return base_area * 0.85
    else:
        return base_area * 0.95

zoning_rules = defaultdict(lambda: 0.7, {
    'residential': 0.9,
    'commercial': 0.75,
    'industrial': 0.85
})

lot_data = "20x30,residential;15x25,commercial;30x40,industrial;25x35,residential"
max_constructible_area = 0

for entry in lot_data.split(';'):
    dimensions, zone_type = entry.split(',')
    width, depth = map(int, dimensions.split('x'))
    modifier = zoning_rules[zone_type]
    area = calculate_max_footprint(width, depth, modifier)
    max_constructible_area = max(max_constructible_area, area)
    
# Apply final city planning constraint
if max_constructible_area > 1000:
    max_constructible_area = int(max_constructible_area * 0.9)
else:
    max_constructible_area = int(max_constructible_area * 0.95)
    
print(f"Result: {max_constructible_area}")