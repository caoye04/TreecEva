def analyze_trends(values):
    # Irrelevant helper function for trend analysis (not used in main logic)
    if len(values) < 2:
        return 0
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
    return trend

# Unused data structures as distractors
trend_data = [15, 23, 34, 45, 52]
dummy_matrix = [[0]*5 for _ in range(5)]
offset_map = {'a': 1, 'b': 2, 'c': 3}

user_data = {
    'id': 'U789',
    'metrics': [85, 90, 78, 92],
    'history': [76, 88, 84],
    'level': 3,
    'active': True
}

preferences = {
    'weight_a': 0.4,
    'weight_b': 0.3,
    'weight_c': 0.3,
    'threshold': 85,
    'bonus_active': True
}

# Misleading intermediate calculations
baseline = sum(user_data['metrics']) / len(user_data['metrics'])
penalty = 0
if user_data['level'] < 2:
    penalty = 5

# Dummy sorting operation (distractor)
sorted_metrics = sorted(user_data['metrics'], reverse=True)
adjusted_metrics = [x + 2 for x in sorted_metrics if x < 88]

# Unused bitwise manipulation (red herring)
flag_value = 0b1010 ^ 0b1100 & 0b0111
mask_applied = flag_value << 2

# Simulated bonus unrelated to final result
temp_bonus = 0
if preferences['bonus_active'] and user_data['active']:
    temp_bonus = 7

# Core logic buried among distractions
recent_avg = sum(user_data['history'][-2:]) / 2 if len(user_data['history']) >= 2 else 0
primary_score = sum(user_data['metrics']) * preferences['weight_a']
secondary_score = recent_avg * (preferences['weight_b'] + preferences['weight_c'])

# Conditional adjustment based on threshold
if primary_score < preferences['threshold'] * 3:
    secondary_score += 10

# Dictionary-based dynamic adjustment (key relevant concept)
level_bonus = {1: 5, 2: 8, 3: 12, 4: 15}.get(user_data['level'], 0)

# Final computation chain
raw_rating = primary_score + secondary_score + level_bonus

# Additional distraction: unused loop over dictionary keys
total_weight = 0
for k in preferences:
    if 'weight' in k:
        total_weight += preferences[k]

# Final score calculation — only this matters
final_score = int(raw_rating - baseline + 5)

Result: final_score