def calculate_proficiency(data_points):
    # Initial data processing with irrelevant transformations
    raw_metrics = [x * 2 + 1 for x in data_points]
    temporary_buffer = [m % 7 for m in raw_metrics]  # Unused computation
    
    # Core logic with distractor operations
    quality_indicators = []
    adjustment_factor = 3.5
    
    for i, metric in enumerate(raw_metrics):
        if i % 2 == 0:
            processed = metric * 1.5 - adjustment_factor
            quality_indicators.append(processed)
        else:
            processed = metric * 0.8 + adjustment_factor  # Misleading branch
            # This else branch is dead code for even indices
    
    # Multiple irrelevant intermediate calculations
    backup_sum = sum(temporary_buffer) * 2  # Unused
    validation_check = len(quality_indicators) * 10  # Distractor
    
    # Key computation with conditional expression
    threshold = 25
    core_evaluation = sum(quality_indicators) if quality_indicators else 0
    efficiency_ratio = (core_evaluation * 1.2) / len(data_points)
    
    # Final computation chain
    performance_modifier = 8.75
    intermediate_result = efficiency_ratio + performance_modifier
    
    # More distractions
    dummy_calculation = intermediate_result * 0.5  # Unused
    verification_flag = intermediate_result > threshold
    
    # Final assignment
    final_evaluation = intermediate_result * 2.0 if verification_flag else intermediate_result
    
    # Target variable assignment
    composite_score = final_evaluation
    
    print(f"Target result: {composite_score}")
    
# Test execution
sample_data = [12, 8, 15, 6, 10, 4]
calculate_proficiency(sample_data)