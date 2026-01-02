def analyze_component(metrics, weights):
    weighted_sum = 0
    normalization_factor = sum(weights.values())
    temp_result = 0

    for key in metrics:
        if key in weights:
            weighted_sum += metrics[key] * weights[key]
        else:
            temp_result += metrics[key] ** 0.5  # Irrelevant computation

    adjusted = weighted_sum / normalization_factor if normalization_factor != 0 else 0
    
    # Dead code path (never executed due to logic)
    if len(metrics) > 100:
        adjusted *= 1.1

    return adjusted


def validate_inputs(data):
    # Semi-relevant validation that doesn't affect final result
    if not isinstance(data, dict) or 'base' not in data:
        return False
    for k, v in data.items():
        if not isinstance(v, (int, float)) or v < 0:
            return False
    return True


def calculate_performance(raw_data):
    # Main logic with distractions
    base_value = raw_data.get('base', 0)
    offset_correction = raw_data.pop('offset', 0)  # Not used later

    intermediate_metrics = {
        'throughput': base_value * 1.5,
        'latency': base_value / 2.0,
        'memory': base_value + 10
    }

    weights = {'throughput': 0.4, 'latency': 0.35, 'memory': 0.25}
    score_raw = analyze_component(intermediate_metrics, weights)

    # Distractor: complex slicing and set operations with no impact
    history_log = [i * 2 for i in range(10)]
    recent_entries = history_log[5:8:1]
    unique_set = set(recent_entries)
    unique_set.add(999)  # Unused modification

    # Additional irrelevant dictionary manipulation
    metadata_cache = {f'entry_{i}': i * 3 for i in range(5)}
    metadata_cache.update({'temp_key': sum(unique_set)})

    # Final adjustment using integer division and logical condition
    adjustment_factor = 2 if score_raw > 50 else 1
    rough_estimate = int(score_raw // adjustment_factor)  # Integer division

    # Actual answer derivation
    final_score = int((rough_estimate * 1.8) + 7)

    return final_score

# Simulated benchmark input
dataset_snapshot = {
    'base': 42,
    'offset': 5,
    'extra_flag': True
}

# Validate call (does nothing critical)
valid = validate_inputs(dataset_snapshot)

# Key execution point
final_score = calculate_performance(dataset_snapshot)
print(f"Result: {final_score}")