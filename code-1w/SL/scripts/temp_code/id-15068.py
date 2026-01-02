def analyze_productivity(activities):
    weights = {'coding': 3, 'review': 2, 'meeting': 1, 'debug': 4}
    base_points = 0
    bonus_tracker = []
    
    for i, activity in enumerate(activities):
        action, duration = activity
        if action in weights:
            base_points += weights[action] * duration
            if duration > 2:
                bonus_tracker.append(i)
    
    adjusted = base_points * 0.9
    return int(adjusted)


def calculate_rating(entries, effects):
    category_map = {'high': 3, 'medium': 2, 'low': 1}
    temp_result = 0
    indices_processed = set()
    
    for idx, (entry, effect) in enumerate(zip(entries, effects)):
        if len(entry) == 0:
            continue
        contribution_value = len(entry) * category_map.get(effect, 0)
        temp_result += contribution_value
        indices_processed.add(idx)
    
    # Misleading secondary computation
    phantom_sum = 0
    for x in range(len(entries)):
        if x not in indices_processed:
            phantom_sum += x * 10
    
    scaling_factor = 1.25 if len(indices_processed) > 3 else 1.0
    intermediate = temp_result * scaling_factor
    
    noise = 0
    for k in [1, 2, 3]:
        noise += (k ** 2) % 3  # Irrelevant but plausible-looking calc
    
    final_rating = int(intermediate - noise)
    return final_rating

# Main data
contributions = [
    ['feat', 'fix'],
    ['refactor'],
    ['docs', 'chore', 'style'],
    ['feat', 'test'],
    ['fix', 'refactor']
]

impact_levels = ['high', 'low', 'medium', 'high', 'medium']

# Dummy variables and irrelevant preprocessing
productivity_log = [
    ('coding', 3),
    ('meeting', 1),
    ('coding', 2),
    ('debug', 5)
]

score_a = analyze_productivity(productivity_log)
score_b = sum(len(item) for item in contributions) * 2  # Distractor metric

# Key statement
final_score = calculate_rating(contributions, impact_levels)

print(f"Result: {final_score}")