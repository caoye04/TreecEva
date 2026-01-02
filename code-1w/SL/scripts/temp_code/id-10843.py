def calculate_final_score(data, mult):
    base_score = 0
    penalty = 0
    temp_adjustment = 0  # distractor variable
    legacy_modifier = 1.0  # unused legacy parameter

    for i, (key, value) in enumerate(data.items()):
        if i % 2 == 0:
            base_score += value['points']
        else:
            temp_adjustment -= value['points'] // 4  # semi-relevant but not used directly

    # Simulate conditional bonus eligibility
    eligible_categories = []
    for category, info in data.items():
        if info['completed']:
            eligible_categories.append(category)

    bonus_points = len(eligible_categories) * mult

    # Red herring: complex but irrelevant computation
    phantom_total = 0
    for x in range(3):
        for y in range(3):
            phantom_total += x * y  # dead computation

    # Actual scoring logic
    streak_count = 0
    max_streak = 0
    for _, info in data.items():
        if info['streak']:
            streak_count += 1
        else:
            max_streak = max(max_streak, streak_count)
            streak_count = 0
    max_streak = max(max_streak, streak_count)

    performance_bonus = 5 * max_streak

    final_score = base_score + bonus_points + performance_bonus

    # Distractor: slicing operation with no impact
    slices = [eligible_categories[i:i+2] for i in range(0, len(eligible_categories), 3)]
    slice_sum = sum(len(s) for s in slices)  # unused

    return final_score

# Initialize player data
data_input = {
    'quest_a': {'points': 25, 'completed': True, 'streak': True},
    'quest_b': {'points': 15, 'completed': False, 'streak': True},
    'quest_c': {'points': 40, 'completed': True, 'streak': False},
    'quest_d': {'points': 10, 'completed': True, 'streak': True},
    'quest_e': {'points': 30, 'completed': True, 'streak': True}
}
bonus_multiplier = 7

# Compute result
final_score = calculate_final_score(data_input, bonus_multiplier)
print(f"Target result: {final_score}")