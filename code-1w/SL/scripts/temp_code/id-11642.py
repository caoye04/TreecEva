def compute_student_grade(raw_score, bonus_eligible):
    base_score = raw_score * 0.8
    adjustment_factor = 1.2 if bonus_eligible else 1.0
    adjusted_base = base_score * adjustment_factor
    
    # Additional computation for curve bonus
    if raw_score >= 70:
        curve_bonus = 10
    elif raw_score >= 60:
        curve_bonus = 5
    else:
        curve_bonus = 0
    
    passing = adjusted_base + curve_bonus >= 60
    final_score = adjusted_base + curve_bonus if passing else base_score * 0.5
    
    # Irrelevant tracking variable (minimal distraction)
    status_label = "Pass" if passing else "Fail"
    
    return final_score

result = compute_student_grade(68, True)
print(f"Result: {result}")