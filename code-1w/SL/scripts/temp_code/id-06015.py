from collections import defaultdict
from itertools import combinations

# Simulate sensor data readings with timestamps and types
data = [
    {'type': 'temp', 'value': 23.5, 'time': 10},
    {'type': 'temp', 'value': 25.1, 'time': 15},
    {'type': 'pressure', 'value': 1013, 'time': 12},
    {'type': 'humidity', 'value': 45, 'time': 10},
    {'type': 'temp', 'value': 22.8, 'time': 20},
    {'type': 'pressure', 'value': 1015, 'time': 18},
    {'type': 'humidity', 'value': 50, 'time': 25}
]

# Thresholds for anomaly detection
thresholds = {
    'temp': (20, 30),
    'pressure': (950, 1030),
    'humidity': (30, 70)
}

# Misleading auxiliary variables (distractors)
total_readings = len(data)
duplicate_check = set()
anomaly_flags = []
aggregated_stats = defaultdict(list)
summary_report = {}

# Group data by type for analysis
for entry in data:
    aggregated_stats[entry['type']].append(entry['value'])

# Compute basic statistics (some used, some not)
avg_values = {}
for k, v_list in aggregated_stats.items():
    avg_values[k] = sum(v_list) / len(v_list)

# Dead code path - never executed but looks relevant
if False:
    print("Debug mode active")
    for t in data:
        t['processed'] = False

# Simulate combination-based correlation check (unused but plausible)
correlation_pairs = list(combinations(aggregated_stats.keys(), 2))
spurious_correlation_score = 0
for pair in correlation_pairs:
    spurious_correlation_score += len(aggregated_stats[pair[0]]) * len(aggregated_stats[pair[1]])

# Real logic: count how many readings are within threshold
valid_count = 0
out_of_range = []
for entry in data:
    low, high = thresholds[entry['type']]
    if low <= entry['value'] <= high:
        valid_count += 1
    else:
        out_of_range.append(entry)

# Secondary validation: only trust readings within time window [10, 20]
time_filtered_valid = 0
for entry in data:
    low, high = thresholds[entry['type']]
    if 10 <= entry['time'] <= 20 and low <= entry['value'] <= high:
        time_filtered_valid += 1

# Auxiliary computation: weighted contribution (only temp matters in final score)
weighted_contributions = []
for entry in data:
    weight = 1.0
    if entry['type'] == 'temp':
        weight = 1.5
    elif entry['type'] == 'pressure':
        weight = 0.8
    weighted_contributions.append(entry['value'] * weight)

# Final scoring logic
base_score = valid_count * 10
adjustment = len(out_of_range) * -5
temp_bonus = 0
for entry in data:
    if entry['type'] == 'temp' and entry['value'] > 24:
        temp_bonus += 3

# Critical statement
final_score = compute_final_score(data, thresholds)

# Red herring function that looks important but isn't used in main logic
def analyze_trend(values):
    return max(values) - min(values) if len(values) > 1 else 0

# Actual function used in final score
def compute_final_score(data, thresholds):
    valid_count = 0
    for entry in data:
        t = entry['type']
        v = entry['value']
        if thresholds[t][0] <= v <= thresholds[t][1]:
            valid_count += 1
    bonus = 0
    temp_vals = [e['value'] for e in data if e['type'] == 'temp']
    if len(temp_vals) >= 2 and temp_vals[-1] > temp_vals[-2]:
        bonus = 7
    return valid_count * 8 + bonus

# Print result for evaluation
Result: {final_score}