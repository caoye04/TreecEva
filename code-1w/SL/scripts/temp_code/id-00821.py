def analyze_system_load(sensor_data, threshold=75):
    overload_count = 0
    for _, value in enumerate(sensor_data):
        if value > threshold:
            overload_count += 1
    return overload_count

# Irrelevant sensor data and analysis (distractor)
sensor_readings = [68, 72, 80, 91, 65, 77, 83]
irrelevant_overloads = analyze_system_load(sensor_readings)

# Simulated network packet sequence with bit flags (red herring)
network_packets = [0b1010, 0b1100, 0b1011, 0b0010]
error_mask = 0b1100
corrupted_count = 0
for packet in network_packets:
    if packet & error_mask == error_mask:
        corrupted_count += 1

# Historical performance snapshots (dead code path)
historical_snapshots = {
    'Q1': {'latency': 45, 'errors': 2},
    'Q2': {'latency': 52, 'errors': 1},
    'Q3': {'latency': 48, 'errors': 3}
}

# Benchmark weight configuration (actually used later)
benchmark_weights = {
    'response_time': 0.4,
    'throughput': 0.3,
    'stability': 0.2,
    'efficiency': 0.1
}

# Core metrics log - contains relevant data
metrics_log = [
    {'metric': 'response_time', 'raw': 120, 'baseline': 100},
    {'metric': 'throughput', 'raw': 850, 'baseline': 800},
    {'metric': 'stability', 'raw': 95, 'baseline': 100},
    {'metric': 'efficiency', 'raw': 78, 'baseline': 90}
]

# Auxiliary function to compute deviation ratio
def compute_deviation(value, base):
    return abs(value - base) / base

# Complex evaluation pipeline
status_flags = {key: False for key in benchmark_weights}
adjusted_scores = []

for idx, entry in enumerate(metrics_log):
    name = entry['metric']
    raw_val = entry['raw']
    base_val = entry['baseline']
    
    # Compute normalized deviation
    deviation = compute_deviation(raw_val, base_val)
    
    # Apply non-linear penalty curve (quadratic)
    penalty = deviation ** 2
    score = max(0, 100 * (1 - penalty))
    
    # Update status based on threshold
    if score >= 85:
        status_flags[name] = True
    
    adjusted_scores.append((name, score))

# Weighted aggregation using dictionary and zip
weighted_components = {}
for (name, score), (weight_name, weight) in zip(adjusted_scores, sorted(benchmark_weights.items())):
    weighted_components[name] = score * weight

# Secondary adjustment based on flag activation count
active_indicators = sum(1 for flag in status_flags.values() if flag)
boost_factor = 1 + (active_indicators * 0.05)  # Up to 20% boost

# Final performance evaluation
composite_base = sum(weighted_components.values())
temp_adjustment = composite_base * 0.1  # Distractor variable, not used
final_score = composite_base * boost_factor

# Decoy calculation with combinatorics (unused)
def calculate_combinations(n, r):
    if r > n or r < 0:
        return 0
    result = 1
    for i in range(min(r, n - r)):
        result = result * (n - i) // (i + 1)
    return result

# Unused combinatoric analysis
theoretical_paths = calculate_combinations(10, 3)

# Spurious logging (no effect)
log_entry = f"Performance run complete: {final_score:.2f}"
debug_payload = [f"{k}:{v}" for k, v in weighted_components.items()]

# Critical output
print(f"Result: {final_score}")