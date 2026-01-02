from collections import defaultdict, Counter

# Simulate sensor data with noise and redundancy
def preprocess_sensor_data(raw_data):
    processed = []
    noise_offset = 0.5
    for item in raw_data:
        cleaned = item - noise_offset
        if cleaned > 0:
            processed.append(round(cleaned, 2))
    return processed

# Analyze frequency of readings above threshold
def analyze_peaks(values):
    freq = Counter(values)
    peak_count = 0
    for val, count in freq.items():
        if val > 2.0:
            peak_count += count
    return peak_count

# Compute weighted average with decay factor
def compute_trend(scores, decay=0.9):
    trend = 0.0
    weight_sum = 0.0
    for i, score in enumerate(reversed(scores)):
        weighted_score = score * (decay ** i)
        trend += weighted_score
        weight_sum += (decay ** i)
    return round(trend / weight_sum, 4) if weight_sum != 0 else 0.0

# Main scoring logic
def calculate_final_score(data_entries, importance_weights):
    temp_store = defaultdict(list)
    total_entries = 0
    valid_sensors = set()

    # Process each sensor stream (some are redundant)
    for sensor_id, readings in data_entries.items():
        filtered = [x for x in readings if x >= 0.1]  # remove low noise
        if len(filtered) > 2:
            smoothed = preprocess_sensor_data(filtered)
            if len(smoothed) > 0:
                temp_store[sensor_id].extend(smoothed)
                valid_sensors.add(sensor_id)
                total_entries += len(smoothed)

    # Aggregate scores per sensor group
    group_scores = {}
    for sid, vals in temp_store.items():
        base_avg = sum(vals) / len(vals)
        peak_factor = analyze_peaks(vals) / len(vals) if vals else 0
        adjusted = base_avg * (1 + peak_factor)
        group_scores[sid] = round(adjusted, 4)

    # Apply external weights and compute composite
    final_components = []
    for sensor, score in group_scores.items():
        weight = importance_weights.get(sensor, 1.0)
        contribution = score * weight
        final_components.append(contribution)

    # Secondary adjustment based on trend analysis
    trend_input = [group_scores.get(k, 0) for k in sorted(group_scores.keys())]
    temporal_trend = compute_trend(trend_input)

    # Final nonlinear transformation
    raw_sum = sum(final_components)
    penalty = len(set(importance_weights.keys()) - valid_sensors) * 0.2  # missing sensor penalty
    efficiency_ratio = raw_sum / (total_entries + 1) if total_entries else 0

    # Irrelevant distraction: buffer tracking (not used in final result)
    buffer_status = {}
    for i in range(3):
        buffer_status[f'buf_{i}'] = (i * 1.5) % 2.3
    overflow_flag = False
    for k, v in buffer_status.items():
        if v > 2.0:
            overflow_flag = True

    # Actual final score computation
    final_score = (raw_sum + temporal_trend) * (1 - penalty)
    final_score = round(final_score + efficiency_ratio, 4)

    return final_score

# Input data setup
data = {
    'sensor_A': [1.2, 1.3, 1.4, 1.5, 2.1],
    'sensor_B': [0.9, 0.8, 3.1, 3.2, 3.3, 0.7],
    'sensor_C': [0.2, 0.3, 0.1],
    'sensor_D': [2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
}

weights = {
    'sensor_A': 1.1,
    'sensor_B': 0.9,
    'sensor_D': 1.3
}

# Execute main logic
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")