def evaluate_performance(skills, difficulty):
    base = sum([s ** 0.5 for s in skills if s > 0])
    penalty = 0
    if difficulty > 7:
        penalty = len([s for s in skills if s < 5]) * 1.5
    bonus = 2.0 if 'high_focus' in locals() else 0.5
    return round(base - penalty + bonus, 2)

skill_levels = [9, 16, 4, 1, 25]
challenge_difficulty = 8
initial_check = skill_levels[0] > 5
high_focus = True  # This doesn't trigger bonus since scope is inside function
final_score = evaluate_performance(skill_levels, challenge_difficulty)
print(f"Result: {final_score}")