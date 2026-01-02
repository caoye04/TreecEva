import math

# Simulated sensor fusion system for environmental monitoring
sensor_a_data = [0.85, 0.91, 0.76, 0.88, 0.90]
sensor_b_data = [0.79, 0.83, 0.81, 0.87, 0.85]
sensor_c_data = [0.92, 0.89, 0.94, 0.90, 0.88]

# Irrelevant calibration offsets (distractors)
calibration_x = 0.021
calibration_y = -0.013
calibration_z = 0.009

# Noise thresholds (unused in final calculation)
noise_floor = 0.05
saturation_limit = 0.95

# Preprocess: normalize and filter data (some irrelevant steps included)
def preprocess_sensor_data(raw_data, threshold=0.0):
    filtered = [x for x in raw_data if abs(x - sum(raw_data)/len(raw_data)) < 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return normalized

processed_a = preprocess_sensor_data(sensor_a_data)
processed_b = preprocess_sensor_data(sensor_b_data)
processed_c = preprocess_sensor_data(sensor_c_data)

# Fused metric computation (relevant)
mean_a = sum(processed_a) / len(processed_a)
mean_b = sum(processed_b) / len(processed_b)
mean_c = sum(processed_c) / len(processed_c)

# Weight initialization (includes red herring weights)
raw_weights = {'temporal': 0.4, 'spatial': 0.3, 'reliability': 0.2, 'legacy_mode': 0.1}

# Misleading weight adjustment path (dead code - not used)
if mean_a > 0.8:
    adjusted_weights = {k: v * 1.1 for k, v in raw_weights.items()}
else:
    adjusted_weights = {k: v * 0.9 for k, v in raw_weights.items()}

# Actual effective weights (override)
effective_weights = {'temporal': 0.5, 'spatial': 0.25, 'reliability': 0.25}

# Simulate diagnostic checksum (irrelevant to final result)
diagnostic_vector = [mean_a, mean_b, mean_c, 1.0]
checksum = sum(math.sin(x) * (i+1) for i, x in enumerate(diagnostic_vector))

# Raw outcome metrics from subsystems (includes decoy entries)
raw_outcomes = {
    'temporal': mean_a,
    'spatial': (mean_b + mean_c) / 2,
    'reliability': min(mean_a, mean_b, mean_c),
    'diagnostic_flag': checksum > 1.0,
    'version': '2.1.0',
    'deprecated_metric': mean_a * mean_b
}

# Metric weights (key input)
metric_weights = [
    ('temporal', effective_weights['temporal']),
    ('spatial', effective_weights['spatial']),
    ('reliability', effective_weights['reliability'])
]

# Decoy function that is never called
def legacy_evaluation(data_map, weights_map):
    total = 0.0
    for key in weights_map:
        if key in data_map:
            total += data_map[key] * weights_map[key] * 0.85
    return total * 1.1

# Core evaluation logic
# Note: Only three keys in metric_weights are used
# All other dictionary entries in raw_outcomes are distractors
def evaluate_performance(weight_list, outcome_dict):
    score = 0.0
    for name, weight in weight_list:
        if name in outcome_dict:
            raw_value = outcome_dict[name]
            # Apply non-linear response curve
            calibrated_value = math.log(1 + raw_value)  # Sigmoid-like dampening
            score += weight * calibrated_value
    return score * 100  # Scale to integer-friendly range

# Critical execution point
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print result for extraction
print(f"Result: {final_score}")