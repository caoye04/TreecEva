def calculate_sensor_quality(sensor_readings):
    # Process sensor data with various filters
    raw_values = [45, 67, 23, 89, 34, 78, 56, 12, 91, 64]
    filtered_values = list(filter(lambda x: x > 30 and x < 80, raw_values))
    
    # Calculate quality metrics
    max_reading = max(filtered_values)
    min_reading = min(filtered_values)
    range_value = max_reading - min_reading
    
    # Apply normalization and scaling (distractor operations)
    normalized_values = [val / 100.0 for val in filtered_values]
    scaled_values = [val * 10 for val in normalized_values]
    
    # Sensor calibration factors (some unused)
    calibration_factors = [1.2, 0.8, 1.1, 0.9, 1.3]
    calibration_offset = sum(calibration_factors)  # Distractor calculation
    
    # Process quality scores with conditional logic
    processed_scores = []
    for idx, val in enumerate(scaled_values):
        if val > 4.5:
            processed_scores.append(int(val * 2))
        else:
            processed_scores.append(int(val * 1.5))
    
    # Calculate adjustment based on sensor consistency
    adjustment_factor = 0
    for i in range(len(processed_scores) - 1):
        if abs(processed_scores[i] - processed_scores[i + 1]) < 3:
            adjustment_factor += 1
    
    # Final quality calculation
    final_quality_score = (sum(processed_scores) // len(processed_scores)) + adjustment_factor
    
    # Additional unused metrics (distractors)
    avg_raw = sum(raw_values) / len(raw_values)
    quality_variance = sum((x - avg_raw) ** 2 for x in raw_values) / len(raw_values)
    
    print(f"Result: {final_quality_score}")

# Execute the function
calculate_sensor_quality([])