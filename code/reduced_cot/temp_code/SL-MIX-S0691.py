def calculate_student_performance():
    # Student marks data
    marks = [85, 72, 91, 66, 78, 95]
    
    # Adjustment factors (some are distractors)
    adjustments = [5, -3, 2, 0, 4, -1]
    bonus_points = [1, 1, 1, 1, 1, 1]
    scaling_factors = [1.1, 1.2, 0.9, 1.0, 1.05, 0.95]
    
    # Process marks with adjustments
    processed_marks = [x + y for x, y in zip(marks, adjustments)]
    
    # Distractor calculations that don't affect final result
    temp_scores = [x * y for x, y in zip(processed_marks, scaling_factors)]
    bonus_total = sum(bonus_points)
    
    # Filter marks above threshold and calculate final result
    threshold = 75
    qualifying_marks = [m for m in processed_marks if m > threshold]
    final_result = len(qualifying_marks) * 10
    
    # More distractor operations
    average_mark = sum(processed_marks) / len(processed_marks)
    max_mark = max(processed_marks)
    
    print(f"Result: {final_result}")
    return final_result

calculate_student_performance()