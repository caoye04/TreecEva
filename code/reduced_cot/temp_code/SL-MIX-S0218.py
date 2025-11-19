import re
from functools import reduce
from collections import defaultdict

def haversine_distance(p1, p2):
    # Simplified distance calculation returning integer meters
    return int(abs(p1[0] - p2[0]) * 100000 + abs(p1[1] - p2[1]) * 100000)

def extract_coordinates(log_line):
    match = re.search(r'\(([-+]?\d*\.\d+),\s*([-+]?\d*\.\d+)\)', log_line)
    if match:
        return (float(match.group(1)), float(match.group(2)))
    return None

tracking_logs = [
    "Device_001: (34.0522, -118.2437)",
    "Device_001: (34.0530, -118.2440)",
    "Device_001: (34.0545, -118.2455)",
    "Device_001: (34.0560, -118.2470)",
    "Device_001: (34.0575, -118.2485)"
]

coordinates_list = list(filter(None, map(extract_coordinates, tracking_logs)))
dp_min_deviation = defaultdict(lambda: float('inf'))
dp_min_deviation[0] = 0

for i in range(1, len(coordinates_list)):
    for j in range(i):
        segment_distance = haversine_distance(coordinates_list[j], coordinates_list[i])
        dp_min_deviation[i] = min(dp_min_deviation[i], dp_min_deviation[j] + segment_distance)

straight_line_distance = haversine_distance(coordinates_list[0], coordinates_list[-1])
migration_efficiency_index = dp_min_deviation[len(coordinates_list)-1] - straight_line_distance

print(f"Result: {migration_efficiency_index}")