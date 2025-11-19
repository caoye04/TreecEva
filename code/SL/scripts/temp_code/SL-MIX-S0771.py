import math
from itertools import combinations
import heapq

def gcd_lcm_harmony(matrix):
    # Step 1: Apply lambda to filter out non-positive values
    filter_positive = lambda row: [x for x in row if x > 0]
    filtered_matrix = [filter_positive(row) for row in matrix]
    
    # Step 2: Flatten and get unique values
    flat_values = list(set([item for sublist in filtered_matrix for item in sublist]))
    
    # Step 3: Use heap to find the smallest 4 values
    heapq.heapify(flat_values)
    smallest_four = [heapq.heappop(flat_values) for _ in range(min(4, len(flat_values)))]
    
    # Step 4: Compute pairwise GCDs
    gcd_pairs = [math.gcd(a, b) for a, b in combinations(smallest_four, 2)]
    
    # Step 5: Compute LCM of all pairwise GCDs
    lcm_result = gcd_pairs[0]
    for val in gcd_pairs[1:]:
        lcm_result = (lcm_result * val) // math.gcd(lcm_result, val)
    
    return lcm_result

# Sensor data matrix
sensor_readings = [
    [12, -5, 18, 0, 24],
    [6, 15, 9, -3],
    [30, 10, 5, 20],
    [-1, 0, 45, 3]
]

# Calculate the array harmony metric
harmonic_score = gcd_lcm_harmony(sensor_readings)
print(f"Result: {harmonic_score}")