from itertools import compress

# Sensor readings from air quality monitoring stations
readings = [45, 60, 72, 88, 91, 33, 54, 76, 83, 95]

# Threshold-based filter: identify readings above threshold and even-indexed
above_threshold = [x > 70 for x in readings]
even_indices = [i % 2 == 0 for i in range(len(readings))]

# Combined condition using logical AND via zip and map with lambda
effective_mask = list(map(lambda pair: pair[0] and pair[1], zip(above_threshold, even_indices)))

# Extract qualifying readings using itertools.compress
filtered_results = list(compress(readings, effective_mask))

# Final computation step
filtration_efficiency = sum(filtered_results)

print(f"Result: {filtration_efficiency}")