def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = len(deductions) * 2
    adjusted = base_score - penalty_total
    bonus = 10 if adjusted > 50 else 0
    return adjusted + bonus

# Simulation data
raw_points = [8, 12, 15, 7, 11]
penalties = ['late_submission', 'formatting_error']

# Irrelevant distraction variables
config_flags = {'debug': False, 'verbose': True}
temp_result = [x ** 2 for x in raw_points if x % 2 == 0]

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")