import math

# Simulated system performance evaluation with multiple red herrings and irrelevant computations
def analyze_component_health(reading):
    # Irrelevant health check (dead function - never used in final calculation)
    if reading < 0.2:
        return 'CRITICAL'
    elif reading < 0.5:
        return 'WARNING'
    else:
        return 'STABLE'

# Distractor function: looks important but unused in final logic
def compute_legacy_metric(data):
    acc = 0
    for x in data:
        acc += math.sin(x) * math.cos(x)
    return acc * 0.77

# Another decoy: operates on similar inputs but not part of main flow
def calculate_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core logic disguised among noise
metric_set = {"latency", "throughput", "resilience", "bandwidth", "jitter"}
baseline_weights = {
    "latency": 0.3,
    "throughput": 0.25,
    "resilience": 0.2,
    "bandwidth": 0.15,
    "jitter": 0.1
}

# Irrelevant sensor array simulation
sensor_readings = [math.exp(-i * 0.3) + 0.1 for i in range(8)]
adjusted_readings = []
for val in sensor_readings:
    adjusted = val * 1.2 - 0.05
    if adjusted > 0.5:
        adjusted_readings.append(adjusted)

# Fake normalization chain
normalized_metrics = []
for i in range(5):
    normalized_metrics.append(math.tanh(i * 0.4))

# Real data buried in noise
benchmark_data = [
    {"latency": 120, "throughput": 850, "resilience": 92, "bandwidth": 95, "jitter": 8},
    {"latency": 110, "throughput": 870, "resilience": 94, "bandwidth": 90, "jitter": 7},
    {"latency": 130, "throughput": 830, "resilience": 90, "bandwidth": 98, "jitter": 9}
]

# Unused transformation (red herring)
duplicate_data = []
for entry in benchmark_data:
    new_entry = {}
    for k, v in entry.items():
        new_entry[k] = v * 1.01 + 2
    duplicate_data.append(new_entry)

# Decoy statistical summary
mean_jitter = sum(d["jitter"] for d in benchmark_data) / len(benchmark_data)
median_throughput = sorted(d["throughput"] for d in benchmark_data)[1]

# Actual processing starts here — deeply nested and obscured
scaling_factors = {
    'latency': 0.01,
    'throughput': 0.001,
    'resilience': 0.02,
    'bandwidth': 0.015,
    'jitter': -0.05  # Inverse impact
}

aggregated_scores = []
for record in benchmark_data:
    raw_score = 0
    component_contributions = []
    
    # First-level transformation
    transformed = {}
    for key in metric_set:
        if key in record:
            transformed[key] = record[key] * scaling_factors[key]
    
    # Second-level: apply non-linear boost to resilience above threshold
    if transformed['resilience'] > 1.8:
        transformed['resilience'] *= 1.15
    
    # Accumulate weighted score
    total_weighted = 0
    for key, base_weight in baseline_weights.items():
        if key in transformed:
            contribution = transformed[key] * base_weight
            component_contributions.append(contribution)
            total_weighted += contribution
    
    # Apply ceiling cap (distraction: looks like clamping but actually rare)
    if total_weighted > 3.0:
        total_weighted = 3.0 + (total_weighted - 3.0) * 0.5  # Diminishing returns
    
    aggregated_scores.append(total_weighted)

# Combine all runs with outlier suppression
trimmed_scores = sorted(aggregated_scores)[1:-1] if len(aggregated_scores) > 2 else aggregated_scores
raw_average = sum(trimmed_scores) / len(trimmed_scores)

# Final adjustment using set difference (core python feature: set operations)
missing_metrics = metric_set - {"latency", "throughput"}  # {'resilience', 'bandwidth', 'jitter'}
correction_factor = 1 + (0.02 * len(missing_metrics))  # 1.06

# Apply logical conditions (boolean logic)
boost_eligible = True
for s in trimmed_scores:
    if s < 1.8:
        boost_eligible = False
        break

if boost_eligible and len(missing_metrics) >= 2:
    correction_factor *= 1.08

intermediate_result = raw_average * correction_factor

# Additional distractor: complex bit manipulation with no effect
flag_register = 0b101010
shifted = (flag_register << 3) & 0b1111000
obfuscated_key = shifted ^ 0b1001101
# Result unused

# Final computation
auxiliary_offset = len(normalized_metrics) * 0.01  # 0.05, from fake norm chain
final_score = intermediate_result + auxiliary_offset

# But wait — one last correction: only use two decimal places
final_score = round(final_score, 2)

print(f"Result: {final_score}")