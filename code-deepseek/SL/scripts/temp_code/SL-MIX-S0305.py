def calculate_performance_score(data_points):
    base_score = sum(data_points) // len(data_points)
    processed_data = {}
    
    # Process valid data points
    valid_points = [x for x in data_points if x > 0]
    processed_data["valid_count"] = len(valid_points)
    
    # Distractor calculations that don't affect final result
    temp_sum = sum(valid_points)
    processed_data["avg_valid"] = temp_sum / processed_data["valid_count"] if valid_points else 0
    
    # Adjustment factor based on data characteristics
    max_point = max(data_points) if data_points else 0
    min_point = min(data_points) if data_points else 0
    range_factor = (max_point - min_point) % 5
    
    # Red herring - appears relevant but unused in final calculation
    outlier_count = len([x for x in data_points if x > 50])
    
    # Key adjustment logic
    adjustment_factor = range_factor * 3 if len(data_points) > 3 else 2
    
    # Final score calculation
    final_score = processed_data["valid_count"] + adjustment_factor
    
    print(f"Target result: {final_score}")
    return final_score

# Test data
sample_data = [12, 25, 8, 45, 3, 18, 32, 7, 55, 2]
result = calculate_performance_score(sample_data)