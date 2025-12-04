def calculate_euclidean_distance(points):
    # Calculate sum of squared distances from origin
    total = 0
    for x, y in points:
        total += (x ** 2 + y ** 2) ** 0.5
    return total

def calculate_manhattan_distance(points):
    # Calculate sum of Manhattan distances from origin
    total = 0
    for x, y in points:
        total += abs(x) + abs(y)
    return total

# Sample geographic coordinates (x, y) of interest points
raw_points = [(3, 4), (1, -2), (5, 12), (-8, 3), (0, 0), (7, -4)]

# Metadata for each point (not used in final calculation)
point_metadata = {
    (3, 4): "Museum",
    (1, -2): "Cafe",
    (5, 12): "Park",
    (-8, 3): "Library",
    (0, 0): "Center",
    (7, -4): "Restaurant"
}

# Filter points based on quadrant
quadrant_points = {}
for idx, (x, y) in enumerate(raw_points):
    if x > 0 and y > 0:
        quadrant = 1
    elif x < 0 and y > 0:
        quadrant = 2
    elif x < 0 and y < 0:
        quadrant = 3
    elif x > 0 and y < 0:
        quadrant = 4
    else:
        quadrant = 0
    
    if quadrant not in quadrant_points:
        quadrant_points[quadrant] = []
    quadrant_points[quadrant].append((x, y))

# Calculate distances for points in different quadrants
euclidean_distances = {}
for quadrant, points in quadrant_points.items():
    if quadrant != 0:  # Skip center point
        euclidean_distances[quadrant] = calculate_euclidean_distance(points)

# Create a set of points in quadrants 1 and 4 (points with positive x)
positive_x_points = set()
for point in raw_points:
    x, y = point
    if x > 0:
        positive_x_points.add(point)

# Filter points for final calculation - only use points in quadrants 1 and 4
filtered_points = []
for point in raw_points:
    if point in positive_x_points and point_metadata[point] != "Center":
        filtered_points.append(point)

# Sort filtered points by x-coordinate (not needed for calculation)
filtered_points.sort(key=lambda p: p[0])

# Calculate the final Manhattan distance
final_distance = calculate_manhattan_distance(filtered_points)

# Alternative calculation that's not used
unused_avg = sum(euclidean_distances.values()) / len(euclidean_distances) if euclidean_distances else 0

print(f"Result: {final_distance}")