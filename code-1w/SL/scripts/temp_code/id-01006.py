def evaluate_performance(metrics, weights):
    base = 0
    bonus = 0
    penalty = 0
    temp_result = {}
    
    # Irrelevant preprocessing: normalize names (not used in final calculation)
    normalized_keys = [k.lower().replace('_', '') for k in metrics.keys()]
    key_mapping = dict(zip(metrics.keys(), normalized_keys))
    
    # Real computation begins
    weighted_sum = 0
    weight_total = 0
    
    for i, (key, value) in enumerate(metrics.items()):
        if key not in weights:
            continue
        weight = weights[key]
        weighted_sum += value * weight
        weight_total += weight
        
        # Conditional bonus logic (some branches are distractions)
        if value > 85 and 'response' in key:
            bonus += 5
        elif value < 60 and 'error' in key:
            penalty += 3
        
    # Dead code: this block never executes due to fixed conditions but looks relevant
    hypothetical_adjustment = 0
    if False and bonus > 10:
        hypothetical_adjustment = 10
    
    # Distracting intermediate calculations
    average_metric = sum(metrics.values()) / len(metrics) if metrics else 0
    inflated_estimate = average_metric * 1.25  # Not used later
    
    # Actual score computation with red herring variables
    raw_score = weighted_sum / weight_total if weight_total else 0
    adjusted_score = raw_score + bonus - penalty
    
    # Final transformation
    final_score = int(round(adjusted_score * 0.95))
    
    # Additional irrelevant dictionary operations
    temp_result['timestamp'] = '2023-01-01'
    temp_result['version'] = 'v1.0'
    temp_result['debug'] = f'raw={raw_score}, adj={adjusted_score}'
    
    return final_score

# Main execution
if __name__ == '__main__':
    metrics = {
        'response_time_ms': 92,
        'error_rate_pct': 45,
        'throughput_rps': 88,
        'memory_usage_mb': 76
    }
    
    weights = {
        'response_time_ms': 0.4,
        'error_rate_pct': 0.2,
        'throughput_rps': 0.3,
        'memory_usage_mb': 0.1
    }
    
    # Unused auxiliary data structures
    historical_data = [
        {'period': 'Q1', 'value': 85},
        {'period': 'Q2', 'value': 87}
    ]
    
    # Key execution point
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")