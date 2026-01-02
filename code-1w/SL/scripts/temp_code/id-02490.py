from math import sqrt

# Sensor readings in a grid layout (x, y coordinates)
x_coords = [1, 4, 7, 3, 9]
y_coords = [2, 6, 8, 1, 5]

# Reference point for distance calculation (e.g., control station)
ref_x, ref_y = 5, 5

distances = []
for x, y in zip(x_coords, y_coords):
    dist = sqrt((x - ref_x)**2 + (y - ref_y)**2)
    distances.append(round(dist, 2))

# Filter distances within a threshold range
close_readings = {i for i, d in enumerate(distances) if d < 4.5}
filtered_distances = [distances[i] for i in close_readings]

# Irrelevant auxiliary variable (minimal interference)
temp_status = "processing"

result = sum(filtered_distances)