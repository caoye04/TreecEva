def evaluate_performance(data, limits):
    baseline = 100
    adjustment = 0
    temp_sum = 0
    
    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    processed_entries = []
    
    for key in data:
        if key in limits:
            value = data[key]
            threshold = limits[key]
            
            # Real logic branch
            if value > threshold * 1.2:
                adjustment += 10
            elif value < threshold * 0.8:
                adjustment -= 15
            else:
                adjustment += 5
            
            # Distractor computation (not used later)
            temp_sum += value ** 0.5
            
            # Semi-relevant but not critical tracking
            processed_entries.append(key)
        else:
            # Dead code path (misleading)
            outlier_count += 1

    # Set operations to satisfy language-specific feature requirement
    expected_keys = {'response_time', 'throughput', 'error_rate', 'latency'}
    actual_keys = set(data.keys())
    missing = expected_keys - actual_keys
    extra = actual_keys - expected_keys
    
    # Dictionary operation for normalization (semi-distractor)
    normalized = {k: round(v / 10, 2) for k, v in data.items() if k != 'debug_flag'}
    
    # Core result computation (depends on adjustment only)
    base_performance = 75
    final_score = base_performance + adjustment
    
    # Unused derived metrics (distractors)
    avg_normalized = sum(normalized.values()) / len(normalized) if normalized else 0
    penalty_factor = len(missing) * 3
    final_score -= penalty_factor  # This line looks important but is overridden
    
    # Critical override based on specific condition
    if 'latency' in data and data['latency'] < 40:
        final_score += 20  # Key boost for low latency
    
    # Final override that nullifies earlier penalty (shows interdependency)
    if len(extra) == 0 and len(missing) == 0:
        final_score += 10
    
    return final_score

# Main execution
metric_data = {
    'response_time': 120,
    'throughput': 95,
    'error_rate': 0.02,
    'latency': 35,
    'debug_flag': 1  # Extra key (triggers extra set)
}

thresholds = {
    'response_time': 100,
    'throughput': 100,
    'error_rate': 0.05,
    'latency': 50
}

# Trigger function call
final_score = evaluate_performance(metric_data, thresholds)
print(f"Target result: {final_score}")