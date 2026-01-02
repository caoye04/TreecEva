def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = sum([d // 2 for d in deductions if d > 0])
    adjusted_score = base_score - penalty_total
    bonus = 10 if adjusted_score >= 50 else 0
    return adjusted_score + bonus

raw_points = [8, 12, 15, 7, 9]
penalties = [6, 0, 10, 4]

# Irrelevant variables (minimal distraction - intervention level 4)
temp_data = [1, 2, 3]
unused_flag = False

final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")