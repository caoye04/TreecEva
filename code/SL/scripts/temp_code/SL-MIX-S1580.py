import math
from functools import reduce

class SensorNode:
    def __init__(self, x, y, next_node=None):
        self.x = x
        self.y = y
        self.next = next_node

def create_sensor_network(coordinates):
    head = None
    for coord in reversed(coordinates):
        head = SensorNode(coord[0], coord[1], head)
    return head

def calculate_polygon_area(head):
    coords = []
    current = head
    while current:
        coords.append((current.x, current.y))
        current = current.next
    
    n = len(coords)
    if n < 3:
        return 0
    
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += coords[i][0] * coords[j][1]
        area -= coords[j][0] * coords[i][1]
    return abs(area) / 2.0

def transform_coordinates(head, scale_factor):
    current = head
    while current:
        current.x *= scale_factor
        current.y *= scale_factor
        current = current.next
    return head

# Initialize sensor network
sensor_coords = [(0, 0), (4, 0), (4, 3), (0, 3)]
sensor_network = create_sensor_network(sensor_coords)

# Apply transformations using functional programming
scaling_operations = [1.5, 2.0, 0.5]
transformed_network = reduce(lambda net, scale: transform_coordinates(net, scale), scaling_operations, sensor_network)

# Calculate base coverage area
base_area = calculate_polygon_area(transformed_network)

# Apply additional geometric adjustments
adjustment_factors = [1.1, 0.9, 1.05]
adjusted_areas = [base_area * factor for factor in adjustment_factors]

# Determine optimal coverage using lambda and filtering
valid_areas = list(filter(lambda area: area > 10 and area < 50, adjusted_areas))
optimal_coverage_area = max(valid_areas) if valid_areas else 0

print(f"Result: {optimal_coverage_area}")