from math import sqrt
from itertools import combinations
class WaypointNode:
    def __init__(self, x, y, elevation):
        self.x = x
        self.y = y
        self.elevation = elevation
        self.next = None

def calculate_distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def path_efficiency(start, end, elevations):
    dx = end.x - start.x
    dy = end.y - start.y
    distance = calculate_distance(start, end)
    elevation_change = abs(elevations[end.y][end.x] - elevations[start.y][start.x])
    return distance / (1 + elevation_change)

elevation_grid = [
    [100, 102, 105, 103],
    [101, 104, 106, 108],
    [103, 105, 107, 109],
    [104, 106, 108, 110]
]

checkpoints = [
    WaypointNode(0, 0, elevation_grid[0][0]),
    WaypointNode(3, 0, elevation_grid[0][3]),
    WaypointNode(0, 3, elevation_grid[3][0]),
    WaypointNode(3, 3, elevation_grid[3][3])
]

visited_path = WaypointNode(checkpoints[0].x, checkpoints[0].y, checkpoints[0].elevation)
current_node = visited_path
for i in range(1, len(checkpoints)):
    current_node.next = WaypointNode(checkpoints[i].x, checkpoints[i].y, checkpoints[i].elevation)
    current_node = current_node.next

total_efficiency = 0
path_segments = list(combinations(checkpoints, 2))

for segment in path_segments:
    efficiency = path_efficiency(segment[0], segment[1], elevation_grid)
    match (segment[0].x, segment[0].y, segment[1].x, segment[1].y):
        case (0, 0, 3, 0):
            if efficiency > 1.5:
                total_efficiency += efficiency * 1.3
            else:
                total_efficiency += efficiency
        case (0, 0, 0, 3):
            total_efficiency += efficiency * 0.9
        case (0, 0, 3, 3):
            total_efficiency += efficiency * 1.1
        case (3, 0, 0, 3):
            total_efficiency += efficiency * 1.2
            break
        case (3, 0, 3, 3):
            total_efficiency += efficiency
        case (0, 3, 3, 3):
            total_efficiency += efficiency * 0.95
        case _:
            total_efficiency += efficiency

optimized_survey_score = round(total_efficiency * 100)
print(f"Result: {optimized_survey_score}")