import heapq
from collections import namedtuple
from dataclasses import dataclass
from typing import List, Tuple

elevation_matrix = [
    [120, 125, 130, 128],
    [118, 122, 135, 133],
    [115, 119, 140, 138],
    [117, 121, 137, 136]
]

@dataclass
class SurveyPoint:
    row: int
    col: int
    elevation: int

Point = namedtuple('Point', ['x', 'y'])

significant_changes_heap = []
visited_points = set()
anomaly_accumulator = 0

for r in range(len(elevation_matrix)):
    for c in range(len(elevation_matrix[0])):
        current_elevation = elevation_matrix[r][c]
        if r > 0 and abs(current_elevation - elevation_matrix[r-1][c]) > 10:
            heapq.heappush(significant_changes_heap, (-abs(current_elevation - elevation_matrix[r-1][c]), SurveyPoint(r, c, current_elevation)))
        if c > 0 and abs(current_elevation - elevation_matrix[r][c-1]) > 10:
            heapq.heappush(significant_changes_heap, (-abs(current_elevation - elevation_matrix[r][c-1]), SurveyPoint(r, c, current_elevation)))

peak_anomaly_score = 0
processed_count = 0
while significant_changes_heap and processed_count < 3:
    neg_diff, point_data = heapq.heappop(significant_changes_heap)
    coord = Point(point_data.row, point_data.col)
    if coord in visited_points:
        continue
    visited_points.add(coord)
    
    # Calculate neighboring average using divide and conquer approach for submatrix
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            nr, nc = point_data.row + dr, point_data.col + dc
            if 0 <= nr < len(elevation_matrix) and 0 <= nc < len(elevation_matrix[0]):
                neighbors.append(elevation_matrix[nr][nc])
    
    if len(neighbors) >= 4:
        neighbors.sort()
        mid = len(neighbors) // 2
        if len(neighbors) % 2 == 0:
            median_elevation = (neighbors[mid-1] + neighbors[mid]) / 2
        else:
            median_elevation = neighbors[mid]
        
        anomaly_delta = abs(point_data.elevation - median_elevation)
        peak_anomaly_score += int(anomaly_delta * 10)
        processed_count += 1

print(f"Result: {peak_anomaly_score}")