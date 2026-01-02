def process_metrics(data, config):
    baseline = sum(data) / len(data) if data else 0
    adjustments = []
    temp_cache = {}
    outlier_count = 0
    scaling_factor = config.get('scale', 1.0)
    threshold_primary = config['primary']
    threshold_secondary = config.get('secondary', 0)

    for i, val in enumerate(data):
        deviation = abs(val - baseline)
        if deviation > threshold_primary:
            adjustments.append(deviation * scaling_factor)
            temp_cache[i] = deviation
            if val > baseline:
                outlier_count += 1
        elif deviation > threshold_secondary:
            adjustments.append(deviation * 0.5)

    # Irrelevant aggregation (distractor)
    avg_adjustment = sum(adjustments) / len(adjustments) if adjustments else 0
    max_deviation = max(temp_cache.values(), default=0)
    
    # Secondary loop with zip - semi-relevant processing
    weighted_pairs = list(zip(data, [scaling_factor] * len(data)))
    scaled_sum = sum(x * f for x, f in weighted_pairs)

    # Dummy logic to inflate complexity
    status_flags = ['high' if x > baseline else 'low' for x in data]
    flag_summary = {k: status_flags.count(k) for k in set(status_flags)}
    
    # Core computation path
    raw_efficiency = len([x for x in adjustments if x > avg_adjustment])
    penalty = outlier_count * config.get('penalty_per_outlier', 2)
    efficiency_score = raw_efficiency - penalty + int(max_deviation)

    # Dead code branch (distractor)
    if len(flag_summary) > 10:
        efficiency_score *= 1.1

    final_output = efficiency_score
    return final_output

# Input setup
data_input = [12, 15, 9, 18, 14, 22, 8, 16]
thresholds = {
    'primary': 5.0,
    'scale': 1.2,
    'penalty_per_outlier': 2
}

# Execution
efficiency_score = process_metrics(data_input, thresholds)
print(f"Result: {efficiency_score}")