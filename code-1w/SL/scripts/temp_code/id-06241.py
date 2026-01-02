import itertools

def analyze_metrics(values, threshold):
    above_threshold = [v for v in values if v > threshold]
    squared_devs = [(x - 10) ** 2 for x in values]  # distractor: not used later
    return len(above_threshold)

def calculate_performance(data):
    flat_data = list(itertools.chain.from_iterable(data))
    
    # Distractor variables and computations
    temp_stats = {
        'max_val': max(flat_data),
        'min_val': min(flat_data),
        'range_val': max(flat_data) - min(flat_data)
    }
    
    outliers = [x for x in flat_data if x > 15]  # semi-relevant but not critical
    filtered_data = [x for x in flat_data if x <= 15]
    
    # Key logic chain
    group_sums = [sum(group) for group in data]
    avg_group_sum = sum(group_sums) / len(group_sums)
    
    # Conditional expression with slicing
    adjustment_factor = 1.5 if len(outliers) > 3 else 0.8
    adjusted_avg = avg_group_sum * adjustment_factor
    
    # Final computation using relevant path
    base_score = sum(filtered_data) // len(filtered_data)
    penalty = len([g for g in group_sums if g < 20]) * 2
    final_score = int(base_score - penalty + adjusted_avg // 4)
    
    # Dead code path (distractor)
    if False:
        fallback = sum(squared_devs) / len(squared_devs)
        final_score += fallback
    
    return final_score

# Simulated benchmark data
benchmark_data = [
    [5, 7, 8, 12],
    [9, 11, 3, 4],
    [10, 10, 10],
    [16, 2, 14, 1]  # includes outlier 16
]

# Irrelevant pre-processing (distractor)
processed_flags = [len(row) >= 4 for row in benchmark_data]
summary_flag = any(processed_flags)

intermediate_result = analyze_metrics([item for row in benchmark_data for item in row], threshold=5)

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")