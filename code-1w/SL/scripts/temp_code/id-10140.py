from itertools import compress

# Sensor readings from water quality monitoring stations
data_readings = [0.88, 1.22, 0.95, 1.01, 0.76, 1.34, 0.89, 1.15]
threshold = 1.1

# Boolean criteria: acceptable if below threshold and not anomalous by pattern
is_acceptable = [x < threshold for x in data_readings]
has_stable_neighbor = [abs(data_readings[i] - data_readings[i-1]) < 0.2 for i in range(1, len(data_readings))]
has_stable_neighbor.insert(0, True)  # First element assumed stable

# Combine conditions using logical operations
valid_conditions = [a and b for a, b in zip(is_acceptable, has_stable_neighbor)]

# Use itertools.compress to filter valid sensor data
filtered_data = list(compress(data_readings, valid_conditions))

# Final computation on cleaned dataset
filtration_score = sum(filtered_data)
print(f"Result: {filtration_score}")