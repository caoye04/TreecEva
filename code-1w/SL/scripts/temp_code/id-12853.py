import itertools

def analyze_temperature_stability(temps):
    stability_score = 0
    for i in range(1, len(temps)):
        if abs(temps[i] - temps[i-1]) < 5:
            stability_score += 1
    return stability_score > len(temps) * 0.7

def transform_readings(sensor_data, threshold=25):
    filtered = []
    noise_count = 0
    for val in sensor_data:
        adjusted = val * 1.02 - 3.1
        if abs(adjusted - val) > threshold:
            noise_count += 1  # distractor: not used later
        if adjusted > 0:
            filtered.append(round(adjusted, 2))
    return filtered

def evaluate_consistency(data_sequence):
    diffs = [abs(a - b) for a, b in zip(data_sequence, data_sequence[1:])]
    avg_change = sum(diffs) / len(diffs) if diffs else 0
    return avg_change < 4.0

def calculate_optimal_yield(clean_data):
    weighted_sum = 0.0
    multiplier = 1.5
    for idx, val in enumerate(clean_data):
        if idx % 3 == 0:
            weighted_sum += val * multiplier
        elif idx % 2 == 0:
            weighted_sum += val * 0.8
        else:
            weighted_sum += val * 1.1
    penalty_factor = 0.95
    applied_penalty = False
    if len(clean_data) > 10 and sum(clean_data) / len(clean_data) > 20:
        weighted_sum *= penalty_factor
        applied_penalty = True  # dead code path: not used
    return round(weighted_sum, 4)

# Simulate multi-stage industrial sensor processing
raw_sensor_input = [23.5, 24.1, 19.8, 26.7, 25.3, 27.0, 22.9, 20.4, 28.2, 26.8, 24.6, 23.9]

# Step 1: Noise filtering and adjustment
processed_data = transform_readings(raw_sensor_input, threshold=20)

# Distractor computations
window_pairs = list(itertools.combinations(processed_data[:5], 2))
high_diff_windows = list(filter(lambda pair: abs(pair[0] - pair[1]) > 4.5, window_pairs))
distinct_values = set(round(x, 0) for x in processed_data)
value_counts = {v: processed_data.count(v) for v in processed_data}

# Step 2: Stability analysis (not directly affecting yield but adds cognitive load)
is_stable = analyze_temperature_stability(processed_data)
is_consistent = evaluate_consistency(processed_data)

# Step 3: Final yield calculation — this is where the answer comes from
final_yield = calculate_optimal_yield(processed_data)

# Irrelevant aggregation
aggregate_metrics = {
    'total': sum(processed_data),
    'peak': max(processed_data, default=0),
    'baseline_ratio': sum(processed_data) / (raw_sensor_input[0] * len(processed_data))
}

# Print result as required
Target result: {final_yield}