def calculate_quality_scores(measurements):
    # Redundant preprocessing step (distractor)
    processed = [x * 2 for x in measurements if x > 0]
    temp_sum = sum(processed)  # Unused variable
    
    # Main quality calculation
    valid_measures = [m for m in measurements if m >= 10]
    if not valid_measures:
        return 0  # Dead code path in this execution
    
    # Distractor calculations
    max_val = max(measurements) * 3.14
    min_val = min(measurements) / 2.0
    avg_val = sum(measurements) / len(measurements)
    
    # Core logic with bitwise operations
    quality_threshold = 25
    high_quality = [m for m in valid_measures if m > quality_threshold]
    
    # Lambda function with combinatorics
    quality_score = (lambda x: (len(x) * (sum(x) // len(x))) >> 2)(high_quality)
    
    # More distractors
    adjustment = (max_val - min_val) * 0.1
    unused_metric = quality_score + int(adjustment)
    
    # Final aggregation with bit manipulation
    base_score = quality_score
    parity_check = base_score & 1
    scaled_result = base_score * (3 if parity_check else 4)
    
    # Misleading intermediate result
    intermediate = scaled_result + len(measurements)
    
    # Actual final calculation
    aggregate_result = scaled_result - (len(high_quality) * 2)
    
    # Distractor assignment
    final_metric = aggregate_result
    
    print(f"Result: {final_metric}")
    return final_metric

# Test data
sensor_readings = [15, 32, 8, 45, 12, 28, 50, 6]
calculate_quality_scores(sensor_readings)