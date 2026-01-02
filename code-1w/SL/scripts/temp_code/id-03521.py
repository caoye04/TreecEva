def evaluate_performance(metrics, weights):
    # Initialize intermediate tracking variables
    base_score = 0
    adjustment_factor = 1.0
    temp_result = 0
    
    # Irrelevant diagnostic counters (distractors)
    computation_steps = 0
    validation_checks = 0
    
    # Simulate data preprocessing (semi-relevant)
    processed_metrics = {}
    for key, value in metrics.items():
        if key == 'latency':
            processed_metrics[key] = max(0, 100 - value)  # Invert latency penalty
        elif key == 'throughput':
            processed_metrics[key] = min(value, 90)  # Cap throughput
        elif key == 'accuracy':
            processed_metrics[key] = value * 100  # Normalize accuracy
        else:
            processed_metrics[key] = value  # Pass-through

    # Begin core evaluation logic
    for metric_name, raw_value in processed_metrics.items():
        if metric_name in weights:
            weight = weights[metric_name]
            contribution = raw_value * weight
            
            # Apply conditional bonus using bitwise logic (relevant)
            if raw_value > 80 and (int(raw_value) & 1):  # High performance and odd value
                contribution += 5 * weight
            
            # Accumulate score with modular adjustment
            base_score += contribution % 97  # Modular arithmetic for stability
            computation_steps += 1  # Distractor: not used later
    
    # Additional irrelevant validation chain
    if base_score > 50:
        validation_checks += 1
    if base_score > 75:
        validation_checks += 1
    if base_score > 90:
        validation_checks += 1

    # Secondary adjustment using logical XOR on binary flags
    flag_a = int(base_score > 60)
    flag_b = int(base_score < 85)
    xor_flag = flag_a ^ flag_b  # True if only one condition is met
    
    if xor_flag:
        adjustment_factor = 1.1
    else:
        adjustment_factor = 0.95

    # Final scoring with distractor-influenced calculation
    temp_result = base_score * adjustment_factor
    
    # Dead code path - never reached due to logic above (misleading)
    if validation_checks == 0:
        temp_result *= 0.8
    
    # Actual final computation
    final_score = int(temp_result + 0.5)  # Round to nearest integer
    
    return final_score

# Main execution
metrics = {
    'latency': 12,
    'throughput': 88,
    'accuracy': 0.87,
    'reliability': 76
}

weights = {
    'latency': 0.3,
    'throughput': 0.25,
    'accuracy': 0.4,
    'reliability': 0.05
}

# Execute and print result
result_value = evaluate_performance(metrics, weights)
print(f"Result: {result_value}")