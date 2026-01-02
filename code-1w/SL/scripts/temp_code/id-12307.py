def calculate_performance(data_map):
    base_multiplier = 1.5
    adjustment_factor = 0.9
    temp_offset = 0
    
    # Irrelevant pre-processing (distractor)
    outlier_flags = {k: (v > 800) for k, v in data_map.items()}
    temp_offset += sum(1 for flag in outlier_flags.values() if flag)

    # Core logic with conditional expressions and dictionary operations
    performance_ratings = {
        k: (v * base_multiplier if v < 500 else v * adjustment_factor) 
        for k, v in data_map.items()
    }
    
    # Additional distraction: unused transformation
    inverted_map = {k: 1 / (v + 1) for k, v in data_map.items()}
    lambda_filter = lambda x: x > 400
    filtered_keys = [k for k, v in performance_ratings.items() if lambda_filter(v)]

    # State tracking with semi-relevant computation
    cumulative_shift = 0
    for key in sorted(filtered_keys):
        if performance_ratings[key] > 450:
            cumulative_shift += 10
        else:
            cumulative_shift -= 5

    # Final score depends only on aggregated rating, not shift
    total_rating = sum(performance_ratings.values())
    final_score = int(total_rating / len(performance_ratings)) + cumulative_shift // 2
    
    # But shift contribution cancels due to integer division behavior
    return final_score

# Benchmark dataset
benchmark_data = {
    'module_a': 320,
    'module_b': 780,
    'module_c': 410,
    'module_d': 615,
    'module_e': 290
}

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")