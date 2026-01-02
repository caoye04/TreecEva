from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    data = [120, 85, 90, 110, 75]
    timestamps = [1, 2, 3, 4, 5]
    
    # Misleading intermediate processing
    temp_buffer = []
    for val in data:
        if val > 80:
            temp_buffer.append(val * 0.95)
        else:
            temp_buffer.append(val * 1.05)
    
    # Actual metric computation
    avg_val = sum(data) / len(data)
    peak = max(data)
    stability = (sum(abs(data[i] - data[i-1]) for i in range(1, len(data))) / len(data))
    
    metrics = {
        'average_throughput': avg_val,
        'peak_load': peak,
        'stability_index': stability,
        'sample_count': len(data)
    }
    return metrics

# Weighting logic with red herring variables
def apply_weights(mets, custom_weights=None):
    default_weights = defaultdict(float)
    default_weights['average_throughput'] = 0.4
    default_weights['peak_load'] = 0.2
    default_weights['stability_index'] = -0.3  # Penalty for instability
    default_weights['sample_count'] = 0.1
    
    # Unused distractor weight
    default_weights['redundant_metric'] = 0.5
    
    if custom_weights:
        for k, v in custom_weights.items():
            default_weights[k] = v
    
    # Compute weighted score
    total_weight = 0.0
    weighted_sum = 0.0
    for key, value in mets.items():
        if key in default_weights:
            total_weight += abs(default_weights[key])  # Use absolute for normalization
            weighted_sum += value * default_weights[key]
    
    # Normalize by total weight magnitude
    normalized_score = weighted_sum / total_weight if total_weight != 0 else 0
    
    # Irrelevant transformation
    adjusted = normalized_score * 1.05
    floor_check = int(normalized_score)
    
    return normalized_score

# Final evaluation combining logical conditions
def evaluate_performance(metrics, weights=None):
    base_score = apply_weights(metrics, weights)
    
    # Conditional bonus/penalty logic
    throughput_ok = metrics['average_throughput'] >= 90
    stable_enough = metrics['stability_index'] < 25
    high_peak = metrics['peak_load'] > 100
    
    bonus_factor = 1.0
    if throughput_ok and stable_enough:
        bonus_factor += 0.1
    elif not stable_enough:
        bonus_factor -= 0.05
    
    if high_peak and throughput_ok:
        bonus_factor += 0.05
    
    # Apply bonus
    enhanced_score = base_score * bonus_factor
    
    # Dead code branch - never executed due to prior logic
    if False and metrics['sample_count'] > 10:
        enhanced_score += 10
    
    # Final clamping
    final_raw = round(enhanced_score, 2)
    
    # Key assignment point
    final_score = int(final_raw + 0.5)  # Round to nearest integer
    return final_score

# Execution flow
metrics_data = collect_metrics()

# Unused derived values (distractors)
shadow_copy = [x * 1.1 for x in [120, 85, 90, 110, 75] if x > 80]
correlation_hint = sum(x * y for x, y in zip([1,2,3], [4,5,6])) / 3

weights_config = {
    'average_throughput': 0.4,
    'peak_load': 0.2,
    'stability_index': -0.3,
    'sample_count': 0.1
}

final_score = evaluate_performance(metrics_data, weights_config)
print(f"Result: {final_score}")