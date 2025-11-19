import math
from itertools import combinations
from collections import defaultdict

def process_sensor_grid(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Step 1: Compute row-wise XOR signatures
    row_signatures = []
    for r in range(rows):
        sig = 0
        for c in range(cols):
            sig ^= grid[r][c]
        row_signatures.append(sig)
    
    # Step 2: Select unique pairs of row signatures and compute their bitwise AND
    pair_ands = [a & b for a, b in combinations(row_signatures, 2)]
    
    # Step 3: Apply logarithmic scaling to each AND result
    scaled_values = [math.log2(x + 1) if x > 0 else 0 for x in pair_ands]
    
    # Step 4: Aggregate scaled values using a frequency-weighted sum
    freq_map = defaultdict(int)
    for val in scaled_values:
        freq_map[val] += 1
    
    aggregated_signal = sum(value * freq for value, freq in freq_map.items())
    
    return aggregated_signal

# Sensor grid data (5x4 matrix)
sensor_readings = [
    [12, 7, 25, 8],
    [3, 19, 14, 6],
    [9, 2, 11, 20],
    [15, 4, 18, 1],
    [16, 13, 5, 22]
]

aggregated_signal = process_sensor_grid(sensor_readings)
print(f"Result: {aggregated_signal}")