def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = len(deductions) * 2
    adjusted = base_score - penalty_total
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_result = [x for x in points if x > 5]
    
    if adjusted > 50:
        adjusted = adjusted * 0.95  # Apply small bonus reduction
    return int(adjusted)

# Simulate student assessment results
criteria = ['clarity', 'logic', 'syntax', 'design', 'testing']
scores_str = "8,7,9,6,8"
raw_points = [int(x.strip()) for x in scores_str.split(',')]
penalties = ['minor_style_issue', 'late_submission']

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")