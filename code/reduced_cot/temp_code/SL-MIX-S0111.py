import math
from collections import defaultdict
from itertools import combinations

def encode_base36(num):
    if num == 0:
        return '0'
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while num:
        num, remainder = divmod(num, 36)
        result = chars[remainder] + result
    return result

def decode_base36(s):
    return int(s, 36)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Encoded waypoints representing x,y coordinates in base36
encoded_waypoints = ['1F4', 'A0', '2K', 'ZO', '1S2', '9A']

# Decode waypoints
waypoints = []
for code in encoded_waypoints:
    x_encoded = code[:len(code)//2] if len(code) > 1 else code
    y_encoded = code[len(code)//2:] if len(code) > 1 else '0'
    x = decode_base36(x_encoded)
    y = decode_base36(y_encoded)
    waypoints.append((x, y))

# Calculate distances between consecutive points
distances = []
for i in range(len(waypoints) - 1):
    d = euclidean_distance(waypoints[i], waypoints[i+1])
    distances.append(round(d, 2))

# Sort distances
sorted_distances = sorted(distances)

# Find all combinations of 3 points
point_combinations = list(combinations(waypoints, 3))

# Check for triangular patterns (non-zero area triangles)
triangular_patterns_count = 0
for p1, p2, p3 in point_combinations:
    # Using cross product to check if three points form a triangle (non-collinear)
    cross_product = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    if abs(cross_product) > 1e-9:  # Non-zero area indicates triangle
        triangular_patterns_count += 1

print(f"Result: {triangular_patterns_count}")