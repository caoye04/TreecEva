def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    for entry in logs:
        if 'start' in entry:
            total_hours += entry['duration']
        if entry.get('status') == 'idle':
            idle_periods += 1
    efficiency = (total_hours - idle_periods) / max(total_hours, 1)
    return efficiency

logs_data = [
    {'start': True, 'duration': 2, 'status': 'active'},
    {'start': True, 'duration': 3, 'status': 'idle'},
    {'start': False, 'duration': 1, 'status': 'idle'},
    {'start': True, 'duration': 4, 'status': 'active'}
]

productivity_rate = analyze_productivity(logs_data)

# Irrelevant distraction: Unused function
def calculate_redundancy_factor(data):
    return len(data) ** 2 + sum(d.get('duration', 0) for d in data)

# Distractor variables
temp_result = [x['duration'] for x in logs_data if x.get('status') == 'idle']
redundant_sum = sum(temp_result) * 2  # Unused computation
phantom_value = len(logs_data) > 5 and productivity_rate < 0.5  # Dead logic

# Real work begins: Metric evaluation with distractors
raw_metrics = {
    'accuracy': 0.92,
    'latency': 45,
    'throughput': 88,
    'consistency': 0.87,
    'availability': 0.95
}

weights = {
    'accuracy': 0.3,
    'latency': -0.1,  # Negative weight: lower is better
    'throughput': 0.2,
    'consistency': 0.25,
    'availability': 0.15
}

# Distractor: Unused alternate weighting
dummy_weights = {k: 1/len(weights) for k in weights}

# Transform metrics: normalize latency inversely
transformed = {}
for key, val in raw_metrics.items():
    if key == 'latency':
        transformed[key] = 100 / (val + 1) if val > 0 else 0
    else:
        transformed[key] = val

# Another red herring: set operation with no impact
duplicate_keys = set(raw_metrics.keys()) & set({'speed', 'accuracy', 'latency'})
key_count = len(duplicate_keys)  # Used nowhere

# More distractions: list comprehension with side storage
evaluation_snapshots = [
    f"{metric}: {transformed[metric]:.2f}" 
    for metric in sorted(transformed.keys())
]
snapshot_size = len(evaluation_snapshots)  # Unused

# Core logic buried among noise
def evaluate_performance(metrics, weights):
    score = 0.0
    for k in metrics:
        if k == 'latency':
            # Already transformed, now apply negative weight as positive gain
            score += metrics[k] * abs(weights[k])
        else:
            score += metrics[k] * weights[k]
    # Additional adjustment based on productivity (hidden dependency)
    global productivity_rate
    score *= (1 + 0.1 * productivity_rate)  # Boost by productivity factor
    return round(score, 4)

# Decoy function call (never executed)
# final_score = evaluate_performance(raw_metrics, dummy_weights)

# Actual execution path
final_score = evaluate_performance(transformed, weights)

# Irrelevant sorting
sorted_metrics = sorted(transformed.items(), key=lambda x: x[1], reverse=True)

# Print result as required
print(f"Target result: {final_score}")