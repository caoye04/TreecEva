from collections import defaultdict
from itertools import combinations

# Simulate user interaction sequences on a feature-rich dashboard
dashboard_logs = [
    ('user_01', 'view', 'chart'),
    ('user_01', 'click', 'export'),
    ('user_02', 'view', 'table'),
    ('user_01', 'hover', 'filter'),
    ('user_03', 'click', 'refresh'),
    ('user_02', 'click', 'export'),
    ('user_03', 'view', 'chart'),
    ('user_01', 'click', 'settings'),
    ('user_04', 'view', 'table'),
    ('user_04', 'hover', 'sort'),
    ('user_02', 'click', 'settings'),
    ('user_03', 'click', 'export')
]

# Track action frequencies per user and type
action_counts = defaultdict(lambda: defaultdict(int))
user_engagement = defaultdict(list)
redundant_counter = 0  # Distractor: counts nothing meaningful

for user, action, target in dashboard_logs:
    action_counts[user][action] += 1
    user_engagement[user].append(target)
    if action == 'click':
        redundant_counter += 1  # Irrelevant increment

# Calculate engagement scores
engagement_scores = {}
for user, actions in action_counts.items():
    base_score = actions.get('view', 0) * 1.0 + actions.get('hover', 0) * 0.5
    bonus = 2 if actions.get('click', 0) >= 2 else 0
    penalty = 1 if 'settings' in user_engagement[user] else 0
    engagement_scores[user] = base_score + bonus - penalty

# Process data for final scoring
processed_data = []
for user, score in engagement_scores.items():
    normalized = round(score * 10) / 10  # Normalize to one decimal
    processed_data.append(normalized)

# Distractor: explore combination patterns (not used in final result)
useless_combinations = []
for combo in combinations(processed_data, 2):
    diff = abs(combo[0] - combo[1])
    if diff > 1.5:
        useless_combinations.append(diff)

# Real computation begins here
def calculate_final_score(data):
    total = 0
    threshold = 3.0
    adjustment = 0
    
    for val in data:
        if val > threshold:
            total += int(val)  # Integer truncation
        else:
            total += len(str(round(val, 1)))  # Count characters in string representation
    
    # Bitwise red herring
    temp_mask = 0b1010
    for _ in range(3):
        temp_mask ^= 0b1111  # Flips back and forth, ultimately irrelevant
    
    # Final adjustment based on data length
    if len(data) % 2 == 1:
        adjustment = temp_mask & 5  # Evaluates to 0 due to mask state
    
    return total + adjustment

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")