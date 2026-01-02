def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_set = {x for x in deductions if x > 0}
    adjusted_score = base_score - sum(penalty_set)
    bonus = 10 if len(penalty_set) < 3 else 0
    return adjusted_score + bonus

raw_points = [85, 90, 78, 92]
penalties = [5, 0, 15, 5]

# Irrelevant auxiliary variable (minimal distraction)
temp_data = 'processing'

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")