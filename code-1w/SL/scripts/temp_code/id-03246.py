from collections import defaultdict, Counter

# Simulate user interaction logs with redundant fields
timestamps = [1623456780, 1623456789, 1623456800, 1623456815, 1623456830]
user_actions = ['click', 'scroll', 'click', 'hover', 'click']
duration_ms = [500, 1200, 300, 800, 450]
redundant_flags = [False, True, False, True, False]

# Misleading intermediate processing (some irrelevant)
action_counter = Counter(user_actions)
invalid_flag_count = sum(redundant_flags)

# Core data transformation (with slicing and filtering)
recent_logs = [(t, a, d) for t, a, d in zip(timestamps, user_actions, duration_ms)][1:-1]
filtered_durations = [d for d in duration_ms if d > 400]

# State tracking with defaultdict
action_state = defaultdict(int)
for action in user_actions:
    action_state[action] += 1

# Auxiliary calculation: session engagement level
avg_duration = sum(duration_ms) / len(duration_ms)
long_engagements = sum(1 for d in duration_ms if d > avg_duration)
engagement_ratio = long_engagements / len(duration_ms)

# Red herring: unused complex structure
nested_analysis = {
    'meta': {'version': '1.2', 'valid': True},
    'details': [
        {'type': 'timing', 'values': [t % 1000 for t in timestamps]},
        {'type': 'duration_norm', 'values': [round(d / max(duration_ms), 3) for d in duration_ms]}
    ]
}

# Case conversion distraction
clean_actions = [act.upper() for act in user_actions]
unique_actions_upper = list(set(clean_actions))

# Real computation begins: weight each action type
action_weights = {'click': 3, 'scroll': 2, 'hover': 1, 'keypress': 4}
total_weight = sum(action_weights.get(a, 0) for a in user_actions)

# Secondary metric: frequency adjustment
max_action_freq = max(action_counter.values())
frequency_penalty = len(user_actions) - max_action_freq
adjusted_weight = total_weight - frequency_penalty * 0.5

# Data restructuring with slicing and tuple unpacking
packed_data = list(zip(user_actions, duration_ms))
sliced_subset = packed_data[::2]  # Every other interaction
processed_data = []
for act, dur in sliced_subset:
    normalized = dur / 1000.0
    score_contribution = action_weights.get(act, 0) * normalized
    processed_data.append(score_contribution)

# Final scoring function (uses collections.Counter indirectly via preprocessing)
def calculate_final_score(data_list):
    base = sum(data_list)
    bonus = len(data_list) * 0.25
    penalty = Counter(clean_actions).get('CLICK', 0) * 0.1  # Slight penalty for too many clicks
    return round(base + bonus - penalty, 4)

# Execute key statement
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")