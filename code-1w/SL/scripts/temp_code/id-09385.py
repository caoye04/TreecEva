from collections import defaultdict, Counter

# Simulate sensor readings with noise and calibration offsets
def preprocess_readings(raw_data):
    calibrated = []
    base_offset = 0.5
    temp_adjustment = 0.0

    for val in raw_data:
        if val < 0:
            temp_adjustment = -0.1
        elif val == 0:
            temp_adjustment = 0.0
        else:
            temp_adjustment = 0.2

        adjusted = val + base_offset + temp_adjustment
        if adjusted > 1.0:
            adjusted = 1.0
        calibrated.append(round(adjusted, 2))

    # Irrelevant aggregation
    stats = defaultdict(int)
    for c in calibrated:
        stats[int(c * 10)] += 1

    return calibrated

# Filter out unstable readings
def filter_anomalies(seq):
    window_size = 3
    filtered = seq[:]
    anomaly_flags = [False] * len(seq)

    for i in range(window_size, len(seq)):
        window = seq[i - window_size:i]
        avg = sum(window) / window_size
        if abs(seq[i] - avg) > 0.4:
            anomaly_flags[i] = True

    cleaned = [seq[i] for i in range(len(seq)) if not anomaly_flags[i]]
    
    # Distractor: unused frequency map
    freq = Counter(cleaned)
    high_freq = [k for k, v in freq.items() if v > 1]

    return cleaned if cleaned else [0.0]

# Compute final reliability score
def compute_final_score(readings_list):
    total_weight = 0.0
    cumulative = 0.0

    weights = [0.8, 1.0, 1.2]
    category_tally = defaultdict(int)

    for r in readings_list:
        bucket = int(r * 10)
        category_tally[bucket] += 1

    for idx, r in enumerate(readings_list):
        w = weights[idx % 3]
        adjusted_r = r ** 2  # emphasize higher values

        # Apply diminishing returns above threshold
        if adjusted_r > 0.7:
            adjusted_r = 0.7 + (adjusted_r - 0.7) * 0.5

        contribution = adjusted_r * w
        cumulative += contribution
        total_weight += w

    # Dead code branch - never reached due to non-empty input
    if len(readings_list) == 0:
        fallback = 1.0
        cumulative = fallback
        total_weight = 1.0

    final = cumulative / total_weight if total_weight != 0 else 0.0
    return round(final, 4)

# Main execution
if __name__ == "__main__":
    raw_sensor_data = [0.3, -0.1, 0.8, 0.0, 1.1, 0.7, 0.9, -0.2]
    
    # Intermediate variables with side processing
    processed = preprocess_readings(raw_sensor_data)
    clean_data = filter_anomalies(processed)
    
    # Debugging counters (distractors)
    under_threshold = len([x for x in clean_data if x < 0.5])
    over_threshold = len([x for x in clean_data if x >= 0.5])
    ratio_warning = over_threshold / under_threshold if under_threshold != 0 else 0
    
    # Key computation
    final_score = compute_final_score(clean_data)
    
    # Additional irrelevant transformation
    normalized_scores = [round((s - 0.1) * 1.1, 4) for s in clean_data]
    average_normalized = sum(normalized_scores) / len(normalized_scores) if normalized_scores else 0
    
    print(f"Result: {final_score}")