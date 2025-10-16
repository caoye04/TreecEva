import math

class PrecisionHandler:
    def __init__(self, precision_bits=8):
        self.precision_bits = precision_bits
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass
    
    def adjust_precision(self, value):
        mask = (1 << self.precision_bits) - 1
        return value & mask

def calculate_polygon_diameter(vertices):
    max_distance = 0
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            dx = vertices[i][0] - vertices[j][0]
            dy = vertices[i][1] - vertices[j][1]
            distance = math.sqrt(dx*dx + dy*dy)
            if distance > max_distance:
                max_distance = distance
    return max_distance

def compute_circle_area_from_diameter(diameter):
    radius = diameter / 2.0
    return math.pi * radius * radius

# Vertex coordinates of a convex polygon
polygon_vertices = [
    (0, 0),
    (4, 0),
    (4, 3),
    (0, 3)
]

with PrecisionHandler() as handler:
    diameter = calculate_polygon_diameter(polygon_vertices)
    adjusted_diameter = handler.adjust_precision(int(diameter * 1000))
    if adjusted_diameter > 5000:
        final_area = compute_circle_area_from_diameter(adjusted_diameter / 1000.0)
    else:
        # Compensate with a fixed value based on bit manipulation
        compensation = (adjusted_diameter << 2) | 0b11
        final_area = compute_circle_area_from_diameter(compensation / 1000.0)

print(f"Result: {round(final_area, 2)}")