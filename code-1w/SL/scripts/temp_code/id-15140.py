def calculate_performance(data):
    # Preprocessing step with distractor variables
    scaling_factor = 1.2
    offset_correction = 0.8
    temp_buffer = []
    
    # Irrelevant statistical measures (distractors)
    mean_val = sum(data) / len(data) if data else 0
    variance_proxy = sum((x - mean_val) ** 2 for x in data) / len(data) if data else 0
    outlier_threshold = mean_val + 2 * (variance_proxy ** 0.5)

    # Filter relevant high-performance segments
    filtered_segments = [x for x in data if x > mean_val]
    
    # Use lambda to compute dynamic weight (required python feature)
    adaptive_weight = lambda x: 1.5 if x > outlier_threshold else 1.1
    
    weighted_sum = 0
    adjustment_counter = 0  # Semi-relevant tracking
    
    for val in filtered_segments:
        if val < 0:
            continue  # Skip invalid entries
        weight = adaptive_weight(val)
        weighted_sum += val * weight
        
        # Dead code path (distractor)
        if val == 0:
            adjustment_counter += 1
            redundant_calc = scaling_factor * offset_correction

    # Secondary processing with red herring computation
    phantom_score = sum(x ** 0.5 for x in data if x > 0) * 0.5
    debug_trace = [mean_val, variance_proxy, outlier_threshold]  # Not used later

    # Core logic: final score depends only on weighted_sum and fixed base
    base_performance = 100
    final_score = base_performance + (weighted_sum / len(filtered_segments) if filtered_segments else 0)
    
    # Early return simulation (not triggered, but adds structure)
    if not data:
        return 0
        
    return final_score

# Input data
benchmark_data = [85, 90, 78, 92, 88, 76, 95, 89]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")