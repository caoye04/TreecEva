import math
from functools import reduce

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def fibonacci_sequence(n):
    if n <= 0: return []
    elif n == 1: return [0]
    elif n == 2: return [0, 1]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

elevation_readings = [1200, 1250, 1230, 1275, 1300, 1280, 1320, 1350, 1330, 1380]
sensor_coordinates = [(0,0), (1,2), (3,1), (2,4), (5,3), (4,6), (6,5), (8,7), (7,9), (9,8)]
visited_coords = {}
current_path = None
path_tail = None

for i, coord in enumerate(sensor_coordinates):
    visited_coords[coord] = elevation_readings[i]
    new_node = ListNode(elevation_readings[i])
    if current_path is None:
        current_path = new_node
        path_tail = new_node
    else:
        path_tail.next = new_node
        path_tail = new_node

unique_elevations = list(set(elevation_readings))
unique_elevations.sort()

metadata_tags = {f'sensor_{i}': {'coord': c, 'elevation': e} 
                 for i, (c, e) in enumerate(zip(sensor_coordinates, elevation_readings))}

fib_weights = fibonacci_sequence(len(unique_elevations))
weighted_sum = sum(e * w for e, w in zip(unique_elevations, fib_weights))
total_weight = sum(fib_weights)
avg_elevation = weighted_sum / total_weight if total_weight != 0 else 0

path_distances = []
for i in range(len(sensor_coordinates)-1):
    dist = euclidean_distance(sensor_coordinates[i], sensor_coordinates[i+1])
    path_distances.append(dist)

greedy_selection = []
current_index = 0
while current_index < len(elevation_readings):
    candidates = [(i, abs(elevation_readings[i] - avg_elevation)) 
                  for i in range(current_index, min(current_index+3, len(elevation_readings)))]
    best_candidate = min(candidates, key=lambda x: x[1])
    greedy_selection.append(best_candidate[0])
    current_index = best_candidate[0] + 1

selected_elevations = [elevation_readings[i] for i in greedy_selection]
fib_filter = fibonacci_sequence(len(selected_elevations))
smoothed_values = []
for i in range(len(selected_elevations)):
    window_start = max(0, i - 1)
    window_end = min(len(selected_elevations), i + 2)
    window_vals = selected_elevations[window_start:window_end]
    window_weights = fib_filter[window_start:window_end]
    if sum(window_weights) > 0:
        smoothed_val = sum(v * w for v, w in zip(window_vals, window_weights)) / sum(window_weights)
    else:
        smoothed_val = selected_elevations[i]
    smoothed_values.append(smoothed_val)

smoothed_altitude = round(sum(smoothed_values) / len(smoothed_values))
print(f'Result: {smoothed_altitude}')