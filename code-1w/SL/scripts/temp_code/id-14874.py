def calculate_final_score(grades, weight_fn):
    weighted_sum = 0
    max_possible = 0
    bonus_applied = False
    
    for i, (subject, score) in enumerate(grades):
        weight = weight_fn(i)
        weighted_sum += score * weight
        max_possible += 100 * weight
        
        if score > 95 and not bonus_applied:
            weighted_sum += 5
            bonus_applied = True

    return weighted_sum

# Student grades data
student_grades = [
    ('math', 98),
    ('physics', 87),
    ('chemistry', 92),
    ('biology', 83)
]

# Weight function using lambda based on position
weight_function = lambda idx: 1.5 if idx == 0 else 1.0

# Irrelevant utility (minimal interference)
def unused_helper():
    return sum([1 for _ in range(5)])

# Calculation
base_average = sum([score for _, score in student_grades]) / len(student_grades)
total_score = calculate_final_score(student_grades, weight_function)

print(f"Result: {total_score}")