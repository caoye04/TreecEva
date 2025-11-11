import math

# Define radii for the flower beds
radius_first_bed = 5
radius_second_bed = 3
radius_third_bed = 4

# The second bed is placed at the edge of the first
# So the distance between their centers is the sum of their radii
distance_first_to_second = radius_first_bed + radius_second_bed

# To ensure the third bed doesn't overlap with the first,
# the distance must be at least the sum of their radii
min_safe_distance = distance_first_to_second + radius_third_bed

print(f"Result: {min_safe_distance}")