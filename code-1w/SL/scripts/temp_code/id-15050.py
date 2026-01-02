def calculate_final_score(points, penalty):
    level_bonus = 10 if points > 80 else 5
    adjusted = points - penalty
    capped = min(adjusted, 95)
    final_score = capped + level_bonus
    return final_score

raw_points = 87
penalty_adjustment = 6
initial_pass = raw_points >= 75
raw_points_str = str(raw_points)
digit_count = len(raw_points_str)
penalty_adjustment = int(str(penalty_adjustment).replace('6', '4'))
final_score = calculate_final_score(raw_points, penalty_adjustment)
print(f"Result: {final_score}")