from collections import defaultdict

# Simulate user activity logs with action types and timestamps
activity_logs = [
    ('user_123', 'click', 10),
    ('user_456', 'scroll', 15),
    ('user_123', 'hover', 8),
    ('user_789', 'click', 12),
    ('user_456', 'click', 20),
    ('user_123', 'click', 5),
    ('user_789', 'scroll', 18),
    ('user_456', 'hover', 7)
]

# Aggregate actions per user
user_actions = defaultdict(list)
for user, action, duration in activity_logs:
    user_actions[user].append((action, duration))

# Compute total interaction time per user
interaction_time = {}
dummy_counter = 0
for user, actions in user_actions.items():
    total_time = sum(duration for _, duration in actions)
    interaction_time[user] = total_time
    if total_time > 25:
        dummy_counter += 1  # Distractor: not used later

# Assign preliminary rank based on interaction time
sorted_users = sorted(interaction_time, key=lambda u: interaction_time[u], reverse=True)
rank_data = {user: idx + 1 for idx, user in enumerate(sorted_users)}

# Misleading computation: unrelated to final result
idle_time_estimate = sum(30 - interaction_time[u] for u in interaction_time if interaction_time[u] < 30)
adjusted_ranks = {u: 1.0 / rank_data[u] for u in rank_data}  # Not used

# Bonus logic based on action diversity
bonus_multiplier = {}
for user, actions in user_actions.items():
    action_types = set(act for act, _ in actions)
    diversity_score = len(action_types)
    bonus_multiplier[user] = 1 + (0.1 * diversity_score)  # Up to 30% bonus

# Dead code path - never executed but looks relevant
def deprecated_rank_adjust(ranks):
    return {u: r * 0.9 for u, r in ranks.items()}

# Core scoring function
def calculate_final_score(ranks, bonuses):
    score = 0
    temp_log = []
    for user, rank in ranks.items():
        base_points = 100 // rank
        adjusted_points = int(base_points * bonuses.get(user, 1))
        # Apply artificial penalty for low activity (distractor logic)
        if interaction_time[user] < 10:
            adjusted_points -= 5
        score += adjusted_points
        temp_log.append(f'{user}: {adjusted_points}')  # Logged but unused
    return score

# Final computation
final_score = calculate_final_score(rank_data, bonus_multiplier)

# Print result as required
print(f"Target result: {final_score}")