from collections import defaultdict

# Simulate user activity logs with action types
logs = [
    ('user1', 'click'),
    ('user2', 'view'),
    ('user1', 'view'),
    ('user3', 'click'),
    ('user2', 'click'),
    ('user1', 'click'),
    ('user3', 'view'),
    ('user4', 'view')
]

# Count actions per user
user_actions = defaultdict(lambda: defaultdict(int))
for user, action in logs:
    user_actions[user][action] += 1

# Compute total interactions per user
interaction_totals = {}
for user, actions in user_actions.items():
    interaction_totals[user] = sum(actions.values())

# Rank users by total interactions
sorted_users = sorted(interaction_totals.keys(), key=lambda u: interaction_totals[u], reverse=True)

# Assign ranks and count rank positions
rank_counts = {}
for rank, user in enumerate(sorted_users):
    rank_counts[rank + 1] = rank_counts.get(rank + 1, 0) + 1

# Dummy variable - irrelevant to final result
temp_multiplier = 1.5
scaling_factor = 1

# Calculate final score based on rank distribution
def calculate_final_score(rank_distribution):
    score = 0
    for rank, count in rank_distribution.items():
        score += rank * count  # Emphasize position weight
    return int(score * scaling_factor)

final_score = calculate_final_score(rank_counts)
print(f"Result: {final_score}")