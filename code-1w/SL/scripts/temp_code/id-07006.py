def calculate_final(exam, coursework):
    weight_exam = 0.7
    weight_coursework = 0.3
    adjusted_exam = max(exam, 40)  # Minimum threshold for exam
    bonus = 5 if coursework > 85 and exam > 70 else 0
    
    # Use lambda to compute weighted sum
    weighted_sum = (lambda e, c: weight_exam * e + weight_coursework * c)(adjusted_exam, coursework)
    
    # Conditional expression for distinction
    final = weighted_sum + bonus
    return final

# Simulated student results
test_exam = 68
test_coursework = 90

# Irrelevant distraction: unused variable
theoretical_max = 100

final_score = calculate_final(test_exam, test_coursework)
print(f"Result: {final_score}")