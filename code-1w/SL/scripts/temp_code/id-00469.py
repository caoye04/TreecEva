from collections import defaultdict, Counter
import math

# Simulated user interaction log with redundant and irrelevant fields
timestamps = [1623456780, 1623456789, 1623456800, 1623456815, 1623456830]
user_actions = ['click', 'scroll', 'click', 'hover', 'click', 'keypress', 'click']
durations = [120, 45, 300, 15, 60, 10, 200]

# Irrelevant preprocessing: dummy transformation chain
action_map = {act: idx for idx, act in enumerate(set(user_actions))}
dummy_encoded = [action_map[action] for action in user_actions]
dummy_shifted = [(x * 7 + 3) % 256 for x in dummy_encoded]

# Feature extraction (some relevant, many red herrings)
click_count = user_actions.count('click')
hover_duration = durations[3]  # Misleading: isolated value not used later
total_time = sum(durations)
avg_duration = total_time / len(durations)

# Distractor: complex but unused data structure
temp_profile = defaultdict(lambda: {'freq': 0, 'total': 0})
for i, action in enumerate(user_actions):
    temp_profile[action]['freq'] += 1
    temp_profile[action]['total'] += durations[i]

# Unused recursive function (dead code path)
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

# String-based session identifier with embedded numeric clues (decoy)
session_id = "sess_2023_user_4567"
id_digits = ''.join(filter(str.isdigit, session_id))
user_id_part = int(id_digits[-4:])  # Looks important but isn't directly used

# Real signal buried in noise: analyze click pattern density
click_indices = [i for i, act in enumerate(user_actions) if act == 'click']
click_intervals = [click_indices[i+1] - click_indices[i] for i in range(len(click_indices)-1)]
interval_variance = sum((x - sum(click_intervals)/len(click_intervals))**2 for x in click_intervals) / len(click_intervals)

# Secondary metric: decay-weighted action score
decay_factor = 0.8
weighted_action_score = sum(decay_factor ** i * (1 + len(act)) for i, act in enumerate(reversed(user_actions)))

# Distractor dictionary with plausible but unused metrics
metrics_summary = {
    'peak_engagement': max(durations),
    'action_entropy': sum(-p/len(user_actions) * math.log(p/len(user_actions)) for p in Counter(user_actions).values()),
    'temporal_jitter': sum(abs(durations[i+1] - durations[i]) for i in range(len(durations)-1)),
    'theoretical_limit': math.gamma(6)  # Red herring using math module
}

# Core logic hidden among noise: assess behavioral consistency via modular pattern
pattern_seed = sum(click_intervals) % 7
consistency_metric = 0
for interval in click_intervals:
    consistency_metric += (interval % pattern_seed) if pattern_seed != 0 else 0

# String manipulation decoy: split and recombine
path_parts = ['home', 'category', 'item', 'checkout', 'confirm']
nav_flow = ' -> '.join(path_parts)
nav_length = len(nav_flow.split(' -> '))  # Looks structural but unused

# Final aggregation with critical but obscured calculation
baseline = avg_duration // 10
modifier = len(click_intervals) * (consistency_metric or 1)
bonus = user_id_part % 13  # Subtle use of earlier parsed value

# Key statement: what is the value of final_score here?
final_score = baseline * modifier + bonus

print(f"Result: {final_score}")