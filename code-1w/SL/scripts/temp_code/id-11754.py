scores = {'alice': 85, 'bob': 90, 'charlie': 95, 'diana': 88}
threshold = 87

top_performers = [k for k, v in scores.items() if v > threshold]

performance_level = 'charlie'

apply_bonus = True if performance_level in top_performers else False

base_reward = 500
bonus_multiplier = 2.5 if apply_bonus else 1.0

# Additional calculation with string-based condition
status = 'active' if scores[performance_level] >= 90 else 'provisional'
extension_eligible = len(status.replace('active', 'ext')) > 3

final_score = base_reward * bonus_multiplier

if extension_eligible:
    final_score += 100

Result: {final_score}