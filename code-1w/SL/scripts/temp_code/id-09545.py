from itertools import compress, cycle

# Simulate sensor data validation and weighted performance scoring
def validate_readings(readings):
    valid_mask = [(x > 0 and x < 100) and (x % 2 == 1) for x in readings]
    return list(compress(readings, valid_mask))

def calculate_stability_factor(seq):
    diffs = [abs(a - b) for a, b in zip(seq, seq[1:])]
    return round(sum(diffs) / len(diffs), 4) if diffs else 0.0

def normalize_values(data):
    max_val = max(data) if data else 1
    return [round(x / max_val, 4) for x in data]

def evaluate_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    adjustment = 0.987
    return int(weighted_sum * adjustment)

# Raw sensor inputs (temperature, pressure, humidity, voltage, vibration)
sensor_inputs = [87, 105, 43, -20, 67, 92, 150, 73]

# Filter valid odd-valued readings within operational range
valid_data = validate_readings(sensor_inputs)

# Compute derived metrics
stability = calculate_stability_factor(valid_data)
normalized = normalize_values(valid_data)

# Auxiliary calculations (distractor: not used in final score)
baseline_shift = sum(1 for x in sensor_inputs if x > 100)
outlier_ratio = len(sensor_inputs) - len(valid_data) / len(sensor_inputs) if valid_data else 0

# Generate phase weights using cycling pattern (relevant)
weight_pattern = [0.8, 1.2, 0.9]
temp_weights = list(zip(normalized, cycle(weight_pattern)))
weights = [w for _, w in temp_weights[:len(normalized)]]

# Key metrics for evaluation
metrics = [
    sum(normalized),
    100 - stability * 10,
    len(valid_data) * 0.5,
    sum(weights)
]

# Misleading intermediate computation (dead-end)
aggregated_diagnostics = {
    'peak': max(valid_data) if valid_data else 0,
    'floor': min(valid_data) if valid_data else 0,
    'span': len(valid_data),
    'noise_floor': stability * 5
}

# This lambda is used to filter out low contributions (relevant)
filter_threshold = lambda x, th: x if x >= th else 0
refined_metrics = [filter_threshold(m, 0.5) for m in metrics]

# Final performance score computation
final_score = evaluate_performance(refined_metrics, weights)

# Print result as required
print(f"Result: {final_score}")