import math
import statistics
from contextlib import contextmanager

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

@contextmanager
def depth_measurement_context(sensor_data):
    try:
        yield sensor_data
    finally:
        pass

def is_point_in_triangle(point, triangle):
    # Barycentric technique
    A, B, C = triangle
    Ax, Ay = A
    Bx, By = B
    Cx, Cy = C
    Px, Py = point
    
    denom = (By - Cy) * (Ax - Cx) + (Cx - Bx) * (Ay - Cy)
    if abs(denom) < 1e-10:
        return False
    
    a = ((By - Cy) * (Px - Cx) + (Cx - Bx) * (Py - Cy)) / denom
    b = ((Cy - Ay) * (Px - Cx) + (Ax - Cx) * (Py - Cy)) / denom
    c = 1 - a - b
    
    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

def process_sonar_data(sensor_positions, depth_points):
    variances = []
    triangle = sensor_positions[:3]
    
    valid_depths = []
    with depth_measurement_context(depth_points) as data:
        for point in data:
            coord = point['position']
            depth_val = point['depth']
            if is_point_in_triangle(coord, triangle):
                valid_depths.append(depth_val)
    
    if len(valid_depths) >= 2:
        var = statistics.variance(valid_depths)
        variances.append(var)
    
    return statistics.mean(variances) if variances else 0

# Sensor positions forming a triangle
sensor_nodes = [
    (0, 0),
    (10, 0),
    (5, 8.66)  # Equilateral triangle approximately
]

# Depth measurement points
sonar_readings = [
    {'position': (2, 2), 'depth': 120},
    {'position': (8, 1), 'depth': 118},
    {'position': (5, 3), 'depth': 122},
    {'position': (4, 5), 'depth': 119},
    {'position': (6, 6), 'depth': 121},
    {'position': (1, 1), 'depth': 117},
    {'position': (9, 2), 'depth': 118}
]

final_variance = process_sonar_data(sensor_nodes, sonar_readings)
print(f"Result: {final_variance}")