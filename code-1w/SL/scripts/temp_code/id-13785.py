from collections import defaultdict, Counter

# Simulated user interaction logs with redundant fields
timestamps = [101, 102, 103, 104, 105, 106]
user_actions = ['click', 'scroll', 'click', 'hover', 'click', 'scroll']
durations = [1.2, 2.1, 0.8, 1.5, 3.0, 1.1]

# Auxiliary data structures (some irrelevant)
action_count = defaultdict(int)
invalid_flags = set()
summary_stats = {'total': 0, 'valid': 0, 'ignored': 0}

# Redundant processing step 1: count all actions
total_processed = 0
for action in user_actions:
    action_count[action] += 1
    total_processed += 1

# Misleading intermediate calculation (not used later)
avg_duration = sum(durations) / len(durations) if durations else 0
penalty_factor = 0.9 if avg_duration < 1.5 else 1.0

# Simulate noise filtering (partially relevant)
filtered_actions = []
for i, action in enumerate(user_actions):
    if durations[i] > 0.5 and action != 'hover':
        filtered_actions.append(action)
    else:
        invalid_flags.add(i)

# Another distraction: frequency analysis of timestamps
interval_gaps = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
gap_counter = Counter(interval_gaps)
median_gap = sorted(interval_gaps)[len(interval_gaps)//2]

# Core logic begins: scoring system based on filtered click-stream
base_weights = {'click': 5, 'scroll': 2}
score_components = []
for act in filtered_actions:
    if act in base_weights:
        score_components.append(base_weights[act])

# Secondary scoring from pattern context
pattern_bonus = 0
if action_count['click'] >= 3:
    pattern_bonus += 10
if 'scroll' in filtered_actions and durations[1] > 2.0:
    pattern_bonus += 5  # Not triggered due to filtering

# Distractor: unused decay model
decay_rate = 0.95
weighted_decay_score = 0
for idx, sc in enumerate(score_components):
    weighted_decay_score += sc * (decay_rate ** idx)

# Main aggregation using conditional expression and slicing
recent_contributions = score_components[-4:] if len(score_components) > 4 else score_components[:]
raw_sum = sum(recent_contributions)
adjustment = 1.1 if len(filtered_actions) > 4 else 0.95

# Final computation point — key statement
final_score = int((raw_sum * adjustment) + pattern_bonus)

# Output required format
print(f"Result: {final_score}")