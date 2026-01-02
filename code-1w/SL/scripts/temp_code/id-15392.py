from collections import defaultdict

# Simulate system performance metrics over time
timestamps = [100, 101, 102, 103, 104]
raw_data = [
    {'cpu': 75, 'mem': 80, 'io': 20},
    {'cpu': 60, 'mem': 75, 'io': 25},
    {'cpu': 80, 'mem': 85, 'io': 15},
    {'cpu': 70, 'mem': 70, 'io': 30},
    {'cpu': 65, 'mem': 60, 'io': 35}
]

# Accumulate metric history
metric_history = defaultdict(list)
for entry in raw_data:
    for k, v in entry.items():
        metric_history[k].append(v)

# Compute moving averages (distraction: not used later)
moving_averages = {}
for key, values in metric_history.items():
    avg = sum(values[:3]) / 3  # only first 3
    moving_averages[key] = round(avg, 2)

# Extract latest readings
latest_metrics = {k: v[-1] for k, v in metric_history.items()}

# Normalize metrics to 0-100 scale (some are already, but pretend)
normalized = {}
for k, v in latest_metrics.items():
    if k == 'cpu':
        normalized[k] = min(v, 100)
    elif k == 'mem':
        normalized[k] = min(v, 100)
    elif k == 'io':
        normalized[k] = max(10 - v, 0)  # inverted: lower IO wait is better

# Irrelevant transformation: set operations on keys
key_set_a = set(metric_history.keys())
key_set_b = {'cpu', 'gpu', 'mem', 'io'}
overlap = key_set_a & key_set_b  # {'cpu', 'mem', 'io'}
disjoint = key_set_b - key_set_a  # {'gpu'}

# Weighted scoring model
weights = {
    'cpu': 0.4,
    'mem': 0.35,
    'io': 0.25
}

# Distractor: unused weight adjustment
if 'gpu' not in latest_metrics:
    temp_weight = weights['io'] * 0.1
    weights['io'] -= temp_weight  # minor tweak, but not actually meaningful

# Another distraction: slicing and processing older data
historical_slice = metric_history['cpu'][1:4]  # middle three values
spike_count = sum(1 for x in historical_slice if x > 70)

# Real evaluation function
def evaluate_performance(metrics, w):
    total = 0.0
    for name, val in metrics.items():
        if name == 'io':
            # Special handling: we inverted earlier
            contribution = val * w[name] * 1.1  # slight boost factor
        else:
            contribution = val * w[name]
        total += contribution
    
    # Add bonus if memory under threshold (even if not reached)
    if metrics.get('mem') < 65:
        total += 5
    else:
        dummy_bonus = 2  # dead code path: not added
    
    return int(total)  # discretize final score

# Critical execution point
final_score = evaluate_performance(normalized, weights)

# Print result
print(f"Result: {final_score}")