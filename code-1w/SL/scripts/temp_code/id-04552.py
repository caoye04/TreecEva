def calculate_total(values, deductions):
    base = sum(values)
    penalty_func = lambda x: x * 0.1 if x > 10 else 0
    total_deduction = sum(penalty_func(d) for d in deductions)
    return int(base - total_deduction)

# Simulation of game round scores and overages
points = [12, 8, 15, 23]
penalties = [12, 5, 18]
extra_data = [1, 2, 3]  # Irrelevant data (minimal distraction)
comment_flag = True  # Distractor flag, unused

final_score = calculate_total(points, penalties)
print(f"Target result: {final_score}")