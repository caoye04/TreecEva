def calculate_final_score(points, deductions):
    base_multiplier = 2
    rank_bonus = len([p for p in points if p > 25])
    adjusted_deductions = sum([d for d in deductions if d < 10])
    raw_score = sum(points) * base_multiplier
    raw_score -= adjusted_deductions
    if rank_bonus:
        raw_score += rank_bonus * 5
    return raw_score

# Irrelevant auxiliary data (minor distraction)
user_data = {'level': 3, 'active': True}
temp_log = [1, 1, 1]  # Unused tracking

# Core computation inputs
rank_points = [30, 15, 40, 20]
penalties = [5, 12, 8, 15]

# Key statement
final_score = calculate_final_score(rank_points, penalties)

print(f"Result: {final_score}")