def analyze_performance(metrics, thresholds):
    cumulative = 0
    penalty_adjustment = 0
    temp_result = []
    
    # Irrelevant pre-processing: normalize metrics (not all used)
    normalized = {k: v / max(1, sum(metrics.values())) for k, v in metrics.items()}
    
    # Track state across multiple conditions
    for idx, (key, value) in enumerate(metrics.items()):
        if idx % 2 == 0 and value > thresholds.get(key, 0):
            cumulative += value * 0.8
        else:
            cumulative -= value * 0.1

        # Distractor computation: dead logic path due to condition above
        if key == "throughput" and value < 50:
            penalty_adjustment += 10
        elif key == "latency" and value > 100:
            penalty_adjustment += 5

    # Unused helper list - red herring
    temp_result.append(cumulative * 1.1)

    return int(cumulative)


def compute_aggregate(data_list, weights):
    total_weighted = 0
    sum_weights = sum(weights.values())
    aux_log = []
    
    # Use of zip and enumerate together
    for i, (entry, (name, weight)) in enumerate(zip(data_list, weights.items())):
        base_val = analyze_performance(entry['metrics'], entry['thresholds'])
        
        # Real computation branch
        if base_val > 0:
            weighted_val = base_val * weight
            total_weighted += weighted_val
        else:
            weighted_val = base_val * 0.5  # less impactful
            total_weighted += weighted_val

        # Dead code: this list is never used
        aux_log.append(f'Step {i}: {weighted_val}')

        # Extra distraction: slicing unused portion
        if i == len(data_list) - 1:
            snapshot = aux_log[-3:]  # never accessed

    # Final aggregation
    final_value = total_weighted / max(1, sum_weights)
    
    # Additional irrelevant transformation
    if final_value > 50:
        final_value = round(final_value * 0.95)
    else:
        final_value = round(final_value * 1.02)
    
    return int(final_value)

# Main execution
if __name__ == '__main__':
    dataset = [
        {
            'metrics': {'throughput': 60, 'latency': 80, 'accuracy': 95},
            'thresholds': {'throughput': 55, 'latency': 85, 'accuracy': 90}
        },
        {
            'metrics': {'throughput': 40, 'latency': 120, 'accuracy': 88},
            'thresholds': {'throughput': 45, 'latency': 110, 'accuracy': 85}
        }
    ]
    
    importance = {'phase1': 3, 'phase2': 2}
    
    # Misleading variable: looks important but only keys matter
    phase_metadata = {'phase1': 'initial', 'phase2': 'follow-up'}
    
    final_score = compute_aggregate(dataset, importance)
    print(f"Result: {final_score}")