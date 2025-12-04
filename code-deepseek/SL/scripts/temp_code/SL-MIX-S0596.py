def calculate_performance(metrics):
    base_score = sum(metrics[:4])
    adjustment = max(metrics[2:5]) - min(metrics[1:4])
    processed_sum = base_score + adjustment
    
    # Distractor operations that don't affect final result
    unused_metrics = metrics[3:6] if len(metrics) > 5 else []
    temp_calc = len(unused_metrics) * 10
    normalization_factor = 3.5
    
    # Semi-relevant intermediate calculation
    scaled_value = (processed_sum * 2) / normalization_factor
    intermediate_result = int(scaled_value)
    
    # Final calculation with rounding
    final_score = round(processed_sum / normalization_factor, 2)
    
    # Print the target result
    print(f"Target result: {final_score}")
    return final_score

# Test data
performance_data = [85, 92, 78, 88, 95, 82]
calculate_performance(performance_data)