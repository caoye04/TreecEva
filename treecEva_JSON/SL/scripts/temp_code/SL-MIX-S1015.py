import math

# Flower bed radii in meters
flower_beds = {
    'roses': 3,
    'tulips': 2,
    'daisies': 4,
    'sunflowers': 5
}

# Calculate area for each flower type using dict comprehension
bed_areas = {flower: math.pi * radius**2 for flower, radius in flower_beds.items()}

# Sum all areas to get total park area
total_park_area = sum(bed_areas.values())

print(f"Result: {total_park_area}")