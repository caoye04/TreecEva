import math

# Simulated sensor fusion system for environmental monitoring
base_threshold = 72.5
adjustment_factor = 1.8
epsilon = 0.0001
dummy_flag = False
placeholder_data = [0] * 100

# Irrelevant helper (dead function)
def normalize_legacy(values):
    max_val = max(values)
    return [v / max_val for v in values]  # Unused

# Core metric processing
def assess_stability(reading, baseline):
    deviation = abs(reading - baseline)
    if deviation < 5:
        return 90
    elif deviation < 15:
        return 70
    else:
        return 40

def compute_entropy(data_stream):
    # Simplified entropy approximation
    freq_map = {}
    for x in data_stream:
        freq_map[x] = freq_map.get(x, 0) + 1
    entropy = 0
    total = len(data_stream)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log(p) if p > 0 else 0
    return int(entropy * 10)

# Misleading diagnostic block (no side effects)
intermediate_diagnostics = []
for i in range(5):
    temp_diag = (i ** 3) % 7
    intermediate_diagnostics.append(temp_diag)
    if temp_diag == 4:
        dummy_flag = True  # Dead assignment

# Real input data
sensor_readings = [68, 75, 70, 80, 73]
time_series = [10, 12, 15, 12, 11, 10, 9, 12]

current_stability = assess_stability(sensor_readings[4], base_threshold)
noise_level = compute_entropy(time_series)

# Simulated calibration offset (unused but looks important)
calibration_sequence = [round((i * adjustment_factor) % 9, 2) for i in range(20)]
offset_correction = sum(calibration_sequence[:5]) / 5

# Environmental hazard flags
hazard_flags = {
    'temp_spike': any(r > 78 for r in sensor_readings),
    'rising_trend': sensor_readings[-1] > sensor_readings[-2],
    'volatility': len(set(sensor_readings)) > 3
}

# Secondary scoring (partially irrelevant)
legacy_metrics = {
    'peak_deviation': max(abs(r - base_threshold) for r in sensor_readings),
    'duration': len(sensor_readings),
    'consistency': 100 if not hazard_flags['volatility'] else 60
}

# Key metrics for final aggregation
metrics = [
    current_stability,  # From stability assessment
    noise_level * 5,     # Amplified entropy score
    85 if hazard_flags['rising_trend'] else 65,
    90 if not hazard_flags['temp_spike'] else 50
]

# Weight vector with decoy elements
weights_pool = [0.3, 0.1, 0.4, 0.2, 0.15, 0.05]
weights = weights_pool[:4]  # Only first four used

# Red herring: set operations that look critical
observed_levels = set(sensor_readings)
expected_range = set(range(65, 85))
overlap = observed_levels & expected_range
coverage_ratio = len(overlap) / len(expected_range)
penalty_adjustment = 0.95 if coverage_ratio > 0.6 else 0.85

# Conditional expression with distractor logic
scaling_factor = 1.1 if (noise_level > 30 or legacy_metrics['peak_deviation'] > 10) else 1.0
bonus_applied = False
if scaling_factor > 1.0 and coverage_ratio > 0.7:
    metrics.append(20)
    weights.append(0.05)
    bonus_applied = True  # Looks important, rarely affects outcome

# Actual aggregation function
def aggregate_performance(scores, importance_weights):
    if len(scores) != len(importance_weights):
        raise ValueError("Mismatched dimensions")
    
    # Normalize weights
    w_sum = sum(importance_weights)
    normalized_weights = [w / w_sum for w in importance_weights]
    
    # Apply weighted sum
    weighted_sum = sum(s * w for s, w in zip(scores, normalized_weights))
    
    # Final nonlinear transformation
    adjusted = (weighted_sum ** 1.1) * penalty_adjustment  # Uses outer scope variable
    return int(round(adjusted))

# Critical execution point
final_score = aggregate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")