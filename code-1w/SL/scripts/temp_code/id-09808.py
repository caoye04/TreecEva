def process_metrics(log, limit):
    total_entries = len(log)
    valid_count = 0
    temp_sum = 0
    outlier_flags = []
    cumulative_weight = 0.0

    weights = {key: (index + 1) / total_entries for index, key in enumerate(log)}

    adjustment_factor = 1.5 if sum(weights.values()) > 0.5 else 0.5

    for key, value in log.items():
        if isinstance(value, dict) and 'reading' in value:
            raw = value['reading']
            conf = value.get('confidence', 1.0)
            
            # Irrelevant intermediate tracking
            if raw < 10:
                outlier_flags.append(key)
                continue
            
            weighted_val = raw * conf * weights[key]
            temp_sum += weighted_val
            
            significance = 'high' if raw * adjustment_factor > limit else 'low'
            
            # Dead code - never used later
            debug_info = {
                'key': key,
                'adjusted': raw * adjustment_factor,
                'category': significance
            }
            
            valid_count += 1
        else:
            # Misleading path - not triggered in this input
            temp_sum += 1

    if valid_count == 0:
        efficiency_score = 0.0
    else:
        mean_weighted = temp_sum / valid_count
        penalty = len(outlier_flags) * 0.01
        efficiency_score = mean_weighted - penalty

    # Additional irrelevant aggregation
    auxiliary_total = 0
    for i in range(valid_count):
        auxiliary_total += i % 7
    
    # Final computation branch
    final_output = int(efficiency_score * 100) if efficiency_score >= 0 else -1
    
    return final_output

# Input data
entry_log = {
    'sensor_A': {'reading': 12, 'confidence': 0.9},
    'sensor_B': {'reading': 15, 'confidence': 0.95},
    'sensor_C': {'reading': 8, 'confidence': 0.8},  # outlier (skipped)
    'sensor_D': {'reading': 20, 'confidence': 1.0},
    'sensor_E': {'reading': 14, 'confidence': 0.85}
}

threshold = 18.0
result_var = process_metrics(entry_log, threshold)
efficiency_score = result_var
print(f"Result: {efficiency_score}")