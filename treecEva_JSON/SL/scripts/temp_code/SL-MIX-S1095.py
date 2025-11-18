import heapq
from functools import reduce
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

elevation_map = [
    [15, 23, 18, 42, 35],
    [28, 33, 29, 38, 45],
    [22, 31, 30, 40, 39],
    [25, 27, 32, 37, 41],
    [19, 24, 26, 36, 34]
]

rows, cols = len(elevation_map), len(elevation_map[0])
peak_candidates = []

for r in range(rows):
    for c in range(cols):
        current = elevation_map[r][c]
        is_peak = True
        neighbors = []
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                neighbor = elevation_map[nr][nc]
                neighbors.append(neighbor)
                if neighbor >= current:
                    is_peak = False
        if is_peak and neighbors:
            heapq.heappush(peak_candidates, (-current, r, c))

prominent_peaks_count = 0
processed_heights = set()

while peak_candidates:
    neg_height, r, c = heapq.heappop(peak_candidates)
    height = -neg_height
    
    adjacent_heights = []
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            adjacent_heights.append(elevation_map[nr][nc])
    
    base_elevation = min(adjacent_heights) if adjacent_heights else 0
    prominence = height - base_elevation
    
    is_prime_prominence = prominence > 1 and all(prominence % i != 0 for i in range(2, int(prominence**0.5)+1))
    
    gcd_with_row_col = gcd(r+1, c+1)
    
    meets_criteria = is_prime_prominence and gcd_with_row_col == 1
    
    prominent_peaks_count += 1 if meets_criteria else 0
    processed_heights.add(height)

print(f"Result: {prominent_peaks_count}")