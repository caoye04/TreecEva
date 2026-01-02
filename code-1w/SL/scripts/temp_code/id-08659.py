def process_outcomes(records, limits):
    # Initialize tracking variables
    count_valid = 0
    temp_sum = 0
    penalty_adjustment = 0.0
    intermediate_results = []
    
    # Auxiliary computation: analyze record patterns
    high_value_flags = [r > limits[1] for r in records]
    low_value_flags = [r < limits[0] for r in records]
    
    # Misleading statistical summary (not used in final logic)
    avg_record = sum(records) / len(records) if records else 0
    variance_proxy = sum((x - avg_record) ** 2 for x in records) / len(records) if records else 0
    noise_correction = variance_proxy * 0.1  # Dead-end calculation
    
    # Main filtering logic with slicing and conditional expressions
    trimmed_records = records[1:-1] if len(records) > 2 else records
    for i, val in enumerate(trimmed_records):
        threshold_lower, threshold_upper = limits
        
        # Simulate stateful inspection with distractor counters
        inspection_cycle = (i % 3) + 1
        debug_weight = 1.5 if inspection_cycle == 2 else 1.0  # Unused in result
        
        is_outlier = val < threshold_lower or val > threshold_upper
        is_critical = val > threshold_upper * 1.2
        
        # Conditional scoring with nested logic
        if is_outlier:
            if is_critical:
                penalty_adjustment -= 5
            else:
                penalty_adjustment -= 2
        else:
            count_valid += 1
            temp_sum += val
            intermediate_results.append(val * 0.95)
    
    # Secondary validation using set operations (semi-relevant)
    unique_in_bounds = list(set(intermediate_results))
    sorted_in_bounds = sorted(unique_in_bounds)
    mid_section = sorted_in_bounds[len(sorted_in_bounds)//4 : len(sorted_in_bounds)*3//4] if sorted_in_bounds else []
    bonus_eligible = len(mid_section) >= 2
    
    # Final score composition with conditional expression
    base_score = temp_sum + penalty_adjustment
    final_score = base_score * 1.1 if bonus_eligible else base_score * 0.9
    
    # Irrelevant aggregation for distraction
    total_magnitude = sum(abs(x) for x in records)
    scale_factor = total_magnitude / 100 if total_magnitude > 100 else 1
    scaled_debug = base_score * scale_factor  # Unused
    
    return int(final_score)

# Input data setup
results = [85, 92, 45, 103, 76, 88, 110, 67, 90]
thresholds = [60, 100]

# Execute main logic
target_result = process_outcomes(results, thresholds)
print(f"Result: {target_result}")