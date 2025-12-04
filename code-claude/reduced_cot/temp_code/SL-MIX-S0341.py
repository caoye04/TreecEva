import itertools

# Sensor network configuration
sensor_readings = [5, 3, 8, 3, 7, 5, 2, 8]
temperature_threshold = 4

# Process sensor data
valid_count = 0
filtered_sensors = []

for reading in sensor_readings:
    # Count valid readings above threshold
    if reading > temperature_threshold:
        valid_count += 1
        filtered_sensors.append(reading)

# Calculate possible sensor pairs for triangulation
total_sensors = len(filtered_sensors)
possible_pairs = total_sensors * (total_sensors - 1) // 2

# Find unique combinations (ignoring duplicate readings)
unique_combinations = sum(1 for x in itertools.combinations(filtered_sensors, 2))

# Alternative calculation method (not used)
manual_count = 0
for i in range(len(filtered_sensors)):
    for j in range(i + 1, len(filtered_sensors)):
        if filtered_sensors[i] != filtered_sensors[j]:
            manual_count += 1

# Final result is the number of unique sensor combinations
print(f"Result: {unique_combinations}")