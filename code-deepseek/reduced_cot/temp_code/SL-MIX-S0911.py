def analyze_data_quality(dataset):
    data_points = [12, 45, 23, 67, 89, 34, 56, 78, 91, 24]
    
    # Initial processing (somewhat relevant but not used in final calculation)
    temp_sum = sum(data_points)
    temp_avg = temp_sum / len(data_points)
    
    # Core quality calculation
    valid_range = data_points[2:8]  # slicing operation
    range_avg = sum(valid_range) / len(valid_range)
    
    # Distractor calculations
    outliers_count = len([x for x in data_points if x > 80])  # not used
    max_deviation = max(data_points) - min(data_points)  # distraction
    
    # Final calculation
    base_score = int(range_avg)
    adjustment = len([x for x in valid_range if x > 50]) * 2
    final_calculation = base_score + adjustment
    
    # Additional unused variable
    quality_variance = sum((x - range_avg) ** 2 for x in valid_range)
    
    quality_score = final_calculation
    print(f"Result: {quality_score}")
    return quality_score

# Execute the analysis
analyze_data_quality([])