def analyze_performance(raw_data, config):
    # Preprocessing phase with red herrings
    offset = config.get('offset', 0)
    base_multiplier = config.get('multiplier', 1.0)
    noise_floor = config.get('noise', 0.05)  # Unused in final logic

    adjusted_data = []
    for x in raw_data:
        if x < 0:
            x = abs(x)  # Normalize negatives
        adjusted = (x + offset) * base_multiplier
        adjusted_data.append(round(adjusted, 3))

    # Irrelevant statistical distraction
    mean_val = sum(adjusted_data) / len(adjusted_data) if adjusted_data else 0
    variance_proxy = sum((v - mean_val) ** 2 for v in adjusted_data) / len(adjusted_data) if adjusted_data else 0

    # Core transformation: scaling based on dynamic factor
    scaling_factor = 2.5 if len(adjusted_data) > 3 else 1.8
    scaled_values = [val * scaling_factor for val in adjusted_data]

    # Misleading conditional path (never taken due to data)
    if any(v > 1000 for v in scaled_values):
        scaled_values = [v % 100 for v in scaled_values]  # Dead code branch

    # Threshold logic with distractor variables
    upper_bound = config.get('cap', 999)
    lower_bound = config.get('floor', -999)
    clamped_values = [min(max(v, lower_bound), upper_bound) for v in scaled_values]

    # Use of enumerate and slicing to meet language feature requirement
    indexed_log = []
    for i, val in enumerate(clamped_values):
        if i % 2 == 0:
            indexed_log.append(f"EvenIndex[{i}]={val}")

    # Distractor dictionary operations
    stats_summary = {}
    for i, val in enumerate(scaled_values):
        stats_summary[f'entry_{i}'] = {
            'raw': raw_data[i] if i < len(raw_data) else 0,
            'scaled': val,
            'flagged': val > 50
        }

    # Another irrelevant computation
    total_pairs = 0
    for i in range(len(scaled_values)):
        for j in range(i + 1, len(scaled_values)):
            if scaled_values[i] + scaled_values[j] > 100:
                total_pairs += 1

    return clamped_values, stats_summary


def compute_aggregate(values, criteria):
    aggregate = 0
    weights = criteria.get('weights', [1] * len(values))
    
    # Use of zip to combine values and weights
    for val, weight in zip(values, weights):
        contribution = val * weight
        if contribution > 0:
            aggregate += contribution * 0.9  # Apply damping

    # Additional logic involving modular arithmetic
    if len(values) % 2 == 1:
        aggregate = (aggregate % 87) * 1.5
    else:
        aggregate = aggregate / 1.5

    return int(aggregate)

# Main execution flow
config_settings = {
    'offset': 2,
    'multiplier': 1.1,
    'cap': 200,
    'floor': 0,
    'weights': [1, 2, 1, 3]
}

input_data = [4, 6, 5, 7]

# First processing stage
processed_list, diagnostics = analyze_performance(input_data, config_settings)

# Critical statement
final_score = compute_aggregate(processed_list, config_settings)

print(f"Result: {final_score}")