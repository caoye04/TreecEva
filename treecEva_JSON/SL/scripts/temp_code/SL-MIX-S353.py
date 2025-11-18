import re
from functools import reduce
from math import sqrt

def calculate_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_valid_coordinate(coord_str):
    pattern = r'^\(?(-?\d+\.\d+),\s*(-?\d+\.\d+)\)?$'
    return re.match(pattern, coord_str)

# Sensor data with mixed valid/invalid formats
sensor_readings = [
    "(3.5, 7.2)", "(1.2, 9.8", "(5.5, 2.1)", 
    "10.3, 4.7)", "(8.9, 6.4)", "(2.1, 3.3)",
    "invalid_data", "(7.7, 1.9)", "(4.4, 8.8)"
]

# Extract valid coordinates using pattern matching and functional programming
valid_coords = list(filter(is_valid_coordinate, sensor_readings))
extracted_points = [tuple(map(float, re.findall(r'-?\d+\.\d+', coord))) for coord in valid_coords]

# Define survey zones as circular areas around base points
base_stations = [(2.0, 3.0), (6.0, 7.0), (9.0, 2.0)]
radius_threshold = 5.0

# Calculate which points fall within each zone
zone_memberships = []
for station in base_stations:
    members = [point for point in extracted_points if calculate_distance(station, point) <= radius_threshold]
    zone_memberships.append(frozenset(members))

# Find intersection of all zones using set operations
common_survey_points = reduce(lambda x, y: x.intersection(y), zone_memberships)

# Apply geometric scoring: sum of distances from all base stations for each common point
survey_scores = []
for point in common_survey_points:
    total_distance = sum(calculate_distance(point, station) for station in base_stations)
    survey_scores.append(total_distance)

# Count zones with above-average scoring points
average_score = sum(survey_scores) / len(survey_scores) if survey_scores else 0
high_value_zones = [score for score in survey_scores if score > average_score]

# Final calculation using list comprehension
optimal_zone_count = len([z for z in zone_memberships if len(z) > len(high_value_zones)])

print(f"Result: {optimal_zone_count}")