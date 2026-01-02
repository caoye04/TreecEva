def calculate_efficiency(data, limit):
    filtered = [x for x in data if x > limit]
    if not filtered:
        return 0.0
    avg = sum(filtered) / len(filtered)
    variance = sum((x - avg) ** 2 for x in filtered) / len(filtered)
    efficiency = (avg / (variance + 1)) if variance != 0 else avg
    return efficiency

# Sensor profile simulation (irrelevant preprocessing)
sensor_offsets = [0.1, -0.3, 0.5, 0.0, -0.2]
baseline_readings = [12, 15, 18, 14, 20, 22, 10]
adjusted_readings = [r + sensor_offsets[i % len(sensor_offsets)] for i, r in enumerate(baseline_readings)]

# Actual relevant data
profile_data = [8, 12, 15, 16, 18, 20, 25, 28]
threshold = 14
scaling_factor = 100

# Dummy transformations (distractors)
dummy_map = list(map(lambda x: x * 0.95 + 2, baseline_readings))
dummy_slice = adjusted_readings[1:5:2]

# Core computation with key intervention point
temp_buffer = tuple(x * 1.1 for x in profile_data)
working_set = {i: val for i, val in enumerate(temp_buffer)}

# Linear search for first above threshold (semi-relevant)
first_above = None
for idx, val in enumerate(profile_data):
    if val > threshold:
        first_above = idx
        break

# Critical assignment
thermal_capacity = calculate_efficiency(profile_data, threshold) * scaling_factor

# Redundant aggregation (dead code path)
if first_above is not None:
    excess_energy = sum(profile_data[first_above:])
    normalized_score = excess_energy / len(profile_data[first_above:])

Result: {thermal_capacity}