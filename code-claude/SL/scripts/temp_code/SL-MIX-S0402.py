# Calculate total distance traveled based on city coordinates
coordinates = [(0, 0), (3, 4), (7, 7), (2, 8)]

# Calculate distances between consecutive points
distances = []
for i, points in enumerate(zip(coordinates[:-1], coordinates[1:])):
    start, end = points
    x_diff = end[0] - start[0]
    y_diff = end[1] - start[1]
    distance = (x_diff**2 + y_diff**2)**0.5
    distances.append(distance)

# Track progress through journey
cities_visited = len(coordinates)
remaining_cities = 0  # No cities remaining after full journey

# Calculate total journey distance
total_distance = sum(distances)
print(f"Result: {total_distance}")