def analyze_data_quality(measurements):
    raw_scores = [x * 2 for x in measurements if x > 10]
    temp_adjustment = sum(raw_scores) * 0.1  # Not used in final calculation
    
    scaling_factor = 5
    filtered_scores = [score for score in raw_scores if score % scaling_factor == 0]
    
    # Distractor operation - doesn't affect the result
    intermediate_sum = sum(filtered_scores) + len(raw_scores)
    
    final_accuracy = max(filtered_scores) // scaling_factor
    print(f"Result: {final_accuracy}")

# Main execution
measurement_data = [12, 8, 15, 22, 9, 18, 25, 14]
analyze_data_quality(measurement_data)