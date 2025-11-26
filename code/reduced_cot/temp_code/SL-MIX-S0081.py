def calculate_student_performance(scores):
    base_total = sum(scores)
    bonus_points = len([s for s in scores if s > 85])
    penalty_deduction = max(scores) - min(scores)
    
    # Intermediate calculations (some relevant, some distracting)
    avg_score = base_total / len(scores)
    score_variance = sum((s - avg_score) ** 2 for s in scores)
    temporary_adjustment = bonus_points * 2.5
    
    # Core logic with conditional expression
    adjusted_total = base_total + temporary_adjustment - penalty_deduction
    threshold = 320
    
    # Unused intermediate variable (intervention)
    performance_ratio = avg_score / penalty_deduction
    
    final_score = adjusted_total if adjusted_total > threshold else 0
    
    print(f"Result: {final_score}")
    return final_score

# Test data
student_scores = [92, 78, 85, 88, 76]
calculate_student_performance(student_scores)