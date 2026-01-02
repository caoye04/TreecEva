def calculate_final_score(points, deductions):
    base_score = sum([p for p in points if p > 0])
    penalty_adjustment = len(deductions) // 2
    adjusted_deductions = [abs(d) for d in deductions if d < -1]
    total_deduction = sum(adjusted_deductions)
    
    # Irrelevant variable (minimal distraction)
    temp_warning_flag = True if total_deduction > 10 else False
    
    if base_score >= 50:
        bonus = 10
    else:
        bonus = 5
    
    return base_score - total_deduction + bonus - penalty_adjustment

# Main execution
raw_points = [15, -5, 20, 0, 25]
penalties = [-2, -3, 1, -4, 0]
final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")