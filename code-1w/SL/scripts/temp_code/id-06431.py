from collections import defaultdict
from itertools import combinations

# Simulated user interaction dataset with redundant fields
data_entries = [
    {'user': 'A', 'action': 'click', 'duration': 120, 'timestamp': 1000, 'extras': {'temp': 0.5}},
    {'user': 'B', 'action': 'hover', 'duration': 45, 'timestamp': 1005, 'extras': {'temp': 0.3}},
    {'user': 'A', 'action': 'click', 'duration': 200, 'timestamp': 1010, 'extras': {'temp': 0.8}},
    {'user': 'C', 'action': 'scroll', 'duration': 300, 'timestamp': 1015, 'extras': {'temp': 0.6}},
    {'user': 'B', 'action': 'click', 'duration': 180, 'timestamp': 1020, 'extras': {'temp': 0.9}}
]

# Irrelevant aggregation: tracking hover counts (not used in final score)
hover_tracker = defaultdict(int)
for entry in data_entries:
    if entry['action'] == 'hover':
        hover_tracker[entry['user']] += 1

# Preprocessing: extract only relevant actions and durations
relevant_actions = [e for e in data_entries if e['action'] in ['click', 'scroll']]

# Misleading transformation: normalize duration with unused temp factor
normalized_durations = []
for entry in relevant_actions:
    adjusted = entry['duration'] * (1 + entry['extras']['temp'])
    normalized_durations.append(adjusted)

# Distractor: compute pairwise duration differences (never used)
duration_pairs = list(combinations(normalized_durations, 2))
mean_pair_diff = sum(abs(a - b) for a, b in duration_pairs) / len(duration_pairs) if duration_pairs else 0

# Actual processing begins here
user_total_time = defaultdict(float)
user_click_count = defaultdict(int)

for entry in relevant_actions:
    user = entry['user']
    user_total_time[user] += entry['duration']
    if entry['action'] == 'click':
        user_click_count[user] += 1

# Compute efficiency ratio per user (clicks per second)
efficiency_ratio = {}
for user in user_total_time:
    time_used = user_total_time[user]
    clicks = user_click_count[user]
    efficiency_ratio[user] = clicks / time_used if time_used > 0 else 0

# Intermediate metric: harmonic mean of efficiency ratios
non_zero_ratios = [r for r in efficiency_ratio.values() if r > 0]
if non_zero_ratios:
    harmonic_mean = len(non_zero_ratios) / sum(1/r for r in non_zero_ratios)
else:
    harmonic_mean = 0

# Secondary distractor: simulate session clustering (unused)
session_splits = [normalized_durations[i:i+2] for i in range(0, len(normalized_durations), 2)]
max_split_sum = max(sum(split) for split in session_splits) if session_splits else 0

# Weighted scoring using modular weights
def calculate_final_score(data):
    base_score = 0
    for user, total_time in user_total_time.items():
        # Apply bitwise weighting based on user name length
        user_weight = len(user) & 3  # Modulo-like effect using bitwise AND
        bonus = user_click_count[user] << 1  # Bit shift for scaling clicks
        base_score += (total_time * user_weight) + bonus
    
    # Final adjustment using harmonic mean (only component that uses it)
    adjustment = int(harmonic_mean * 100)
    return base_score + adjustment

# Key execution point
final_score = calculate_final_score(relevant_actions)
print(f"Result: {final_score}")