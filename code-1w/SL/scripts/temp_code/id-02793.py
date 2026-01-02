from collections import defaultdict, Counter

# Simulate user activity logs with redundant fields
timestamps = [100, 105, 110, 115, 120, 125, 130]
user_actions = ['click', 'scroll', 'click', 'keypress', 'click', 'scroll', 'click']
dummy_metadata = [{'src': 'a'}, {'src': 'b'}, {'src': 'a'}, {'src': 'c'}, {'src': 'a'}, {'src': 'b'}, {'src': 'a'}]

# Extract action counts per type
action_counter = defaultdict(int)
for action in user_actions:
    action_counter[action] += 1

# Compute derived metrics (some are distractions)
total_interactions = len(user_actions)
dominant_action = max(action_counter, key=action_counter.get)
action_entropy = 0.0
for count in action_counter.values():
    prob = count / total_interactions
    action_entropy -= prob * prob  # Simplified entropy-like calc

# Filter only click-stream events for processing
click_positions = [i for i, a in enumerate(user_actions) if a == 'click']
interval_gaps = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
mean_gap = sum(interval_gaps) / len(interval_gaps)

# Misleading distraction: analyze metadata sources even though unused later
source_counter = Counter()
for meta in dummy_metadata:
    source_counter[meta['src']] += 1
peak_source = source_counter.most_common(1)[0][1]

# Process data: focus on timing consistency around clicks
timing_consistency = 0
for i in range(1, len(click_positions)):
    pos_diff = click_positions[i] - click_positions[i-1]
    timing_consistency += abs(pos_diff - 2)  # Expected every 2nd event

timing_consistency = 10 - min(timing_consistency, 10)  # Cap at 10

# Secondary distraction: compute action diversity (not directly used)
unique_actions = len(action_counter)
action_diversity_score = unique_actions * 1.5

# Core logic: calculate final score based on click frequency and timing
def calculate_final_score(data):
    base_score = data['click_count'] * 7
    time_bonus = data['consistency'] * 3
    return int(base_score + time_bonus)

# Prepare processed data
processed_data = {
    'click_count': action_counter['click'],
    'consistency': timing_consistency,
    'other_metric': action_entropy  # Included but not used
}

# Final computation
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")