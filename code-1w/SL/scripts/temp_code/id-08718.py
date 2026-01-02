def calculate_total(grades, multiplier):
    base_total = sum([grade for grade in grades.values() if grade >= 60])
    extra_credit = len([g for g in grades.values() if g > 90]) * 5
    adjustment = 0
    if base_total > 200:
        adjustment = 10
    return (base_total + extra_credit + adjustment) * multiplier

# Student grades in various subjects
dict_grades = {
    'math': 85,
    'science': 92,
    'literature': 78,
    'history': 65,
    'art': 94
}

bonus_multiplier = 1.1
initial_check = sum(dict_grades.values())  # Irrelevant: used for logging only
final_score = calculate_total(dict_grades, bonus_multiplier)
print(f"Result: {final_score}")