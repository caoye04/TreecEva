from collections import defaultdict, Counter
import itertools

# Simulate user interaction sequences on a feature-rich dashboard
dashboard_logs = [
    ('user_01', 'dashboard_view', '2023-05-01 08:30'),
    ('user_02', 'filter_apply', '2023-05-01 08:31'),
    ('user_01', 'export_data', '2023-05-01 08:33'),
    ('user_03', 'dashboard_view', '2023-05-01 08:35'),
    ('user_02', 'dashboard_view', '2023-05-01 08:36'),
    ('user_01', 'filter_apply', '2023-05-01 08:37'),
    ('user_03', 'export_data', '2023-05-01 08:38'),
    ('user_02', 'export_data', '2023-05-01 08:40'),
]

# Extract behavior sequences per user
user_actions = defaultdict(list)
for user_id, action, timestamp in dashboard_logs:
    user_actions[user_id].append(action)

# Misleading distraction: count total timestamps (not used later)
timestamp_counter = Counter([ts.split()[1] for _, _, ts in dashboard_logs])

# Process each user's action sequence
processed_data = []
for user_id, actions in user_actions.items():
    action_count = len(actions)
    unique_actions = len(set(actions))
    
    # Semi-relevant transformation: generate n-grams of actions (distraction)
    bigrams = list(itertools.pairwise(actions))
    bigram_diversity = len(set(bigrams))
    
    # Core metric: engagement score
    base_engagement = action_count * 2 + unique_actions
    
    # Distractor computation: average time between actions (not computable here, mocked)
    mock_time_variance = sum(ord(a[0]) for a in actions) / len(actions) if actions else 0
    
    # Store processed features (only base_engagement is actually used later)
    processed_data.append({
        'user': user_id,
        'engagement': base_engagement,
        'diversity': unique_actions,
        'bigram_entropy': bigram_diversity,  # not used
        'temporal_proxy': mock_time_variance   # not used
    })

# Secondary distraction: aggregate all unique actions across users
all_action_set = set()
for log in dashboard_logs:
    all_action_set.add(log[1])
action_frequency_map = {a: 0 for a in all_action_set}
for _, action, _ in dashboard_logs:
    action_frequency_map[action] += 1

# Real logic begins: filter only high-engagement users
high_engagement_threshold = 5
filtered_users = [p for p in processed_data if p['engagement'] > high_engagement_threshold]

# Compute composite score based only on engagement values
raw_total = sum(p['engagement'] for p in filtered_users)
adjustment_factor = len(filtered_users) if filtered_users else 1

# Apply non-linear adjustment (only this affects final result)
adjusted_sum = int((raw_total / adjustment_factor) ** 1.5)

# Final scoring with weighted contribution from diversity (but diversity not actually accessed)
diversity_bonus = 0
for p in processed_data:
    if p['diversity'] >= 2:
        diversity_bonus += 1  # minor effect, but included

# Critical statement
final_score = calculate_final_score(processed_data)

def calculate_final_score(data):
    high_engagement = [d for d in data if d['engagement'] > 5]
    total_engagement = sum(d['engagement'] for d in high_engagement)
    count = len(high_engagement)
    mean_engagement = total_engagement / count if count else 0
    spread_penalty = abs(high_engagement[0]['engagement'] - high_engagement[-1]['engagement']) if count > 1 else 0
    score = int(mean_engagement ** 2 - spread_penalty * 1.5)
    return score

# Update final_score correctly after function definition
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")