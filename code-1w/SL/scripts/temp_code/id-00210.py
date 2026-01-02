from collections import defaultdict
import math

def encode_triangulation(triangles):
    encoded = 0
    for i, triangle in enumerate(triangles):
        # Simple encoding: sum of vertex indices shifted by position
        value = sum(triangle) << (i % 8)
        encoded ^= value
    return encoded

def greedy_triangulation(points):
    # Sort points by x-coordinate (greedy choice)
    points.sort(key=lambda p: p[0])
    triangles = []
    
    # Create triangles using consecutive triplets after sorting
    for i in range(len(points) - 2):
        triangle = (points[i][2], points[i+1][2], points[i+2][2])  # Use point IDs
        triangles.append(tuple(sorted(triangle)))  # Normalize triangle representation
    
    return triangles

def calculate_elevation_stats(elevations):
    total = sum(elevations)
    count = len(elevations)
    avg = total // count if count else 0
    return avg

elevation_data = [
    (10.5, 20.3, 1),   # (x, y, point_id)
    (15.2, 25.1, 2),
    (12.8, 22.7, 3),
    (18.9, 30.4, 4),
    (14.6, 24.8, 5),
    (16.3, 26.9, 6)
]

# Step 1: Calculate average elevation
elevations = [int(p[0]*p[1]) for p in elevation_data]  # Derived elevation metric
avg_elevation = calculate_elevation_stats(elevations)

# Step 2: Filter points above average (greedy filtering)
filtered_points = [p for p in elevation_data if int(p[0]*p[1]) > avg_elevation]

# Step 3: Generate triangulation
triangulation_result = greedy_triangulation(filtered_points)

# Step 4: Encode triangulation
encoded_result = encode_triangulation(triangulation_result)

print(f"Result: {encoded_result}")