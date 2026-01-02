from collections import defaultdict
from itertools import combinations

# Simulate user interaction sequences on a feature-rich dashboard
dashboard_events = [
    ('user_a', 'click', 'button_x'),
    ('user_b', 'hover', 'menu_y'),
    ('user_a', 'submit', 'form_z'),
    ('user_c', 'click', 'button_x'),
    ('user_b', 'click', 'button_x'),
    ('user_d', 'submit', 'form_z'),
    ('user_a', 'hover', 'menu_y')
]

# Track event frequencies by user and type
event_counter = defaultdict(lambda: defaultdict(int))
user_action_matrix = defaultdict(set)
redundant_tracker = {}  # Unused tracking structure (distractor)

for user, action, target in dashboard_events:
    event_counter[user][action] += 1
    user_action_matrix[user].add(target)

# Compute action diversity per user
action_diversity = {}
total_interactions = 0
for user in event_counter:
    action_types = len(event_counter[user])
    action_diversity[user] = action_types
    total_interactions += sum(event_counter[user].values())

# Derive engagement score based on unique targets and action variety
engagement_scores = {}
for user in user_action_matrix:
    unique_targets = len(user_action_matrix[user])
    variety_bonus = action_diversity[user]
    base_score = unique_targets * 2.5
    engagement_scores[user] = base_score + variety_bonus

# Process data for final scoring
processed_data = []
for user, score in engagement_scores.items():
    normalized = score / total_interactions
    processed_data.append(normalized * 100)  # Scale to percentage-like values

# Irrelevant combination analysis (distractor - does not affect result)
if len(processed_data) > 2:
    combinatorial_pairs = list(combinations(processed_data, 2))
    pair_summation = sum([abs(a - b) for a, b in combinatorial_pairs])  # Unused

# Weighted aggregation function
def calculate_final_score(data):
    weights = [0.1, 0.2, 0.4, 0.3]  # Assume max 4 users
    weighted_total = 0.0
    for i, value in enumerate(data):
        if i < len(weights):
            weighted_total += value * weights[i]
        else:
            weighted_total += value * 0.05  # Fallback weight
    return round(weighted_total, 4)

# Final computation step
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")