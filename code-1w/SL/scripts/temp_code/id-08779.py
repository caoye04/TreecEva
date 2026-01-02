def analyze_productivity(logs):
    total_hours = sum([entry['hours'] for entry in logs])
    idle_count = len([e for e in logs if e['idle']])
    efficiency = (total_hours - idle_count * 0.5) / total_hours if total_hours > 0 else 0
    return efficiency

logs_data = [
    {'day': 'Mon', 'hours': 8, 'idle': False},
    {'day': 'Tue', 'hours': 7, 'idle': True},
    {'day': 'Wed', 'hours': 9, 'idle': False},
    {'day': 'Thu', 'hours': 6, 'idle': True},
    {'day': 'Fri', 'hours': 8, 'idle': False}
]

productivity_rate = analyze_productivity(logs_data)

# Irrelevant distraction: system health simulation
def monitor_system_health(timestamps):
    cpu_loads = [t % 77 for t in timestamps]
    avg_load = sum(cpu_loads) / len(cpu_loads)
    warnings = [load for load in cpu_loads if load > 50]
    return len(warnings) > 3

timestamps = [120, 125, 130, 135, 140, 145, 150]
system_alert = monitor_system_health(timestamps)

# Real computation begins — performance metrics
base_metrics = [85, 90, 78, 92, 88]
weight_map = {'punctuality': 0.2, 'output': 0.3, 'collaboration': 0.15, 'innovation': 0.25, 'attendance': 0.1}
weights = list(weight_map.values())

# Distractor: unused alternate weighting
alt_weights = [0.1, 0.4, 0.2, 0.2, 0.1]  # never used

# Transform base metrics using productivity adjustment
adjusted_metrics = [m * (1 + 0.1 * productivity_rate) for m in base_metrics]

# Add dummy transformation with enumerate and string method red herring
dummy_labels = ['A', 'B', 'C', 'D', 'E']
label_shift = ''.join([label.lower() for label in dummy_labels]).count('a')  # evaluates to 1, unused

# Use of zip and lambda — relevant only through filtering effect
metric_pairs = list(zip(adjusted_metrics, weights))
filter_fn = lambda x: x[0] >= 80
filtered_pairs = [pair for pair in metric_pairs if filter_fn(pair)]

# Simulate conditional boost for high performers
boost_applied = False
if len(filtered_pairs) >= 3:
    adjusted_metrics = [m * 1.05 for m in adjusted_metrics]
    boost_applied = True

# Another distraction: recursive decoy function
def calculate_entropy(data, depth=0):
    if depth >= 3 or sum(data) < 10:
        return 0.0
    return data[0] % 10 + calculate_entropy(data[1:], depth + 1)

entropy_value = calculate_entropy(base_metrics)  # computed but not used

# Core evaluation logic
combined_metric = sum(m * w for m, w in zip(adjusted_metrics, weights))
penalty = 0.0
if boost_applied:
    outlier_count = len([m for m in adjusted_metrics if m > 95])
    penalty = outlier_count * 2.5

raw_score = combined_metric - penalty

# Final normalization step
max_possible = sum([100 * w for w in weights])
normalized_score = (raw_score / max_possible) * 100

# Decoy array operations
buffer = [0] * 10
for i in range(len(buffer)):
    buffer[i] = i * 11 % 7
checksum = sum(buffer)  # irrelevant

# Final scoring with distractor condition
scaling_factor = 1.0
if checksum > 30:
    scaling_factor = 0.95  # never triggers

final_score = round(normalized_score * scaling_factor, 4)

# Output target result
print(f"Result: {final_score}")