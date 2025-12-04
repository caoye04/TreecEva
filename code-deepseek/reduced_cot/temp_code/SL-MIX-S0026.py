def calculate_validation_metrics():
    raw_readings = [0.82, 0.91, 0.75, 0.88, 0.93, 0.79]
    processed_readings = [x * 100 for x in raw_readings]
    valid_subset = {x for x in processed_readings if x >= 80}
    
    # Main computation path
    primary_score = sum(processed_readings) / len(processed_readings)
    calibrated_score = primary_score * 1.05
    
    # Distractor computations
    outlier_threshold = max(processed_readings) - min(processed_readings)
    adjusted_threshold = outlier_threshold * 0.8
    
    # Secondary computation path
    filtered_scores = [x for x in processed_readings if x >= 85]
    backup_score = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 75.0
    
    # Validation logic
    target_threshold = 85.5
    validated_score = calibrated_score if calibrated_score > 80 else backup_score
    
    # Final assignment with conditional expression
    final_accuracy = validated_score if validated_score >= target_threshold else backup_score
    
    print(f"Result: {final_accuracy}")
    return final_accuracy

calculate_validation_metrics()