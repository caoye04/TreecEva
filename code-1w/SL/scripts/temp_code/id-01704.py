def calculate_total(grades, bonus_func):
    base_total = sum(grades)
    adjustments = list(map(lambda x: 1 if x >= 90 else 0, grades))
    extra_points = bonus_func(len([x for x in adjustments if x == 1]))
    return base_total + extra_points

# Student marks in various subjects
test_marks = [85, 92, 78, 96, 88]
participation = 5

# Irrelevant distraction variable (minimal interference)
student_status = "active".upper()

# Bonus logic based on high-performing subjects
dynamic_bonus = lambda count: count * 3.5

# Final computation step
class_curve = 2.0
final_score = calculate_total(test_marks, dynamic_bonus)
print(f"Result: {final_score}")