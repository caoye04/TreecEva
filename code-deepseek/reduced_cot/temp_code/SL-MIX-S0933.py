import itertools

def process_temperature_readings(temps):
    # Calculate average temperature (distractor - not used in final result)
    avg_temp = sum(temps) / len(temps)
    
    # Find temperature ranges using itertools
    temp_pairs = list(itertools.combinations(temps, 2))
    temp_diffs = [abs(pair[0] - pair[1]) for pair in temp_pairs]
    max_diff = max(temp_diffs) if temp_diffs else 0
    
    # Process temperature thresholds
    threshold = 20
    above_threshold = [t for t in temps if t > threshold]
    below_threshold = [t for t in temps if t < threshold]
    
    # Calculate relevant metrics
    sum_above = sum(above_threshold) if above_threshold else 0
    count_below = len(below_threshold)
    
    # Apply modular arithmetic
    mod_base = 15
    processed_sum = sum_above % mod_base
    
    # Create combined results with some irrelevant intermediate steps
    temp_variance = max_diff * 2  # Not used in final calculation
    adjustment_factor = (count_below + 3) // 2
    
    combined_results = [
        processed_sum,
        len(above_threshold) * 5,  # Distractor value
        adjustment_factor,
        temp_variance  # Redundant calculation
    ]
    
    # Final computation
    final_output = combined_results[2] * adjustment_factor
    
    print(f"Result: {final_output}")
    return final_output

# Main execution
readings = [18, 25, 22, 19, 27, 16, 24]
result = process_temperature_readings(readings)