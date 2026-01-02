def analyze_efficiency(data):
    # Irrelevant preprocessing
    temp_data = [x for x in data if x > 0]
    offset = sum(temp_data) // len(temp_data) if temp_data else 0
    adjusted = [x - offset for x in data]

    # Distractor: unused transformation
    transformed = list(map(lambda y: y ** 0.5 if y > 0 else 0, adjusted))

    # Actual relevant computation
    positive_count = len([x for x in adjusted if x > 0])
    negative_impact = sum(-x for x in adjusted if x < 0)
    return positive_count, negative_impact


def compute_baseline(ref_values):
    base = 0
    for val in ref_values:
        if val % 3 == 0:
            base ^= val  # Bitwise distraction with partial relevance
    return base

# Main logic
metrics = [85, 92, 78, 63, 96]
weights = [0.2, 0.3, 0.15, 0.1, 0.25]

# Dead code path (not used)
if len(metrics) > 10:
    fallback = sum(metrics) / 100
    scaling_factor = 1.5
else:
    scaling_factor = 1.0  # This is misleading but overwritten later

scaling_factor = 0.1  # Actual scaling factor

# Simulate auxiliary analysis with side irrelevant results
aux_data = [70, 88, None, 95, 60]
filtered_aux = [x for x in aux_data if isinstance(x, int) and x >= 60]
dummy_analysis = analyze_efficiency(filtered_aux)

# Unused dictionary structure (distractor)
status_map = {
    'high': [x for x in metrics if x >= 90],
    'medium': [x for x in metrics if 70 <= x < 90],
    'low': [x for x in metrics if x < 70]
}

# Core weighted calculation
weighted_sum = sum(metric * weight for metric, weight in zip(metrics, weights))

# Secondary adjustment using bitwise and arithmetic
baseline_ref = compute_baseline([3, 6, 9, 12])
adjustment = (weighted_sum % 7) ^ baseline_ref  # XOR with modulo result

# Final score computation
raw_performance = weighted_sum + adjustment

# Additional red herring: string processing that doesn't affect result
log_entry = "Performance run complete: {} metrics processed".format(len(metrics))
log_valid = 'complete' in log_entry and 'error' not in log_entry

# Final scaling
final_score = int(raw_performance * scaling_factor)  # Key assignment point

print(f"Result: {final_score}")