from collections import defaultdict

# Simulate user quiz attempts with varying success rates
def calculate_final_score(attempts):
    score_map = {'easy': 1, 'medium': 3, 'hard': 5}
    penalty_rate = 0.2
    bonus_applied = False
    streak_count = 0
    base_score = 0
    total_penalty = 0

    for attempt in attempts:
        level = attempt['difficulty']
        correct = attempt['correct']
        base_score += score_map[level] if correct else 0

        if correct:
            streak_count += 1
            if streak_count == 3 and not bonus_applied:
                base_score += 5  # Bonus for three correct in a row
                bonus_applied = True
        else:
            streak_count = 0

        # Accumulate penalties for wrong answers
        if not correct:
            total_penalty += score_map[level] * penalty_rate

    final_score = base_score - total_penalty
    return round(final_score, 2)

# Irrelevant utility function (minor distraction)
def normalize_string(s):
    return s.strip().lower().replace(' ', '_')

# User attempt history
user_attempts = [
    {'difficulty': 'easy',   'correct': True},
    {'difficulty': 'medium', 'correct': True},
    {'difficulty': 'hard',   'correct': False},
    {'difficulty': 'easy',   'correct': True},
    {'difficulty': 'medium', 'correct': False},
    {'difficulty': 'easy',   'correct': True},
    {'difficulty': 'easy',   'correct': True}
]

# Calculation entry point
total_score = calculate_final_score(user_attempts)
print(f"Result: {total_score}")