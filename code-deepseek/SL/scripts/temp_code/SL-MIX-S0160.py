def calculate_data_quality(data_points):
    # Irrelevant preprocessing calculations
    temp_sum = sum(data_points)
    mean_value = temp_sum / len(data_points)
    
    # Distractor calculations that don't affect final result
    variance = sum((x - mean_value) ** 2 for x in data_points) / len(data_points)
    std_dev = variance ** 0.5
    
    # Main logic path with misleading intermediate values
    processed_data = [x * 2 if x > 5 else x - 1 for x in data_points]
    processed_sum = sum(processed_data)
    
    # Dead code path that's never executed
    if processed_sum > 1000:
        bonus_points = 50
    else:
        bonus_points = 0
    
    # More irrelevant computations
    filtered_data = [x for x in processed_data if x % 2 == 0]
    filtered_sum = sum(filtered_data)
    
    # Key calculations that actually matter
    base_total = sum(x for x in processed_data if x < 15)
    adjustment_factor = len([x for x in processed_data if x > 10]) * 3
    
    # Misleading intermediate result
    intermediate_result = base_total + adjustment_factor
    
    # Critical execution point
    correction_factor = (len(data_points) * 2) ^ 5  # XOR operation
    adjusted_total = base_total - 7
    
    # Final assignment (this is what matters)
    final_score = adjusted_total + correction_factor
    
    # More dead code that doesn't affect final_score
    unused_calculation = intermediate_result * 2
    redundant_check = final_score > 50
    
    print(f"Result: {final_score}")

# Execute the function
data_samples = [3, 8, 12, 6, 9, 15, 4, 11]
calculate_data_quality(data_samples)