def calculate_performance(rewards):
    base_points = 85
    multiplier = len(rewards)
    adjustment = 0
    
    for key in rewards:
        if key.startswith('skill'):
            adjustment += rewards[key] * 0.2
        elif key.endswith('bonus'):
            adjustment += rewards[key]

    raw_score = base_points + sum(rewards.values())
    final_score = raw_score * multiplier + adjustment
    
    return final_score

# Irrelevant utility function (minor distraction)
def format_percentage(value):
    return f'{value * 100:.1f}%'

# Data setup
bonus_map = {
    'skill_test_a': 10,
    'skill_test_b': 15,
    'year_end_bonus': 7,
    'referral_bonus': 3
}

initial_estimate = 0
for v in bonus_map.values():
    initial_estimate += v

final_score = calculate_performance(bonus_map)
print(f'Result: {final_score}')