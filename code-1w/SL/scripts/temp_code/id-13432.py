from collections import defaultdict

# Simulate sensor data readings over time
sensor_readings = [
    ('power', 105), ('temp', 32), ('power', 98), ('power', 102),
    ('temp', 35), ('power', 110), ('power', 95), ('power', 108)
]

# Separate power levels using defaultdict
readings_dict = defaultdict(list)
for sensor_type, value in sensor_readings:
    readings_dict[sensor_type].append(value)

# Extract and filter power levels above threshold
power_levels = readings_dict['power']
filtered_power_levels = [level for level in power_levels if level > 100]

# Compute total load from filtered levels
total_load = sum(filtered_power_levels)

# Print result
print(f"Result: {total_load}")