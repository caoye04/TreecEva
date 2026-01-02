def transform_values(data, key_offset=3):
    # Irrelevant transformation function (dead code path)
    return {k: (v << 2) ^ key_offset for k, v in data.items()}


def preprocess_metrics(raw):
    # Distractor: looks important but unused in final calculation
    cleaned = {}
    for k, v in raw.items():
        if v < 0:
            cleaned[k] = abs(v) * 2
        else:
            cleaned[k] = v + 1
    return cleaned


def calculate_baseline(measures):
    # Misleading intermediate result
    base = 0
    for val in measures.values():
        base += val % 7
    return base * 3  # Never actually used


def adjust_weight(w):
    # Red herring function with no real impact
    if w < 5:
        return w * 1.5
    return w - 2


def evaluate_performance(metrics, importance_weights):
    temp_results = []
    scaling_factor = 1.75
    offset_correction = 0.92
    
    # Real computation begins here
    for key in metrics:
        if key in importance_weights:
            weighted_val = metrics[key] * importance_weights[key]
            
            # Conditional branch affecting outcome
            if weighted_val > 10:
                weighted_val = weighted_val / scaling_factor
            else:
                weighted_val = weighted_val * offset_correction
            
            temp_results.append(weighted_val)
    
    # Key aggregation step
    aggregate = sum(temp_results)
    
    # Decoy manipulation
    for _ in range(2):
        aggregate = (aggregate + 1.1) * 0.98  # Smokescreen
    
    # Final adjustment based on set logic
    unique_caps = {c.upper() for c in metrics.keys() if 'x' in c.lower()}  # Set operation
    if len(unique_caps) >= 2:
        aggregate *= 1.1
    
    # Dictionary-based bonus check
    bonus_table = {'A': 5, 'B': 3, 'C': 1}
    bonus_key = 'A' if aggregate > 25 else 'C'
    aggregate += bonus_table.get(bonus_key, 0)
    
    return round(aggregate, 4)

# Main execution block
if __name__ == '__main__':
    # Input data with meaningful structure
    metric_data = {
        'x_latency': 8,
        'throughput': 12,
        'x_error_rate': 6,
        'reliability': 9
    }
    
    weights = {
        'x_latency': 1.8,
        'throughput': 2.1,
        'x_error_rate': 1.5,
        'reliability': 1.2
    }
    
    # Irrelevant variables and decoy computations
    shadow_metrics = transform_values(metric_data)
    normalized = preprocess_metrics(metric_data)
    baseline = calculate_baseline(metric_data)
    adjusted_weights = {k: adjust_weight(v) for k, v in weights.items()}
    
    # Unused complex structure
    audit_log = [
        {'step': 'init', 'valid': True},
        {'step': 'weight_adj', 'valid': False}
    ]
    
    # Critical execution point
    final_score = evaluate_performance(metric_data, weights)
    
    # Output required format
    print(f"Result: {final_score}")