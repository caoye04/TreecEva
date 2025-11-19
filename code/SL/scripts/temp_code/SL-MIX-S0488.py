import math
from functools import reduce
from itertools import combinations

def calculate_triangle_area(p1, p2, p3):
    # Using the cross product formula for triangle area
    return abs((p1[0]*(p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1])) / 2.0)

def extract_numeric_prefix(s):
    # Extract numeric prefix from string
    num_str = ''.join(filter(str.isdigit, s))
    return int(num_str) if num_str else 0

# Simulated sensor data with coordinates and metadata tags
sensor_readings = [
    ((2, 3), "Zone41-North"),
    ((5, 7), "Zone22-East"),
    ((8, 1), "Zone33-South"),
    ((1, 9), "Zone14-West"),
    ((6, 4), "Zone55-Central")
]

# Step 1: Filter out sensors with zone numbers less than 20
filtered_sensors = [(coord, tag) for coord, tag in sensor_readings if extract_numeric_prefix(tag) >= 20]

# Step 2: Generate all possible triangular combinations of sensor coordinates
triangular_combinations = list(combinations([coord for coord, _ in filtered_sensors], 3))

# Step 3: Calculate total coverage area as sum of all triangle areas
coverage_areas = [calculate_triangle_area(*combo) for combo in triangular_combinations]
total_geometric_coverage = sum(coverage_areas)

# Step 4: Process textual metadata to derive quality scores
zone_numbers = [extract_numeric_prefix(tag) for _, tag in filtered_sensors]
quality_scores = list(map(lambda x: math.log(x) if x > 0 else 0, zone_numbers))

# Step 5: Combine geometric coverage with metadata quality using weighted average
weighted_quality = reduce(lambda acc, val: acc + val*0.3, quality_scores, 0)
combined_metric = total_geometric_coverage * 0.7 + weighted_quality

# Step 6: Apply normalization factor based on number of valid sensors
normalization_factor = len(filtered_sensors) / len(sensor_readings)
optimal_coverage_score = combined_metric * normalization_factor

# Step 7: Round to nearest integer for final discrete score
optimal_coverage_score = round(optimal_coverage_score)

print(f"Result: {optimal_coverage_score}")