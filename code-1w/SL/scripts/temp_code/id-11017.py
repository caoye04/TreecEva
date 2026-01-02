from collections import defaultdict
import math

# Simulated system metrics over time (key-value pairs)
raw_data = [
    {'cpu': 75, 'mem': 80, 'disk_io': 30, 'latency': 45},
    {'cpu': 60, 'mem': 85, 'disk_io': 25, 'latency': 40},
    {'cpu': 90, 'mem': 90, 'disk_io': 35, 'latency': 60},
    {'cpu': 55, 'mem': 70, 'disk_io': 20, 'latency': 35}
]

# Irrelevant transformation: converts to string lengths (red herring)
stringified = [str(d) for d in raw_data]
decoy_lengths = [len(s) for s in stringified]

# Aggregate metrics by key (relevant)
aggregated = defaultdict(list)
for entry in raw_data:
    for k, v in entry.items():
        aggregated[k].append(v)

# Compute mean values per metric (relevant)
means = {k: sum(v) / len(v) for k, v in aggregated.items()}

# Decoy function: uses lambda but doesn't contribute to final result
top_heavy = list(filter(lambda x: x > 70, [means['cpu'], means['mem'], means['disk_io'], means['latency']]))

def normalize(value, min_val=0, max_val=100):
    # Normalize to 0-1 scale
    return (value - min_val) / (max_val - min_val)

# Early normalization attempt (distractor)
normalized_latency = normalize(means['latency'], 0, 100)

# Baseline thresholds (arbitrary reference)
baseline = {
    'cpu': 70,
    'mem': 75,
    'disk_io': 25,
    'latency': 50
}

# Weighting scheme with decoy weights
weights = {
    'cpu': 0.3,
    'mem': 0.3,
    'disk_io': 0.1,  # De-emphasized
    'latency': 0.3
}

# Extra irrelevant structure: unused weight combinations
decoys = [
    {'cpu': 0.2, 'mem': 0.4, 'disk_io': 0.2, 'latency': 0.2},
    {'cpu': 0.4, 'mem': 0.1, 'disk_io': 0.1, 'latency': 0.4}
]

# Performance delta from baseline (relevant)
deltas = {}
for k in means:
    deltas[k] = means[k] - baseline[k]  # positive = worse than baseline

# Apply penalty scaling based on deviation magnitude
penalty_scale = {}
for k in deltas:
    if abs(deltas[k]) < 5:
        penalty_scale[k] = 1.0
    elif abs(deltas[k]) < 10:
        penalty_scale[k] = 1.5
    else:
        penalty_scale[k] = 2.0

# Compute weighted penalty (core logic)
weighted_penalty = 0
for k in means:
    weighted_penalty += abs(deltas[k]) * weights[k] * penalty_scale[k]

# Dummy transformations (dead code path)
if False:
    alternative = 0
    for k in means:
        alternative += (means[k] - 50) ** 0.5

# Secondary adjustment using trigonometric red herring (irrelevant)
angle_adjustment = math.sin(math.pi / 6) * 0.1  # Always 0.05, never used

# Critical computation hidden among distractors
efficiency_ratio = (means['cpu'] + means['mem']) / (means['disk_io'] + means['latency'] + 1)

# Main evaluation function
metrics = means.copy()

# Decoy list processing
buffer = [100]
for i in range(3):
    buffer.append(buffer[-1] - i*5)

# Unused recursive helper (misleading)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n - 2)

recursive_trace = [calculate_depth(i) for i in range(1, 6)]

# Final performance score calculation (answer depends only on this)
def evaluate_performance(metrics, baseline):
    score = 100.0  # starting score

    # CPU impact
    if metrics['cpu'] > baseline['cpu']:
        score -= (metrics['cpu'] - baseline['cpu']) * 1.2

    # Memory impact
    if metrics['mem'] > baseline['mem']:
        score -= (metrics['mem'] - baseline['mem']) * 1.5

    # Latency penalty with tiered response
    if metrics['latency'] > baseline['latency']:
        excess = metrics['latency'] - baseline['latency']
        if excess > 10:
            score -= excess * 2.0
        else:
            score -= excess * 1.8

    # Disk IO bonus if underutilized
    if metrics['disk_io'] < baseline['disk_io']:
        score += (baseline['disk_io'] - metrics['disk_io']) * 0.8

    # Overhead penalty if any metric exceeds 85%
    critical_count = 0
    for val in metrics.values():
        if val >= 85:
            critical_count += 1
    if critical_count > 0:
        score -= critical_count * 5

    return score

# Execute key statement
target_result = evaluate_performance(metrics, baseline)
final_score = target_result

# Print final answer as required
print(f"Result: {final_score}")