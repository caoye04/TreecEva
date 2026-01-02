from collections import defaultdict

# Simulated sensor data log with timestamps and readings
data_log = [
    ('temp', 23.5, 1), ('pressure', 101.3, 2), ('temp', 24.1, 3),
    ('humidity', 45, 4), ('temp', 22.8, 5), ('pressure', 100.7, 6),
    ('humidity', 47, 7), ('pressure', 102.1, 8), ('temp', 25.3, 9)
]

# Threshold for acceptable deviation
threshold = 1.5

# Tracking counts of each metric type
metric_counter = defaultdict(int)
summed_values = defaultdict(float)
peak_moments = []
baseline_ref = {'temp': 23.0, 'pressure': 101.0, 'humidity': 46}

deviation_log = []
smoothed_series = []
rolling_window = []

# Preprocess: extract and count metrics
for sensor_type, value, timestamp in data_log:
    metric_counter[sensor_type] += 1
    summed_values[sensor_type] += value

    # Compute deviation from baseline if applicable
    if sensor_type in baseline_ref:
        dev = abs(value - baseline_ref[sensor_type])
        deviation_log.append(dev)

        # Track significant deviations
        if dev > threshold:
            peak_moments.append((sensor_type, value, timestamp, dev))

# Misleading secondary analysis: normalize deviations (not used later)
normalized_devs = [d / (max(deviation_log) + 1e-5) for d in deviation_log]
for nd in normalized_devs:
    smoothed_series.append(round(nd * 100, 2))

# Auxiliary function to compute stability index
def calculate_stability(deviations):
    if not deviations:
        return 0.0
    mean_dev = sum(deviations) / len(deviations)
    variance = sum((x - mean_dev) ** 2 for x in deviations) / len(deviations)
    return round(1 / (1 + variance), 3)

# Another red herring: combinatorial pairing check (unused)
pair_count = 0
for i in range(len(data_log)):
    for j in range(i+1, len(data_log)):
        if data_log[i][0] == data_log[j][0]:
            pair_count += 1

# Main processing function
def process_metrics(log, thresh):
    temp_vals = []
    press_vals = []
    humid_vals = []

    for typ, val, ts in log:
        if typ == 'temp':
            temp_vals.append(val)
        elif typ == 'pressure':
            press_vals.append(val)
        elif typ == 'humidity':
            humid_vals.append(val)
    
    # Compute average trends
    avg_temp = sum(temp_vals) / len(temp_vals) if temp_vals else 0
    avg_press = sum(press_vals) / len(press_vals) if press_vals else 0
    avg_humid = sum(humid_vals) / len(humid_vals) if humid_vals else 0

    # Calculate cumulative precision score based on consistency
    temp_consistency = sum(1 for v in temp_vals if abs(v - avg_temp) < thresh)
    press_consistency = sum(1 for v in press_vals if abs(v - avg_press) < thresh)
    humid_consistency = sum(1 for v in humid_vals if abs(v - avg_humid) < thresh)

    total_consistent = temp_consistency + press_consistency + humid_consistency
    total_readings = len(log)

    # Efficiency score: ratio of consistent readings, weighted by metric frequency
    weights = {
        'temp': len(temp_vals) / total_readings,
        'pressure': len(press_vals) / total_readings,
        'humidity': len(humid_vals) / total_readings
    }

    efficiency_score = total_consistent / total_readings
    efficiency_score *= (1 + weights['temp'] * 0.1)  # Slight bonus for temperature coverage

    # Dead code branch: never executed due to fixed threshold
    if threshold < 0:
        efficiency_score *= 0.5  # hypothetical penalty

    # Additional distraction: string-based status tagging
    status_tags = []
    for sensor_type, _, _ in data_log:
        tag = f"{sensor_type[:3].upper()}-{len(sensor_type)}"
        status_tags.append(tag)
    
    final_tag_sequence = "|".join(status_tags)
    tag_entropy = len(set(status_tags)) / len(status_tags) if status_tags else 0

    # Critical result assignment
    return efficiency_score

# Execute main logic
final_output = process_metrics(data_log, threshold)
efficiency_score = final_output

# Print required result
print(f"Result: {efficiency_score}")