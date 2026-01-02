def evaluate_performance(metrics, weights):
    # Initialize various tracking variables (some are distractions)
    temp_buffer = []
    running_total = 0
    adjustment_factor = 1.25
    decay_rate = 0.9
    cumulative = 0
    
    # Irrelevant pre-processing: simulate data smoothing (not used in final logic)
    for i in range(len(metrics)):
        if i > 0:
            smoothed = (metrics[i] + metrics[i-1]) * 0.5
            temp_buffer.append(smoothed * decay_rate)

    # Real computation begins: weighted sum using dictionary keys
    weighted_sum = 0.0
    for key in weights.keys():
        if key in metrics:
            weighted_sum += metrics[key] * weights[key]

    # Additional irrelevant transformation on a copy of metrics (dead-end path)
    shifted_metrics = {k: v << 1 for k, v in metrics.items() if isinstance(v, int)}
    overflow_check = sum(shifted_metrics.values()) >> 3

    # Use slicing to extract part of an intermediate list (semi-relevant)
    samples = [weighted_sum * adjustment_factor] * 5
    samples[2] = samples[2] + 10
    mid_samples = samples[1:4]  # slicing operation
    running_total += sum(mid_samples)

    # Final decision logic with bitwise interference (only one branch matters)
    control_flag = 0b1010 ^ 0b1100  # XOR result is 0b0110 = 6
    if control_flag & 0b0010:  # checks if second bit is set
        cumulative += running_total / 2
    else:
        cumulative -= 5  # this runs because 6 & 2 = 2 (truthy)

    # Core answer derivation
    base_result = weighted_sum
    penalty = len(temp_buffer) - len(metrics)  # this will be 0
    final_score = int(base_result - penalty + (cumulative % 7))

    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    metrics = {
        'accuracy': 88,
        'latency': 45,
        'throughput': 60,
        'energy': 30
    }
    
    weights = {
        'accuracy': 0.4,
        'latency': 0.1,
        'throughput': 0.3,
        'energy': 0.2
    }

    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Print result
    print(f"Target result: {final_score}")