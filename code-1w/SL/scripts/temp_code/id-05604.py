def analyze_metrics(data_map):
    temp_results = {}
    cumulative = 0
    adjustment_factor = 0.85
    
    for key, values in data_map.items():
        if len(values) == 0:
            temp_results[key] = 0
            continue
        
        base_sum = sum(v ** 0.5 for v in values if v > 0)
        penalty = len([v for v in values if v < 5]) * 0.5
        adjusted = base_sum - penalty
        
        # Distractor: irrelevant transformation
        shadow_value = (adjusted * 1.1) % 7
        
        temp_results[key] = max(adjusted, 0)
        
    # Irrelevant aggregation
    total_keys = len(temp_results)
    dummy_aggregate = sum(v * 0.1 for v in temp_results.values())
    
    return temp_results


def compute_weights(size):
    # Dead function - not used but adds distraction
    weights = [0.1 * i for i in range(size)]
    normalized = [w / sum(weights) for w in weights]
    return normalized

def calculate_performance(raw_data):
    processed = analyze_metrics(raw_data)
    
    # Real computation path
    score_parts = []
    scaling_constant = 1.2
    offset = 10
    
    for k, val in processed.items():
        if k.startswith('metric_'):
            # Only metrics with prefix contribute
            contribution = val * scaling_constant + offset
            score_parts.append(contribution)
    
    # Final accumulation
    raw_total = sum(score_parts)
    
    # Distractor: unused smoothing
    smoothed = raw_total * 0.95
    fluctuation_check = abs(smoothed - raw_total) < 5
    
    final_score = int(raw_total)  # Critical assignment point
    
    # Additional red herring variables
    audit_log = {'entries': 5, 'valid': True, 'score_snapshot': final_score - 5}
    metadata_enrichment = {"version": "2.1", "calibration": 0.99}
    
    return final_score

# Main execution
benchmark_data = {
    'metric_a': [16, 9, 25, 4],
    'metric_b': [36, 1, 100],
    'auxiliary_debug': [1, 2, 3],  # Not included in final score
    'metric_c': [49, 64, 0, 81],
    'temp_diagnostic': [],
    'metric_d': [121]
}

result = calculate_performance(benchmark_data)
final_score = result
print(f"Result: {final_score}")