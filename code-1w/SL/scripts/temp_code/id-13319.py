from collections import defaultdict

def calculate_final_score(student_grades, multiplier):
    base_points = 0
    extra_credit = 0
    
    # Apply grade scaling using common letter grade to point conversion
    scale = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    for grade in student_grades:
        if grade in scale:
            base_points += scale[grade]
    
    # Bonus logic based on performance consistency
    grade_count = defaultdict(int)
    for g in student_grades:
        grade_count[g] += 1

    if grade_count['A'] >= 3:
        extra_credit = 5
    
    # Compute final score with multiplier adjustment
    adjusted_bonus = extra_credit * multiplier
    final_result = base_points + adjusted_bonus
    return final_result

# Simulate student transcript data
grades = ['A', 'B', 'A', 'C', 'A', 'B']
bonus_multiplier = 2.0

# Calculate overall score
total_score = calculate_final_score(grades, bonus_multiplier)

print(f"Result: {total_score}")