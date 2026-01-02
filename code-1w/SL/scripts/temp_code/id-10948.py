from itertools import combinations

def compute_set_overlap():
    # Sensor coverage areas represented as sets of grid cells
    sensor_a = {1, 2, 3, 4, 5, 6}
    sensor_b = {4, 5, 6, 7, 8, 9}
    sensor_c = {6, 7, 8, 10, 11}
    sensor_d = {10, 11, 12}

    # List of all sensors for pairwise analysis
    sensors = [sensor_a, sensor_b, sensor_c, sensor_d]
    overlaps = []

    # Compute pairwise intersections between sensor coverages
    for pair in combinations(sensors, 2):
        intersection = len(pair[0] & pair[1])
        overlaps.append(intersection)

    total_overlap = sum(overlaps)
    
    # Irrelevant metric (minimal distraction)
    max_single_coverage = max(len(s) for s in sensors)
    
    return total_overlap

result = compute_set_overlap()
print(f"Result: {result}")