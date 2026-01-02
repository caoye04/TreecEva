import math

# Simulated telemetry data from sensor array
telemetry_stream = [147, 255, 193, 98, 201, 164, 112, 229, 177, 134]

# Irrelevant signal processing (dead path)
def process_signal(data):
    return [x ^ 0xFF for x in data]

signal_filtered = process_signal(telemetry_stream)  # Unused downstream

# Core system: Network node performance evaluator
node_metrics = {
    'latency': [12, 15, 14, 18, 13],
    'bandwidth': [98, 92, 95, 88, 100],
    'reliability': [0.991, 0.987, 0.993, 0.979, 0.995]
}

baseline_thresholds = {
    'latency': 16,
    'bandwidth': 90,
    'reliability': 0.985
}

# Decoy function: Looks important but unused
def calculate_stress_load(metrics):
    stress = 0
    for val in metrics['latency']:
        stress += max(0, val - 10) ** 2
    return stress / len(metrics['latency'])

# Auxiliary transformation (used indirectly)
def normalize(values, upper=100):
    return [round((x / upper) * 100, 2) for x in values]

# Scoring weights (misleading weight set)
weights_v1 = {'latency': 0.3, 'bandwidth': 0.4, 'reliability': 0.3}  # Not used
weights_v2 = {'latency': 0.2, 'bandwidth': 0.3, 'reliability': 0.5}  # Used

# Historical comparison dataset (distractor)
historical_avg = {
    'latency': 14.2,
    'bandwidth': 93.1,
    'reliability': 0.986
}

# Bit manipulation red herring
def scramble_key(n):
    n = ((n << 3) & 0xFF) | (n >> 5)
    n ^= 0b10101010
    n = (n + 17) % 256
    return n

key_lookup = {i: scramble_key(i) for i in range(10)}  # Unused

# Real evaluation logic begins
metric_set = set(node_metrics.keys())
benchmark_data = {}

for key in metric_set:
    if key == 'latency':
        # Invert to make lower latency better
        norm_vals = normalize([baseline_thresholds[key] - x for x in node_metrics[key]], 4)
        benchmark_data[key] = sum(norm_vals) / len(norm_vals)
    elif key == 'bandwidth':
        norm_vals = normalize(node_metrics[key])
        benchmark_data[key] = sum(norm_vals) / len(norm_vals)
    else:
        # reliability and others
        scaled = [r * 100 for r in node_metrics[key]]
        benchmark_data[key] = sum(scaled) / len(scaled)

# Secondary transformation using slicing
transformed_scores = []
for k in sorted(benchmark_data.keys()):
    chunk = [benchmark_data[k] + i*0.1 for i in range(2)]
    transformed_scores.extend(chunk[::1])  # Redundant slice

# Composite score construction
temp_offset = 0
for i, val in enumerate(transformed_scores):
    if i % 3 == 0:
        temp_offset += math.sin(math.pi / (val + 1))

# Final evaluation with correct weights
def evaluate_performance(metrics, data):
    w = weights_v2  # Critical: uses v2, not v1
    score = 0.0
    
    # Additional distraction: set difference
    expected_metrics = {'latency', 'bandwidth', 'reliability', 'jitter'}
    present = metrics.intersection(expected_metrics)
    missing_penalty = 10 * (len(expected_metrics) - len(present))  # Always 10 here
    
    for m in metrics:
        contribution = data[m] * w[m]
        score += contribution
    
    # Apply non-linear bonus for high reliability
    if data['reliability'] > 99.0:
        score *= 1.05
    
    # Misleading adjustment
    magic_factor = sum(key_lookup.values()) % 50  # Large irrelevant computation
    magic_factor -= 25  # Center around zero
    
    final = score - missing_penalty + (temp_offset * 2) - 1.23
    return int(round(final * 10)) / 10.0  # One decimal precision

# Execution point of interest
final_score = evaluate_performance(metric_set, benchmark_data)

print(f"Target result: {final_score}")