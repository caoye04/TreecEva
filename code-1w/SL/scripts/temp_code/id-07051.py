def analyze_readings(data, limit):
    warnings = []
    critical_count = 0
    temp_log = []

    for val in data:
        adjusted = abs(val - 50) * 0.8
        category = 'normal'

        if adjusted > 40:
            category = 'critical'
            critical_count += 1
        elif adjusted > 25:
            category = 'elevated'

        temp_log.append((val, adjusted, category))

        if len(temp_log) % 3 == 0:
            # Red herring: tracking every third entry (not used later)
            dummy_flag = True

    # Simulate secondary analysis with no real impact
    outlier_indices = {i for i, v in enumerate(data) if v < 10 or v > 90}
    shadow_copy = [x for x in data if x > limit]  # unused list comprehension

    # Actual logic: compute diagnostic score based on critical readings
    base_score = sum(1 for item in temp_log if item[2] == 'critical')
    penalty = len([v for v in data if v < 0]) * 2  # irrelevant: no negative values
    final_score = base_score * 10 - penalty

    consistency_check = all(data[i] <= data[i+1] for i in range(len(data)-1))  # unused

    return final_score


# Sensor simulation parameters
initial_threshold = 15
raw_readings = [23, 67, 88, 45, 12, 91, 74, 56]

# Preprocessing: filter out readings below threshold (simulated calibration)
filtered_data = [x for x in raw_readings if x >= initial_threshold]

# Extraneous state tracking
system_status = {'calibrated': True, 'mode': 'diagnostic'}
data_snapshot = set(raw_readings)  # distractor
backup_readings = tuple(sorted(raw_readings))  # more distraction

# Key computation
final_diagnostic = analyze_readings(filtered_data, initial_threshold)

# Dummy bitwise check (irrelevant to result)
mask = 0b1101
flagged = mask & len(filtered_data) > 0

# Final output
print(f"Result: {final_diagnostic}")