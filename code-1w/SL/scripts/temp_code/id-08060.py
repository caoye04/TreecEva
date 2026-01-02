from collections import defaultdict

# Simulate sensor data with timestamps and readings
timestamped_readings = [
    (1001, [23.4, 25.1, 22.9]),
    (1002, [24.0, None, 23.7]),
    (1003, [22.5, 23.8, 24.1]),
    (1004, [None, 25.3, 23.9]),
    (1005, [24.2, 24.6, None])
]

# Irrelevant backup list for distraction
backup_readings = timestamped_readings.copy()

# Track valid readings per sensor index
valid_count = [0, 0, 0]
sensor_sums = [0.0, 0.0, 0.0]

# Aggregate valid sensor data
dropped_readings = 0
for ts, readings in timestamped_readings:
    for i, val in enumerate(readings):
        if val is not None:
            sensor_sums[i] += val
            valid_count[i] += 1
        else:
            dropped_readings += 1

# Compute averages, default to 0 if no valid data
sensor_avgs = [
    sensor_sums[i] / valid_count[i] if valid_count[i] > 0 else 0 
    for i in range(3)
]

# Distractor: unused computation for median-like behavior
sorted_avgs = sorted(sensor_avgs)
median_avg = sorted_avgs[1]  # Not used later

# Simulate pressure adjustment model
base_pressure = 1013.25
altitude_factor = 0.87
adjusted_base = base_pressure * altitude_factor

# Extract magnitude from deviations (deviation > 0.5 triggers inclusion)
magnitude_sum = 0.0
deviation_threshold = 0.5
reference_avg = sum(sensor_avgs) / len(sensor_avgs)

for avg in sensor_avgs:
    deviation = abs(avg - reference_avg)
    if deviation >= deviation_threshold:
        magnitude_sum += deviation

# Unused alternate calculation path (dead-end logic)
if magnitude_sum < 1.0:
    fallback_correction = 0.1 * base_pressure
else:
    temp_adjust = 0.05 * magnitude_sum  # Computed but unused

# Impact factor based on frequency of significant deviations
deviation_events = 0
event_log = defaultdict(int)

for avg in sensor_avgs:
    if abs(avg - reference_avg) >= deviation_threshold:
        event_log['significant'] += 1
        deviation_events += 1
    else:
        event_log['normal'] += 1

impact_factor = 1.75 if deviation_events >= 2 else 1.2

# Key statement
final_pressure = adjusted_base + (magnitude_sum * impact_factor)

# Print result for evaluation
print(f"Result: {final_pressure}")