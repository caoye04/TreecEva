from collections import defaultdict, Counter
import math

# Simulated system telemetry data (irrelevant in part)
telemetry_logs = [
    {'cpu': 75, 'mem': 80, 'disk': 40},
    {'cpu': 80, 'mem': 60, 'disk': 50},
    {'cpu': 90, 'mem': 95, 'disk': 30}
]

# Irrelevant helper function (dead code path)
def analyze_telemetry(logs):
    stats = defaultdict(int)
    for log in logs:
        for k, v in log.items():
            stats[k] += v
    return {k: v / len(logs) for k, v in stats.items()}

# Unused transformation map
telemetry_weights = {'cpu': 0.4, 'mem': 0.35, 'disk': 0.25}

# Core data for evaluation (relevant)
raw_input = """
error_rate=0.02|latency_ms=120|throughput=850|consistency=high|availability=zoned
error_rate=0.05|latency_ms=200|throughput=400|consistency=medium|availability=global
error_rate=0.01|latency_ms=90|throughput=950|consistency=high|availability=local
"""

# Parse input into list of dicts (relevant)
entries = []
for line in raw_input.strip().split('\n'):
    record = {}
    for pair in line.split('|'):
        k, v = pair.split('=')
        try:
            record[k] = float(v) if '.' in v or k == 'latency_ms' or k == 'throughput' else v
        except ValueError:
            record[k] = v
    entries.append(record)

# Extract numeric metrics (relevant)
numeric_metrics = [
    {k: v for k, v in e.items() if isinstance(v, (int, float))} for e in entries
]

# Compute aggregates with distraction logic
aggregates = defaultdict(float)
for metric in ['error_rate', 'latency_ms', 'throughput']:
    values = [e[metric] for e in numeric_metrics]
    if metric == 'error_rate':
        aggregates['avg_error'] = sum(values) / len(values)
        aggregates['min_error'] = min(values)
    elif metric == 'latency_ms':
        aggregates['max_latency'] = max(values)
        # Distractor computation
        aggregates['latency_variance'] = sum((x - sum(values)/len(values))**2 for x in values) / len(values)
    elif metric == 'throughput':
        aggregates['total_throughput'] = sum(values)
        aggregates['throughput_efficiency'] = sum(values) / (max(values) * len(values))

# Benchmark thresholds (relevant)
benchmark_data = {
    'error_threshold': 0.03,
    'latency_cap': 150,
    'min_throughput': 600
}

# Scoring weights (partially irrelevant)
score_weights = defaultdict(lambda: 1.0)
score_weights.update({'error_rate': 1.5, 'latency_ms': 1.2, 'throughput': 1.0})

# Decoy scoring using lambda (distractor)
penalty_curve = lambda x, threshold: 100 * (math.exp((x - threshold) / threshold) if x > threshold else 0)

# Real scoring logic (nested conditions and counters)
def evaluate_performance(metrics, benchmarks):
    # Initialize counters
    performance_log = []
    category_counts = Counter()

    for entry in entries:
        score = 100.0
        # Primary checks
        if entry['error_rate'] <= benchmarks['error_threshold']:
            score += 10
            category_counts['stability'] += 1
        else:
            score -= 15

        if entry['latency_ms'] <= benchmarks['latency_cap']:
            score += 15
            category_counts['responsiveness'] += 1
        else:
            score -= 20
            # Fake compensation (misleading)
            fallback_boost = 5 if entry['availability'] == 'global' else 0
            score += fallback_boost  # Irrelevant due to net loss

        if entry['throughput'] >= benchmarks['min_throughput']:
            score += 25
            category_counts['capacity'] += 1
        else:
            score -= 10

        # Consistency bonus (red herring - not in benchmark)
        if entry['consistency'] == 'high':
            consistency_bonus = 8
            score += consistency_bonus  # Slight boost but not critical

        # Availability-based penalty (distractor)
        availability_map = {'local': 0, 'zoned': -5, 'global': -2}
        score += availability_map.get(entry['availability'], 0)

        performance_log.append(score)

    # Final aggregation logic (key)
    base_final = sum(performance_log) / len(performance_log)
    count_bonus = len([c for c in category_counts.values() if c >= 2]) * 7
    stability_penalty = 0
    
    # Critical adjustment based on aggregate statistics
    if aggregates['avg_error'] > benchmark_data['error_threshold']:
        stability_penalty = 12
    
    final_normalized = base_final + count_bonus - stability_penalty
    
    # Apply non-linear compression (only if high efficiency)
    if aggregates['throughput_efficiency'] > 0.7:
        final_normalized = final_normalized * 0.95 + 30  # Diminishing returns
    
    return int(round(final_normalized))

# Execute main logic
final_score = evaluate_performance(numeric_metrics, benchmark_data)

# Print result as required
print(f"Target result: {final_score}")