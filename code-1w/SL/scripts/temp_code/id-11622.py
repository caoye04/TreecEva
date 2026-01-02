import math

# Simulated sensor data processing with performance evaluation
raw_readings = [0.88, 0.91, 0.76, 0.94, 0.85, 0.89, 0.92, 0.83]
decoy_readings = [x ** 2 for x in raw_readings if x > 0.95]  # Irrelevant: no elements qualify

scaling_factor = 1.05
base_threshold = 0.87
adjustment_log = []

# Misleading normalization function (not used in final calculation)
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

def smooth_data(series, factor=0.1):
    smoothed = [series[0]]
    for i in range(1, len(series)):
        smoothed.append(smoothed[-1] * (1 - factor) + series[i] * factor)
    return smoothed

# Decoy transformation path (dead code path)
transform_options = {
    'basic': lambda x: x,
    'scaled': lambda x: x * scaling_factor,
    'squared': lambda x: x ** 2
}

# Actual metric computation pipeline
metric_data = [
    x for x in raw_readings 
    if x >= base_threshold - 0.03  # Filter near-threshold values
]

# Secondary filtering and transformation
filtered_metrics = []
for val in metric_data:
    if val >= base_threshold:
        filtered_metrics.append((val * 100) + 2.5)
    else:
        filtered_metrics.append((val * 95) + 1.8)

# Auxiliary tracking (distractor list)
performance_flags = []
for v in filtered_metrics:
    flag = 'high' if v > 90 else 'medium' if v > 85 else 'low'
    performance_flags.append(flag)

# Unused recursive helper (red herring)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n * 0.9 + calculate_depth(n - 1) * 0.1

# Real evaluation logic
state_history = []

for reading in raw_readings:
    state = 'optimal' if reading >= base_threshold else 'suboptimal'
    state_history.append(state)

# Core logic disguised among distractions
current_streak = 0
max_streak = 0
for state in state_history:
    if state == 'optimal':
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0

# Weighting based on streak and average
avg_metric = sum(filtered_metrics) / len(filtered_metrics)

# Conditional expression with distractor components
bonus = 10 if max_streak >= 3 else 5 if max_streak >= 2 else 0
penalty = 0
if 'suboptimal' in state_history[:3]:
    penalty = 3

# Final score depends only on avg_metric, bonus, penalty — others are decoys
final_score = 0
intermediate_deltas = []

for m in filtered_metrics:
    delta = m - 87.5
    intermediate_deltas.append(delta)

aggregate_deviation = sum([abs(d) for d in intermediate_deltas])

# The actual determining statement
final_score = evaluate_performance(metric_data, base_threshold)

# Critical function buried after noise
def evaluate_performance(data_list, threshold):
    above_count = len([x for x in data_list if x >= threshold])
    below_count = len(data_list) - above_count
    ratio = above_count / len(data_list) if data_list else 0
    base_score = ratio * 100
    streak_weight = max_streak * 1.5  # Uses captured max_streak from earlier
    return round(base_score + streak_weight + (10 if above_count >= 4 else 0), 4)

# Print result for verification
Result: {final_score}