def calculate_student_performance():
    student_grades = [85, 92, 78, 96, 88]
    assignment_weights = [0.15, 0.20, 0.10, 0.25, 0.30]
    
    # Calculate weighted sum using zip
    weighted_sum = 0
    for grade, weight in zip(student_grades, assignment_weights):
        weighted_sum += grade * weight
    
    # Bonus calculation (distractor - not used in final result)
    max_grade = max(student_grades)
    bonus_calc = max_grade * 0.05
    
    # Bonus points based on grade consistency
    grade_range = max(student_grades) - min(student_grades)
    bonus_points = 10 if grade_range < 20 else 5
    
    # Penalty adjustment (distractor - partially relevant)
    average_grade = sum(student_grades) / len(student_grades)
    penalty_calc = (100 - average_grade) * 0.1
    
    # Final calculation with conditional expression
    penalty_adjustment = penalty_calc if average_grade < 90 else 0
    
    # The key statement
    final_score = weighted_sum + bonus_points - penalty_adjustment
    
    print(f"Result: {final_score}")
    return final_score

calculate_student_performance()