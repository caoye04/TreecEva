import math

# Define radius of flower bed and path width
flower_bed_radius = 3
path_width = 1.5

# Calculate outer radius including the path
outer_radius = flower_bed_radius + path_width

# Using list comprehension to calculate areas
areas = [math.pi * r**2 for r in [flower_bed_radius, outer_radius]]

# Calculate total area (area of outer circle)
total_area = areas[1]

print(f"Result: {total_area}")