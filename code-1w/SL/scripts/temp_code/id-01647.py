def evaluate_performance(metrics, limits):
    score = 0
    penalty_adjustment = 0.0
    
    # Irrelevant preprocessing: normalize names (not used in scoring)
    normalized_keys = [k.strip().lower() for k in metrics.keys() if 'temp' not in k]
    temp_data = {k: v for k, v in metrics.items() if 'temp' in k}
    
    # Real logic begins: assess performance against thresholds
    exceeded_count = 0
    for key, value in metrics.items():
        base_limit = limits.get(key, 100)
        if value > base_limit * 1.1:  # 10% tolerance exceeded
            score += 10
            exceeded_count += 1
        elif value > base_limit:
            score += 5
        else:
            score += 2
    
    # Distractor: unused conditional block (dead code path)
    if exceeded_count > 10:
        emergency_override = True
        backup_scores = sorted([v for v in metrics.values()])
        midpoint = len(backup_scores) // 2
        median_val = (backup_scores[midpoint] + backup_scores[~midpoint]) / 2

    # Additional distraction: complex but irrelevant slicing and set operation
    history_log = list(metrics.values())[-5:]  # last 5 metric values
    unique_recent = list(set(history_log))
    unique_recent.sort()
    middle_slice = unique_recent[1:-1] if len(unique_recent) > 2 else unique_recent
    
    # Secondary scoring mechanism that doesn't override primary
    auxiliary_score = 0
    for val in middle_slice:
        if val > 80:
            auxiliary_score += 3
    
    # Final aggregation uses only primary score with minor adjustment
    stability_factor = 1.0
    if len(metrics) % 2 == 0:
        stability_factor = 0.95
    
    final_raw = score * stability_factor
    
    # Rounding to 2 decimal places
    final_score = round(final_raw, 2)
    
    return final_score

# Main execution
metric_data = {
    'throughput': 120,
    'latency': 95,
    'bandwidth': 110,
    'jitter': 45,
    'packet_loss': 2,
    'temp_01': 75,
    'temp_02': 78
}

thresholds = {
    'throughput': 100,
    'latency': 100,
    'bandwidth': 100,
    'jitter': 50,
    'packet_loss': 5
}

intermediate_result = sum(metric_data.values()) / len(metric_data)  # distractor computation
offset_correction = max(metric_data.values()) - min(metric_data.values())  # unused offset

final_score = evaluate_performance(metric_data, thresholds)
print(f"Result: {final_score}")