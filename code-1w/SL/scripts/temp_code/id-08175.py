def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = len(deductions) * 2
    adjusted = base_score - penalty_total
    
    # Irrelevant distraction: unused variable (minimal interference)
    max_possible = 100
    
    if adjusted > 85:
        return adjusted + 5
    elif adjusted > 70:
        return adjusted + 2
    else:
        return adjusted

# Main execution
categories = ['math', 'logic', 'coding', 'design']
raw_points = [20, 18, 19, 16]
penalties = ['late_submission', 'format_error']

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")