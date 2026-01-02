from collections import defaultdict
import itertools

# Simulate system performance metrics over time
metrics = [
    {'cpu': 70, 'mem': 65, 'latency': 45, 'throughput': 80},
    {'cpu': 85, 'mem': 70, 'latency': 50, 'throughput': 75},
    {'cpu': 60, 'mem': 80, 'latency': 40, 'throughput': 85},
    {'cpu': 90, 'mem': 85, 'latency': 60, 'throughput': 60}
]

baseline = {
    'cpu': 75,
    'mem': 75,
    'latency': 50,
    'throughput': 75
}

# Auxiliary tracking for irrelevant analysis (distractor)
timing_phases = ['init', 'warmup', 'steady', 'cooldown']
phase_data = defaultdict(list)
for i, phase in enumerate(timing_phases):
    phase_data[phase].append(metrics[i]['cpu'])
    phase_data[phase].append(metrics[i]['mem'])

# Misleading trend analysis (dead computation path)
avg_trends = {}
for key in ['cpu', 'mem', 'latency', 'throughput']:
    values = [m[key] for m in metrics]
    avg_trends[key] = sum(values) / len(values)
    # This is computed but not used later (irrelevant)

# Helper function to compute weighted deviation
def compute_deviation(record, base):
    deviation = 0.0
    weights = {'cpu': 0.2, 'mem': 0.2, 'latency': 0.3, 'throughput': 0.3}
    for k in record:
        diff = abs(record[k] - base[k])
        deviation += diff * weights[k]
    return deviation

# Secondary helper with red herring logic
def analyze_stability(records):
    stability = 0
    for r in records:
        # Complex but unused metric
        if r['cpu'] > 80 and r['mem'] > 80:
            stability -= 5
        elif r['latency'] < 45:
            stability += 2
    return stability  # Never actually used

# Real processing begins here
smoothed_metrics = []
for m in metrics:
    smoothed = {k: v * 0.9 for k, v in m.items()}  # Apply damping
    smoothed_metrics.append(smoothed)

# Compute deviation for each record
deviations = [compute_deviation(m, baseline) for m in smoothed_metrics]

# Aggregate total deviation (semi-relevant but transformed)
total_dev = sum(deviations)

# Simulate correction factor based on pattern cycles (itertools usage)
cycle_pattern = list(itertools.cycle([1, -1]))
correction = 0
for i, dev in enumerate(deviations):
    correction += dev * cycle_pattern[i % 2]

# Final performance score calculation
base_score = 100
penalty = int(total_dev)
effective_correction = abs(correction) // 10

# Critical statement
final_score = evaluate_performance(metrics, baseline)

# Actual implementation of evaluate_performance
def evaluate_performance(data, ref):
    cumulative = 0
    count = 0
    for entry in data:
        for k, v in entry.items():
            threshold = ref[k] * 1.1 if k == 'throughput' else ref[k] * 0.9
            if (k == 'throughput' and v >= threshold) or (k != 'throughput' and v <= threshold):
                cumulative += 1
        count += 1
    return (cumulative * 10) // count  # Score per condition met

# Print final result
print(f"Result: {final_score}")