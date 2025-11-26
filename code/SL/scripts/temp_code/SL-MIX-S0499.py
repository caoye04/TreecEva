route_points = [25, 42, 18, 56, 33]
checkpoint_times = [10, 25, 40, 55, 70]

enumerate_distances = []
for idx, point in enumerate(route_points):
    if idx < len(route_points) - 1:
        distance_segment = route_points[idx + 1] - point
        enumerate_distances.append(abs(distance_segment))

# Calculate total distance
auxiliary_sum = 0
for dist in enumerate_distances:
    auxiliary_sum += dist

total_distance = sum(enumerate_distances)
print(f"Result: {total_distance}")