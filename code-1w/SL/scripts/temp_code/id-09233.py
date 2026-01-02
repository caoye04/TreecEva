import itertools

# Real data processing scenario: system performance evaluation with noise

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def apply_discount(factor):
    # Irrelevant recursive discount logic (dead-end)
    if factor < 0.1:
        return factor
    return apply_discount(factor * 0.9)

def analyze_trend(data):
    # Unused trend analyzer (distractor function)
    increasing = sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    decreasing = sum(1 for i in range(1, len(data)) if data[i] < data[i-1])
    return 'upward' if increasing > decreasing else 'downward'

def filter_outliers(values, threshold=2.0):
    mean = sum(values) / len(values)
    std = (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean) <= threshold * std]

# Simulated sensor readings (with decoy entries)
sensor_data = [89, 102, 95, 450, 93, 87, 91, 200, 89, 96]  # 450 and 200 are outliers

# Irrelevant transformation chain
temp_log = list(map(lambda x: round(x ** 0.5, 2), filter(lambda y: y < 150, sensor_data)))
duplicate_check = {x for x in sensor_data if sensor_data.count(x) > 1}

# Core metrics (only these matter)
raw_metrics = {
    'latency': 94.0,      # ms
    'throughput': 87.0,   # ops/sec
    'accuracy': 95.0,     # %
    'stability': 89.0,    # stability index
    'bandwidth': 91.0     # Mbps
}

# Weighting scheme (critical for final score)
weights = [0.2, 0.25, 0.3, 0.15, 0.1]  # Sum = 1.0

# Distractor: unused alternate weights
cost_weights = [0.1, 0.1, 0.5, 0.2, 0.1]

# Normalize each metric to 0-1 scale using realistic bounds
bounds = [
    (50, 100),  # latency: lower is better → inverted
    (50, 120),  # throughput
    (80, 100),  # accuracy
    (70, 100),  # stability
    (60, 120)   # bandwidth
]

# Inversion flags: 1 if higher is better, -1 if lower is better
inversion = [-1, 1, 1, 1, 1]

# Apply filtering to sensor-derived stability proxy (but we already have stability)
filtered_sensors = filter_outliers(sensor_data)
avg_sensor = sum(filtered_sensors) / len(filtered_sensors) if filtered_sensors else 0

# Fake adjustment branch (never taken due to condition)
if len(duplicate_check) > 10:
    raw_metrics['stability'] = avg_sensor

# Generate all pairwise combinations of metrics (irrelevant)
pair_keys = list(itertools.combinations(raw_metrics.keys(), 2))
pair_sums = {pair: raw_metrics[pair[0]] + raw_metrics[pair[1]] for pair in pair_keys}

# Extract values in correct order
metric_values = [
    raw_metrics['latency'],
    raw_metrics['throughput'],
    raw_metrics['accuracy'],
    raw_metrics['stability'],
    raw_metrics['bandwidth']
]

# Normalize with inversion
normalized = []
for i, (val, bound, inv) in enumerate(zip(metric_values, bounds, inversion)):
    norm = normalize(val, *bound)
    normalized.append(norm if inv == 1 else 1 - norm)

# Weighted sum calculation (this is the real logic)
weighted_sum = sum(w * n for w, n in zip(weights, normalized))

# Secondary adjustment based on trend (but trend is ignored)
trend_signal = analyze_trend([90, 92, 93, 94, 95])  # Simulated history
trend_bonus = 0.02 if trend_signal == 'upward' else -0.01

# Final score computation (target statement)
final_score = weighted_sum  # No bonus applied; distraction only

# Decoy transformations on final_score
adjusted_score = final_score * 1.05
ceiling_score = int(adjusted_score + 0.5)
score_category = 'High' if final_score >= 0.8 else 'Low'

# Debug logs (irrelevant prints)
#print(f'Debug - Normalized: {normalized}')
#print(f'Debug - Pair sums: {list(pair_sums.values())[:3]}')

# Output the required result
print(f"Result: {final_score}")