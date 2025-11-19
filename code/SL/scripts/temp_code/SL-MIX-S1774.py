import math

# Radii of circular flower beds in meters
flower_bed_radii = [3, 5, 2, 7, 4]

# Calculate areas using list comprehension and geometry formula (π * r²)
flower_bed_areas = [math.pi * radius ** 2 for radius in flower_bed_radii]

total_garden_area = sum(flower_bed_areas)

print(f"Result: {total_garden_area}")