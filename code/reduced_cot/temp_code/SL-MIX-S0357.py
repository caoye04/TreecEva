def score_calculator(grades):
    weight_factor = 0.6
    base_points = 50
    
    weighted_grades = [grade * weight_factor for grade in grades]
    total_weighted = sum(weighted_grades)
    final_result = base_points + total_weighted
    
    # Distractor variable (never used)
    adjustment_factor = 1.25
    bonus_points = 15
    
    return final_result

student_grades = [85, 92, 78, 95, 88]
final_score = score_calculator(student_grades)
print(f"Result: {final_score}")