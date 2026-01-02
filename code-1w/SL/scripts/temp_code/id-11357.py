from collections import defaultdict

# Simulate sensor data from industrial machinery over time
timestamps = [101, 102, 103, 104, 105, 106, 107, 108]
sensor_readings = [23, 45, 12, 67, 45, 23, 89, 45]

# Map each reading to list of timestamps it occurred at
time_map = defaultdict(list)
for t, val in zip(timestamps, sensor_readings):
    time_map[val].append(t)

# Extract duplicate readings (occur more than once)
duplicates = {k: v for k, v in time_map.items() if len(v) > 1}

# Calculate frequency score (irrelevant to final result but adds distraction)
frequency_score = 0
for val, times in time_map.items():
    frequency_score += len(times) * (val % 7)

# Identify high-stress values above threshold
high_stress_values = [v for v in sensor_readings if v > 40]

# Count transitions between high-stress states
stress_transitions = 0
for i in range(1, len(sensor_readings)):
    if sensor_readings[i-1] > 40 and sensor_readings[i] > 40:
        stress_transitions += 1

# Compute baseline efficiency (average of unique high-stress values)
efficiency = sum(set(high_stress_values)) / len(set(high_stress_values))

# Determine peak periods based on clustered duplicates
peak_periods = 0
for val, times in duplicates.items():
    if val > 40:  # Only high-stress duplicates count
        for i in range(1, len(times)):
            if times[i] - times[i-1] == 1:  # Consecutive timestamps
                peak_periods += 1

# Dead code: simulates calibration but unused
baseline_calibration = []
for x in range(3):
    temp = 0
    for y in sensor_readings[:3]:
        temp += y ** (x + 1)
    baseline_calibration.append(temp)

# Misleading intermediate calculation (not used in final result)
average_gap = 0
if len(time_map[45]) > 1:
    gaps = [time_map[45][i] - time_map[45][i-1] for i in range(1, len(time_map[45]))]
    average_gap = sum(gaps) / len(gaps)

# Core logic function
def calculate_stress_factor(efficiency, peaks):
    factor = efficiency * 1.75
    if peaks > 0:
        factor += peaks * 2.5
    return round(factor, 2)

# Critical execution point
final_load = calculate_stress_factor(efficiency, peak_periods)

print(f"Result: {final_load}")