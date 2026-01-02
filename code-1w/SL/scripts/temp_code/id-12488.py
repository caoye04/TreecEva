from collections import defaultdict

# Simulate system benchmark data with multiple metrics
def generate_test_metrics():
    raw_data = [78, 85, 92, 64, 77, 81, 96, 73, 88, 79]
    processed = [x ** 0.5 * 1.5 for x in raw_data]  # Distorted normalization
    return {f"task_{i}": processed[i] for i in range(len(processed))}

# Misleading auxiliary function that isn't used in final calculation
def deprecated_analysis(data):
    temp = 0
    for k, v in data.items():
        if "task_" in k:
            temp += (v // 2) % 7
    return temp

# Secondary processing with red herring computations
def apply_filter(metrics):
    filtered = defaultdict(float)
    adjustment = 0.91
    decay = 0.99
    
    for key, value in metrics.items():
        if value > 10:  # Always true
            adjusted_val = value * adjustment
            filtered[key] = round(adjusted_val, 2)
            adjustment *= decay  # Distractor: adjustment drifts but doesn't matter
    
    # Extra computation on unused metric
    outlier_count = sum(1 for v in filtered.values() if v < 11.0)
    scaling_factor = 1.0 + (outlier_count * 0.01)  # Computed but not used
    
    return dict(filtered)

# Core logic hidden among noise
def calculate_performance(data_dict):
    values = list(data_dict.values())
    base_total = sum(values)
    
    # Apply conditional bonus based on pattern recognition
    bonus = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:  # Detect increasing trend
            bonus += 0.5
    
    # Penalty for values below threshold
    penalty = sum(0.2 for v in values if v < 11.5)
    
    # Final performance score — depends only on base_total, bonus, and penalty
    result = base_total + bonus - penalty
    return round(result, 2)

# Main execution flow
benchmark_data = generate_test_metrics()
cached_results = deprecated_analysis(benchmark_data)  # Dead-end call
filtered_data = apply_filter(benchmark_data)
final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")