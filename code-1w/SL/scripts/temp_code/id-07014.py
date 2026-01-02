from collections import defaultdict

def calculate_final_score(attempts, multiplier):
    base_scores = defaultdict(int)
    
    # Record scores from each attempt
    for attempt in attempts:
        if attempt['success']:
            base_scores[attempt['level']] += attempt['points']
    
    # Calculate total from unique levels completed
    raw_total = sum(base_scores.values())
    bonus_points = raw_total * multiplier // 100
    final_score = raw_total + bonus_points
    
    return final_score

# Simulation data
attempts_log = [
    {'level': 'easy', 'points': 10, 'success': True},
    {'level': 'medium', 'points': 25, 'success': True},
    {'level': 'hard', 'points': 50, 'success': False},
    {'level': 'medium', 'points': 25, 'success': True},
    {'level': 'easy', 'points': 10, 'success': True}
]

bonus_multiplier = 20

# Irrelevant tracking variable (minor distraction)
streak_count = 0

for entry in attempts_log:
    if entry['success']:
        streak_count += 1
    else:
        streak_count = 0

# Key computation
total_score = calculate_final_score(attempts_log, bonus_multiplier)

# Output result
print(f"Result: {total_score}")