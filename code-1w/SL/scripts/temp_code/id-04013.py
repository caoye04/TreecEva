from collections import defaultdict, Counter

# Simulated user interaction logs with various actions and timestamps
log_data = [
    ('click', 1, 101), ('scroll', 2, 102), ('click', 1, 103),
    ('hover', 3, 104), ('click', 4, 105), ('scroll', 2, 106),
    ('click', 1, 107), ('keypress', 5, 108), ('scroll', 4, 109),
    ('click', 4, 110)
]

# Irrelevant distractor: unused data structure for session mapping
temp_session_map = {i: f'session_{i}' for i in range(1, 6)}

# Distractor variables: fake metrics that are computed but not used
fake_avg_duration = sum([len(entry[0]) * entry[1] for entry in log_data]) / len(log_data)
fake_action_ranks = sorted(set([entry[0] for entry in log_data]), key=len, reverse=True)

# Track action counts per user
user_action_count = defaultdict(lambda: defaultdict(int))
for action, user_id, timestamp in log_data:
    user_action_count[user_id][action] += 1

# Compute total interactions per user (distraction from main logic)
user_totals = {uid: sum(actions.values()) for uid, actions in user_action_count.items()}

# Focus metric: count only 'click' actions across users
click_counter = Counter()
for action, user_id, _ in log_data:
    if action == 'click':
        click_counter[user_id] += 1

# Secondary distraction: analyze hover patterns even though they're irrelevant
total_hovers = sum(1 for a, _, _ in log_data if a == 'hover')
hover_users = set(user_id for a, user_id, _ in log_data if a == 'hover')

# Real computation begins: weight each user's click count by inverse of their total activity
weighted_clicks = []
for user_id in click_counter:
    total_user_actions = user_totals[user_id]  # includes all actions
    raw_clicks = click_counter[user_id]
    # Apply weighting: more clicks relative to total actions increases score
    weight = raw_clicks / total_user_actions if total_user_actions > 0 else 0
    weighted_clicks.append(weight * 100)  # scale up for integer precision

# Decoy function: looks important but unused
def calculate_engagement_score(data):
    return sum(len(d[0]) for d in data) % 100

# Another red herring: complex string transformation with no impact
dummy_profile = ''.join([str(len(a) * t)[-1] for a, _, t in log_data[:5]])

# Aggregate function that actually matters
def compute_aggregate(values, offset=10):
    base = sum(val for val in values if val > 10)  # filter out low weights
    bonus = len([v for v in values if v > 20]) * 2  # extra credit for high engagement
    penalty = int(any(v < 5 for v in values)) * 3  # small penalty if any weak scores
    return int(base + bonus - penalty + offset)

# Misleading comment: "adjusting for system latency" (no real latency here)
adjusted_offset = abs(hash('latency_correction')) % 7  # looks technical, but predictable

# Critical execution point
final_score = compute_aggregate(weighted_clicks, offset=adjusted_offset)

# Output the result as required
print(f"Result: {final_score}")