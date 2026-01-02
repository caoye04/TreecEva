def evaluate_performance(data, importance):
    temp_result = 0
    offset = len(data) % 3
    
    # Irrelevant preprocessing (distractor)
    normalized = {k: v / (sum(data.values()) + 0.1) for k, v in data.items()}
    adjusted = {k: v * 100 for k, v in normalized.items()}
    
    # Actual logic begins
    base_values = list(data.values())
    weight_vals = list(importance.values())
    
    # Slice to ignore first and last elements (actual use of slicing)
    trimmed_base = base_values[1:-1]
    trimmed_weights = weight_vals[1:-1]
    
    intermediate_sum = 0
    for i in range(len(trimmed_base)):
        if i % 2 == 0:
            intermediate_sum += trimmed_base[i] * trimmed_weights[i]
        else:
            intermediate_sum += (trimmed_base[i] + offset) ** 2

    # Red herring calculation (not used in final result)
    avg_normalized = sum(adjusted.values()) / len(adjusted)
    dummy_tracker = [0]
    for _ in range(5):
        dummy_tracker[0] += avg_normalized * 10

    # Final computation
    penalty = 0
    for k in data:
        if 'error' in k:
            penalty += data[k]

    temp_result = intermediate_sum - penalty * 2.5
    
    # Key assignment
    final_score = int(temp_result + 0.5)  # round to nearest integer
    return final_score

# Main execution
metrics = {
    'latency': 45,
    'throughput': 88,
    'error_rate': 12,
    'reliability': 91,
    'failures': 7
}
weights = {
    'latency': 0.8,
    'throughput': 1.2,
    'error_rate': 0.5,
    'reliability': 1.0,
    'failures': 0.3
}

result_var = evaluate_performance(metrics, weights)
final_score = result_var
print(f"Result: {final_score}")