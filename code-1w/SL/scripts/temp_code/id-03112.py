def calculate_final_score(points, deductions):
    base = sum(points)
    adjustment = len(deductions) * 2
    if base > 50:
        base -= adjustment
    else:
        base -= adjustment // 2
    return base

# Player performance tracking
today_attempts = [15, 20, 18]
bonus_awarded = False
rank_points = today_attempts + [7]
penalties = {"timeout": 1, "foul": 1, "delay": 1}
dummy_var = [x**2 for x in range(3)]  # Irrelevant computation (minimal distraction)

final_score = calculate_final_score(rank_points, penalties)
print(f"Result: {final_score}")