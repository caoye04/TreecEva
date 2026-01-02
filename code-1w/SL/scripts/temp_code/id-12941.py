def calculate_performance(data):
    # Preprocessing phase with some irrelevant transformations
    normalized = [x * 0.95 for x in data if x > 0]
    offset_values = [n - 5 for n in normalized]
    
    # Real computation begins: filter and aggregate relevant metrics
    filtered = [val for val in normalized if val >= 10]
    
    # Auxiliary tracking variables (some unused)
    peak = max(filtered) if filtered else 0
    baseline = sum(filtered) / len(filtered) if filtered else 0
    deviation_sum = sum((x - baseline) ** 2 for x in filtered)
    variance_proxy = deviation_sum / len(filtered) if filtered else 0
    
    # Simulated weight adjustment (partially misleading)
    weights = {i: 1 + i * 0.1 for i in range(len(filtered))}
    weighted_total = sum(filtered[i] * weights[i] for i in range(len(filtered)))
    scaling_factor = 1.0 if len(filtered) < 5 else 1.25  # conditional scaling
    
    # Distractor block: unrelated statistical attempt
    median_guess = sorted(filtered)[len(filtered)//2] if filtered else 0
    outlier_count = len([x for x in data if x > 50])  # based on original data
    temp_correction = outlier_count * 0.5
    
    # Core logic: performance score based on scaled weighted average and penalty
    raw_score = weighted_total * scaling_factor
    penalty = len([x for x in data if x < 5]) * 2  # penalty from original data
    final_score = int(raw_score - penalty + temp_correction)  # final integral score
    
    # Red herring: this variable is never used
    theoretical_max = sum(x * 2 for x in filtered)
    
    return final_score

# Input dataset with mixed relevance
benchmark_data = [12, -3, 15, 8, 22, 4, 18, 9, 25, 7]

# Additional preprocessing (distractor)
processed_snapshot = benchmark_data[::2]  # slicing every other element
placeholder_map = {k: k * 2 for k in processed_snapshot}

# Key execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")