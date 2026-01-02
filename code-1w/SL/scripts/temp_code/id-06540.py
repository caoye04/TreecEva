from collections import defaultdict

# Simulate sensor data aggregation for a thermal regulation system
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 23.7]
humidity_readings = [45, 47, 46, 50, 48, 49, 46]

# Irrelevant data buffer (distractor)
data_buffer = [0] * len(temperature_readings)
for i in range(len(data_buffer)):
    data_buffer[i] = temperature_readings[i] * humidity_readings[i % len(humidity_readings)]

# Track frequency of temperature bands (semi-relevant, not used in final result)
temp_buckets = defaultdict(int)
for temp in temperature_readings:
    band = int(temp // 1)
    temp_buckets[band] += 1

# Primary computation: system configuration
base_capacity = sum(temperature_readings) / len(temperature_readings)

# Efficiency model with conditional adjustments
efficiency_factor = 1.0
if base_capacity > 23.5:
    efficiency_factor = 0.92
else:
    efficiency_factor = 1.05

# Redundancy logic with nested condition and loop (only one branch matters)
redundancy_offset = 0
status_codes = [200, 404, 500, 200, 200]
for code in status_codes:
    if code == 200:
        redundancy_offset += 1
    elif code == 500:
        redundancy_offset -= 0.5

# Distractor: unused function
def calculate_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Distractor variables
variance_proxy = 0
for t in temperature_readings:
    variance_proxy += (t - base_capacity) ** 2
variance_proxy /= len(temperature_readings)

# Key statement
thermal_capacity = base_capacity * efficiency_factor + redundancy_offset

# Output result
print(f"Result: {thermal_capacity}")