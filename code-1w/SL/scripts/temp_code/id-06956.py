from itertools import combinations
from math import log

# Simulate sensor data processing with noise filtering and metric extraction
def preprocess_sensor_readings(readings):
    filtered = [r for r in readings if 10 <= r <= 100]
    normalized = [(x - 10) / 90 for x in filtered]
    return normalized

# Calculate entropy of distribution as a stability metric
def calculate_entropy(values):
    if not values:
        return 0.0
    value_counts = {}
    for v in values:
        rounded = round(v, 2)
        value_counts[rounded] = value_counts.get(rounded, 0) + 1
    total = len(values)
    entropy = -sum((count / total) * log(count / total) for count in value_counts.values())
    return round(entropy, 4)

# Dummy function to simulate redundant computation
def compute_redundant_metrics(data):
    # These computations are not used in final result
    mean_val = sum(data) / len(data) if data else 0
    variance = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0
    peak_to_peak = max(data) - min(data) if data else 0
    # Return unused metrics
    return mean_val, variance, peak_to_peak

# Main evaluation logic combining multiple concepts
def evaluate_performance(metrics, raw_data):
    # Irrelevant intermediate transformation (distractor)
    temp_transform = [x * 1.05 for x in raw_data if x > 20]
    temp_result = sum(temp_transform[:10]) if temp_transform else 0

    score = 0

    # Use of set operations to identify unique pattern combinations
    base_set = set(metrics)
    extended_combinations = list(combinations(base_set, 2))
    pair_count = len(extended_combinations)

    # Key scoring logic based on entropy and combination diversity
    if 'entropy' in metrics:
        clean_data = preprocess_sensor_readings(raw_data)
        entropy_value = calculate_entropy(clean_data)
        score += int(entropy_value * 100)

    if 'diversity' in metrics:
        score += pair_count * 2

    # Logical short-circuit and conditional weighting
    weights = {'critical': 3, 'monitor': 1}
    alert_mode = 'critical' if score > 40 else 'monitor'
    multiplier = weights[alert_mode] if alert_mode in weights else 1

    # Final score computation
    final_score = score * multiplier

    # Dead code path - never executed due to fixed condition (distractor)
    debug_trace = False
    if debug_trace:
        print(f'Trace: {temp_result=}, {pair_count=}')

    return final_score

# Input data
metric_set = {'entropy', 'diversity', 'latency', 'throughput'}
raw_data = [15, 23, 45, 23, 67, 89, 23, 45, 12, 90, 76, 45, 33, 88]

# Redundant variable assignments (misleading)
data_copy = raw_data.copy()
sorted_data = sorted(raw_data)
outlier_flags = [x for x in raw_data if x < 10 or x > 100]

# Unused helper using lambda (distractor)
process_fn = lambda seq, func: [func(x) for x in seq]
squared_data = process_fn(raw_data, lambda x: x**2)

# Actual key execution point
final_score = evaluate_performance(metric_set, raw_data)

# Output result
print(f"Result: {final_score}")