def calculate_final_score(grades, adjustments):
    weighted_grades = []
    for i, grade in enumerate(grades):
        weight = 1.0 + (0.1 * i)  # Emphasis on later grades
        adjusted_grade = grade * weight
        weighted_grades.append(adjusted_grade)

    # Apply lambda-based curve adjustment
    curve_function = lambda x: x * 1.05 if x < 80 else x * 1.02
    curved_grades = [curve_function(g) for g in weighted_grades]

    base_total = sum(curved_grades)
    
    # Add bonus based on adjustment factors using zip
    bonus = 0
    for raw_adj, idx in zip(adjustments, range(len(adjustments))):
        bonus += raw_adj * (idx + 1)
    
    total_score = base_total + bonus
    
    # Irrelevant distraction: string processing with no impact
    student_name = "Alice Johnson"
    name_parts = student_name.split()
    initials = ''.join([part[0] for part in name_parts])
    
    return total_score

# Main execution
grades = [85, 78, 92, 88]
adjustments = [3, -1, 2]
total_score = calculate_final_score(grades, adjustments)
print(f"Result: {total_score}")