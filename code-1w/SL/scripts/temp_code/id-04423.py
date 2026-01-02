from collections import defaultdict, Counter

# Simulated system performance monitoring with irrelevant metrics
def monitor_system_load(cpu_readings, memory_snapshots):
    load_profile = defaultdict(float)
    peak_memory = max(memory_snapshots) if memory_snapshots else 0
    avg_cpu = sum(cpu_readings) / len(cpu_readings) if cpu_readings else 0

    for i, reading in enumerate(cpu_readings):
        load_profile[f'cpu_{i}'] = reading * 1.1

    # Distractor: Memory fragmentation index (not used later)
    frag_index = sum(1 for x in memory_snapshots if x < peak_memory * 0.3)

    return {'avg_cpu': avg_cpu, 'peak_mem': peak_memory}

# Irrelevant utility function for network stats
def calculate_network_efficiency(packets, latency):
    if not packets:
        return 0.0
    good_packets = sum(1 for p in packets if p > 0)
    efficiency = good_packets / len(packets)
    penalty = sum(latency) / len(latency) if latency else 0
    return efficiency - penalty * 0.01  # Unused result

# Core evaluation logic with distractors
def analyze_component_stability(readings_list):
    stability = {}
    cumulative_drift = 0

    for idx, series in enumerate(readings_list):
        diffs = [abs(series[i] - series[i-1]) for i in range(1, len(series))] if len(series) > 1 else [0]
        avg_drift = sum(diffs) / len(diffs)
        cumulative_drift += avg_drift

        # Red herring: store but never use individual stability scores
        stability[f'component_{idx}'] = 1 / (1 + avg_drift) if avg_drift > 0 else 1

    # Return only cumulative value actually used
    return cumulative_drift

# Main scoring algorithm with multiple distractions
def evaluate_performance(metrics_log, benchmark_weights):
    base_scores = []
    adjustment_factor = 0.0

    # Real data processing mixed with noise
    for entry in metrics_log:
        raw_value = entry['value']
        category = entry['type']
        timestamp = entry['ts']  # Unused

        weight = benchmark_weights.get(category, 0.5)
        normalized = raw_value * weight

        # Real computation path
        if category == 'throughput':
            base_scores.append(normalized * 1.2)
        elif category == 'latency':
            base_scores.append(1000 / (normalized + 1))  # Avoid division by zero
        elif category == 'error_rate':
            base_scores.append(max(0, 100 - normalized * 10))

        # Distractor block: fake anomaly detection
        if raw_value > 90 and category != 'error_rate':
            adjustment_factor += 0.05  # Never applied
        elif raw_value < 5:
            adjustment_factor -= 0.02  # Dead code path

    # Real accumulation
    total_base = sum(base_scores)

    # Fake transformation chain
    transformed = [x ** 0.5 for x in base_scores if x > 10]
    shrink_factor = sum(transformed) / len(transformed) if transformed else 0

    # Another red herring: entropy calculation
    score_counter = Counter([round(x) for x in base_scores])
    entropy = 0.0
    n = sum(score_counter.values())
    for count in score_counter.values():
        p = count / n
        entropy -= p * __import__('math').log(p) if p > 0 else 0

    # Actual final computation
    raw_final = total_base * 0.85

    # Final adjustment using unrelated system data
    system_data = monitor_system_load([75, 80, 85, 90], [400, 420, 430, 380, 450])
    cpu_bonus = 5 if system_data['avg_cpu'] > 80 else 0

    final_score = int(raw_final + cpu_bonus)

    return final_score

# Setup realistic input data
metrics_log = [
    {'type': 'throughput', 'value': 85, 'ts': 1645000},
    {'type': 'latency', 'value': 15, 'ts': 1645001},
    {'type': 'error_rate', 'value': 0.8, 'ts': 1645002},
    {'type': 'throughput', 'value': 92, 'ts': 1645003},
    {'type': 'latency', 'value': 12, 'ts': 1645004}
]

benchmark_weights = {
    'throughput': 1.1,
    'latency': 0.9,
    'error_rate': 1.3
}

# Call the main function - this produces the answer
final_score = evaluate_performance(metrics_log, benchmark_weights)

# Evaluate component drift (distractor, not affecting final_score)
drift_total = analyze_component_stability([
    [100, 98, 101, 99],
    [200, 195, 198, 203],
    [50, 52, 49, 51]
])

# Network efficiency (completely irrelevant)
network_result = calculate_network_efficiency([10, 10, 0, 10, 5], [20, 25, 30, 22])

# Print result as required
print(f"Result: {final_score}")