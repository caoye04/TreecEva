import math

# Simulated sensor data and calibration parameters
data_stream = [3.2, 1.8, 4.5, 2.7, 3.6, 5.1, 2.3, 4.4, 3.9, 2.8]
calibration_factor = 1.07
offset_adjustment = -0.15

# Irrelevant auxiliary arrays (distractors)
noise_floor = [0.1, 0.3, 0.2, 0.4]
temp_buffer = [x ** 2 for x in noise_floor]
unused_flags = [True, False, True]
placeholder_matrix = [[0] * 4 for _ in range(3)]

# Weight configuration for scoring (critical)
weights = {'w1': 0.4, 'w2': 0.35, 'w3': 0.25}

# Preprocessing: extract relevant slice with slicing and filtering
data_slice = [x for x in data_stream if x > 2.5][:6]  # First 6 values above threshold

# Decoy function - looks important but unused
def analyze_pattern(seq):
    return sum([seq[i] - seq[i-1] for i in range(1, len(seq))]) if len(seq) > 1 else 0

# Secondary metrics with red herring calculations
peak_value = max(data_slice)
avg_value = sum(data_slice) / len(data_slice)
deviation_scores = [abs(x - avg_value) for x in data_slice]
normalized_rms = math.sqrt(sum([x**2 for x in deviation_scores]) / len(deviation_scores))

# Conditional adjustment based on arbitrary threshold (distraction)
if peak_value > 4.0:
    sensitivity_boost = 1.15
    dummy_calc = sensitivity_boost * 0.05  # Unused downstream
else:
    sensitivity_boost = 1.0

# Real processing begins here — subtle due to surrounding noise
def compute_base_metric(val):
    return math.log(val + 1) if val > 0 else 0

# Apply transformation with conditional expression
typed_metrics = [
    {'type_a': compute_base_metric(x), 'type_b': x * calibration_factor + offset_adjustment}
    for x in data_slice
]

# Extract components for weighted combination
metric_a_total = sum(m['type_a'] for m in typed_metrics) * weights['w1']
metric_b_total = sum(m['type_b'] for m in typed_metrics) * weights['w2']

# Additional derived score using string-based key logic (python idiom)
weight_keys = ''.join(sorted(weights.keys()))
if 'w3' in weight_keys:
    fallback_contribution = len(weight_keys) * 0.5 * weights['w3']
else:
    fallback_contribution = 0.0

# Final aggregation with misleading intermediate variables
aggregation_trace = {
    'part1': metric_a_total,
    'part2': metric_b_total,
    'part3': fallback_contribution,
    'debug_sum': metric_a_total + metric_b_total  # Looks important, not used directly
}

# Key statement: combines all relevant parts into final score
final_score = metric_a_total + metric_b_total + fallback_contribution

# Dead code path — never executed, adds confusion
if __name__ == "__main__":
    print("Debug mode inactive")

# Output target result
print(f"Result: {final_score}")