def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [round((m - min(metrics)) / (max(metrics) - min(metrics)) * 100) for m in metrics]
    
    # Semi-relevant filtering (only some values used later)
    filtered_metrics = [m for m in metrics if m > thresholds[0]]

    # Tracking state across iterations (used in final calculation)
    cumulative_shift = 0
    temp_results = []
    
    for i, val in enumerate(filtered_metrics):
        if i % 2 == 0:
            shifted = val + (i * 2)
        else:
            shifted = val - i
        cumulative_shift += shifted
        temp_results.append(shifted)

    # Dead code path (never executed under current inputs)
    if len(metrics) > 100:
        fallback = sum(temp_results) / len(temp_results)
    else:
        fallback = 0  # Unused

    # Complex but relevant aggregation logic
    paired_data = list(zip(temp_results[:-1], temp_results[1:]))
    differences = [abs(a - b) for a, b in paired_data]
    
    # Misleading intermediate computation (looks important but unused)
    avg_difference = sum(differences) / len(differences) if differences else 0
    peak_fluctuation = max(differences) if differences else 0

    # Core logic contributing to answer
    base_score = sum(temp_results)
    penalty = 0
    for diff in differences:
        if diff > thresholds[1]:
            penalty += diff // 2

    return base_score - penalty


def compute_aggregate(data_set, config):
    # Extraneous preprocessing
    processed = [x for x in data_set if x >= config['min_val']]
    processed = [x for x in processed if x <= config['max_val']]

    # Secondary distractor: histogram-like counting (unused)
    counts = {}
    for item in processed:
        bucket = item // 10
        counts[bucket] = counts.get(bucket, 0) + 1

    # Main analysis pipeline
    stage_one = analyze_performance(processed, [config['thresh_a'], config['thresh_b']])
    adjustment_factor = len(processed) % 7

    # Final scoring with subtle arithmetic
    raw_final = stage_one + adjustment_factor * config['bonus_multiplier']
    
    # Normalize to integer score
    final_score = int(raw_final)

    # Red herring: complex conditional that doesn't trigger
    if all(x < 50 for x in processed) and len(processed) > 50:
        final_score *= 2  # Never reached

    return final_score

# Input setup
metrics_input = [45, 67, 33, 89, 72, 55, 41, 78, 64, 59, 38, 81]
config_params = {
    'min_val': 30,
    'max_val': 90,
    'thresh_a': 40,
    'thresh_b': 25,
    'bonus_multiplier': 3
}

# Execution
final_score = compute_aggregate(metrics_input, config_params)
print(f"Result: {final_score}")