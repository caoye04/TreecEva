import re
import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

survey_readings = [
    "POINT(32.5;-118.2;247.9)",
    "POINT(33.1;-118.0;251.3)",
    "POINT(32.8;-118.5;249.7)",
    "POINT(33.0;-118.3;250.1)",
    "POINT(32.9;-118.4;248.8)"
]

parsed_points = []
for reading in survey_readings:
    match = re.search(r"POINT\(([^;]+);([^;]+);([^)]+)\)", reading)
    if match:
        lat, lon, elev = map(float, match.groups())
        parsed_points.append((lat, lon, elev))

stability_factors = []
base_elevation = parsed_points[0][2]
for i in range(1, len(parsed_points)):
    delta_elev = abs(parsed_points[i][2] - base_elevation)
    distance = math.sqrt((parsed_points[i][0] - parsed_points[0][0])**2 + 
                         (parsed_points[i][1] - parsed_points[0][1])**2)
    factor = int(delta_elev * 1000 + distance * 100)
    stability_factors.append(factor)

common_divisor = gcd_list(stability_factors)
terrain_stability_index = sum(x // common_divisor for x in stability_factors) % 1000
print(f"Result: {terrain_stability_index}")