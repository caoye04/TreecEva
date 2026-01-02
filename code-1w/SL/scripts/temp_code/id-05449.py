def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = len(deductions) * 2
    adjusted_score = base_score - penalty_total
    
    # Apply bonus for high performance
    if adjusted_score > 80:
        adjusted_score += 10
    
    return adjusted_score

# Simulate student assessment results
criteria_met = {'clarity': True, 'logic': True, 'efficiency': False}
raw_points = [25, 20, 15, 10]
penalties = ['formatting', 'late_submission']

# Irrelevant distraction: unused variable (minimal interference)
temp_result = set([1, 2, 3])

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")