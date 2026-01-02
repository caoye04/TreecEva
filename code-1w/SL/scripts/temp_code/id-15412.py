def analyze_component(reading, threshold=75):
    return reading > threshold

# Irrelevant helper function (dead code path)
def calculate_baseline(readings):
    return sum(readings) / len(readings) if readings else 0

# Distractor variables
temp_log = [68, 72, 77, 81, 65]
baseline_ref = 74.6
dummy_mask = [True, False, True, False, True]

# Lambda for dynamic weighting (relevant)
adaptive_weight = lambda x: 0.5 + (x % 4) * 0.1

# Sensor metrics with mixed relevance
sensor_a = [88, 92, 76, 85]
sensor_b = [60, 70, 78, 80]
sensor_c = [90, 85, 88, 91]

# Extract key performance indicators
kpi_a = sum(1 for val in sensor_a if val >= 80)
kpi_b = sum(1 for val in sensor_b if val >= 75)
kpi_c = sum(1 for val in sensor_c if val >= 85)

# Irrelevant transformation
shifted_vals = [v * 1.05 for v in sensor_c]
offset_correction = sum(shifted_vals) - sum(sensor_c)

# Weight assignment with decoy logic
weights_raw = [len(sensor_a), len(sensor_b), kpi_b]
normalized_weights = [w / sum(weights_raw) for w in weights_raw]

# Actual weight adjustment using lambda (critical)
weights = [adaptive_weight(i + 2) for i in range(len(normalized_weights))]

# Performance metrics with red herring components
metrics = {
    'stability': kpi_a,
    'response_time': kpi_b,
    'precision': kpi_c,
    'redundancy_check': sum(dummy_mask),  # Irrelevant metric
    'calibration_offset': baseline_ref      # Unused field
}

# Decoy function that is never called
def validate_integrity(data_stream):
    checksum = 0
    for d in data_stream:
        checksum ^= d
    return checksum % 10 == 0

# Conditional branch with misleading intermediate
if metrics['response_time'] < 3:
    fallback_mode = True
    primary_active = False
else:
    fallback_mode = False
    primary_active = True  # This is distracting but unused later

# Complex evaluation with nesting and lambdas
evaluate_performance = lambda m, w: (
    (m['stability'] * w[0]) + 
    (m['response_time'] * w[1]) + 
    (m['precision'] * w[2])
) * (1.1 if m['stability'] >= 3 else 1.0)

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")