import itertools
import math

def calculate_zone_overlap(regions):
    overlaps = 0
    for pair in itertools.combinations(regions, 2):
        if pair[0] & pair[1]:  # Check if sets intersect
            overlaps += 1
    return overlaps

def transform_coordinates(x, y, scale):
    return (x * scale, y * scale)

class ProjectionContext:
    def __init__(self, base_scale=1.5):
        self.scale = base_scale
        self.processed_zones = set()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Initialize coordinate system
base_points = [(1, 2), (3, 4), (5, 6)]
zone_definitions = [
    frozenset([1, 2, 3]),
    frozenset([2, 3, 4]),
    frozenset([4, 5, 6]),
    frozenset([1, 5, 6])
]

with ProjectionContext(2.0) as ctx:
    # Transform coordinates
    transformed_points = [transform_coordinates(x, y, ctx.scale) for x, y in base_points]
    
    # Calculate geometric properties
    distances = []
    for i in range(len(transformed_points)-1):
        p1, p2 = transformed_points[i], transformed_points[i+1]
        distance = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
        distances.append(distance)
    
    # Process zone overlaps using short-circuit evaluation
    total_overlap = calculate_zone_overlap(zone_definitions)
    has_significant_overlap = total_overlap > 2 and len(zone_definitions) >= 4
    
    # Calculate spatial density
    avg_distance = sum(distances) / len(distances) if distances else 0
    
    # Final zone scoring algorithm
    zone_density = len(zone_definitions) * 1.5
    final_zone_score = int((avg_distance * zone_density) + (10 if has_significant_overlap else 0))

print(f"Result: {final_zone_score}")