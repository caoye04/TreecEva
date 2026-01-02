import math

# Simulated sensor data processing pipeline for environmental monitoring system
def analyze_readings(readings):
    if not readings:
        return 0
    filtered = [x for x in readings if 10 <= x <= 100]
    if len(filtered) < 3:
        return 0
    sorted_vals = sorted(filtered)
    median_val = sorted_vals[len(sorted_vals) // 2]
    return median_val * 0.75

# Legacy function - unused but looks relevant
def legacy_calibrate(x):
    return (x + 5) ** 2 % 97

# Data normalization using various strategies
def normalize(value, method='linear'):
    strategies = {
        'linear': lambda v: v / 100.0,
        'log': lambda v: math.log(v + 1) / 5.0,
        'sqrt': lambda v: math.sqrt(v) / 10.0
    }
    return strategies.get(method, strategies['linear'])(value)

# Complex weighting logic with red herring branches
def apply_weights(data, weights):
    weighted_sum = 0.0
    total_weight = sum(weights.values())
    if total_weight == 0:
        return 0
    
    # Distractor: elaborate but unused transformation
    transformed = {k: math.sin(v) ** 2 + math.cos(v) ** 2 for k, v in weights.items()}  # always 1
    consistency_check = all(0.99 <= val <= 1.01 for val in transformed.values())
    
    for key, value in data.items():
        if key in weights:
            weighted_sum += value * weights[key]
    return weighted_sum / total_weight if total_weight else 0

# Recursive feature extraction (only some branches contribute)
def extract_features(x):
    if x <= 1:
        return 1
    return x + extract_features(x - 2)

# Main evaluation logic
metric_weights = {
    'accuracy': 0.4,
    'stability': 0.3,
    'response_time': 0.2,
    'calibration': 0.1
}

auxiliary_data = [15, 22, 18, 25, 30, 45, 60, 40, 35]
decoy_matrix = [[i * j for j in range(5)] for i in range(5)]  # Unused structure

raw_data = {
    'accuracy': 88,
    'stability': analyze_readings(auxiliary_data),
    'response_time': extract_features(5),
    'calibration': normalize(75, 'log')
}

# Intermediate computations that look important
baseline_offset = sum([len(decoy_matrix[i]) for i in range(len(decoy_matrix))])  # = 25
adjustment_factor = math.floor(math.pi * 10)  # = 31 - misleading constant

# Critical computation path
scaling_lookup = {i: i * 0.1 for i in range(1, 11)}
scaling_factor = scaling_lookup.get(int(raw_data['accuracy'] // 10), 0.5)

preliminary_score = apply_weights(raw_data, metric_weights)

# Final scoring with conditional boost
confidence_boost = 1.1 if raw_data['accuracy'] > 85 and raw_data['stability'] > 20 else 1.0

# Dead code branch - looks like it might affect things
if preliminary_score < 0:
    for i in range(3):
        adjustment_factor *= -1  # Never executed

final_score = preliminary_score * scaling_factor * confidence_boost

# Print result for verification
Result: {final_score}