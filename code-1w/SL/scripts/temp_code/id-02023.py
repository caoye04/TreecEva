def evaluate_performance(metrics, weights):
    # Initialize various tracking variables (some are distractions)
    total = 0.0
    normalized = []
    temp_sum = 0  # distractor
    scaling_factor = 1.5  # not actually used in core logic
    adjustment = 0.1   # red herring

    # Normalize metrics using min-max scaling (only some are relevant)
    min_val = min(metrics)
    max_val = max(metrics)
    for val in metrics:
        if max_val != min_val:
            norm_val = (val - min_val) / (max_val - min_val)
        else:
            norm_val = 0.5
        normalized.append(norm_val)

    # Apply weights with conditional boost for high-efficiency indicators
    weighted_sum = 0
    efficiency_boost = 0
    for i, (norm, w) in enumerate(zip(normalized, weights)):
        if norm > 0.7:
            efficiency_boost += 0.05 * w
        weighted_sum += norm * w

    # Simulate threshold-based bonus
    above_threshold = sum(1 for m in metrics if m >= 80)
    bonus = 0
    if above_threshold >= 2:
        bonus = 5.0

    # Secondary validation via string-encoded rules (using string methods)
    rule_string = "threshold@80|bonus_active|weight_adjust@off"
    rules = rule_string.split('|')
    parsed_rules = {r.split('@')[0]: r.split('@')[1] if '@' in r else True for r in rules}

    if parsed_rules.get('threshold').isdigit():
        threshold_value = int(parsed_rules['threshold'])
        if threshold_value == 80:
            bonus += 2.0  # additional red herring, doesn't apply directly

    # Distractor: unused loop over zipped indices and values
    debug_info = []
    for idx, (m, w) in enumerate(zip(metrics, weights)):
        log_entry = f"Metric_{idx}: {m} * {w}"
        debug_info.append(log_entry)
    
    # Final computation - only weighted_sum and original bonus matter
    final_score = weighted_sum * 100 + bonus

    return final_score

# Main execution
metrics_data = [85, 90, 78, 92]
weights_config = [0.3, 0.4, 0.2, 0.1]

# Irrelevant pre-processing (distractor)
processed_metrics = [m + 1 if m < 80 else m for m in metrics_data]
dropped = [w * 0.9 for w in weights_config]  # unused

final_score = evaluate_performance(metrics_data, weights_config)
print(f"Result: {final_score}")