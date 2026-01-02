from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_records = [
    {'node': 'A', 'load': 78, 'errors': 2, 'response_time': 120, 'active': True},
    {'node': 'B', 'load': 95, 'errors': 5, 'response_time': 200, 'active': False},
    {'node': 'A', 'load': 60, 'errors': 1, 'response_time': 90, 'active': True},
    {'node': 'C', 'load': 88, 'errors': 3, 'response_time': 180, 'active': True},
    {'node': 'B', 'load': 45, 'errors': 0, 'response_time': 110, 'active': True},
    {'node': 'C', 'load': 77, 'errors': 4, 'response_time': 160, 'active': True}
]

# Irrelevant helper (distractor)
def analyze_throughput(data):
    total = sum(entry['response_time'] for entry in data if entry['load'] > 80)
    return total // len(data) if data else 0

# Misleading preprocessing step (dead path)
raw_stats = defaultdict(int)
for record in task_records:
    raw_stats[record['node']] += record['errors']

# Decoy transformation
error_rankings = sorted(raw_stats.items(), key=lambda x: x[1], reverse=True)
penalty_map = {item[0]: idx * 10 for idx, item in enumerate(error_rankings)}

# Real metric aggregation
metrics = defaultdict(list)
for record in task_records:
    if record['active']:
        metrics[record['node']].append((record['load'], record['response_time']))

# Another distraction: string-based node analysis (irrelevant to final result)
nodes_str = ''.join(sorted(set(metrics.keys())))
checksum = sum(ord(c) for c in nodes_str) % 100

# Compute aggregated node performance (only this matters)
aggregated = {}
for node, values in metrics.items():
    avg_load = sum(v[0] for v in values) / len(values)
    avg_response = sum(v[1] for v in values) / len(values)
    # Composite score with weighted penalties
    score = avg_load * 0.6 + (100 - min(avg_response, 100)) * 0.4
    aggregated[node] = round(score, 2)

# Baseline comparison reference (key control structure)
baseline = {
    'A': 75.0,
    'B': 68.5,
    'C': 70.0
}

# Complex conditional scoring logic with red herring variables
def evaluate_performance(perf_data, ref):
    adjustment_factor = 1.05
    volatility_index = 0  # unused distractor
    compliance_log = []   # dead variable
    
    total_deviation = 0.0
    node_count = 0
    
    for node, current in perf_data.items():
        if node not in ref:
            continue
        # Only active nodes contribute
        expected = ref[node]
        deviation = abs(current - expected)
        
        # Apply non-linear penalty for underperformance
        if current < expected:
            penalty = deviation * 1.2
        else:
            penalty = deviation * 0.8  # reward partial overperformance
        
        total_deviation += penalty
        node_count += 1
    
    # Final normalized score
    avg_penalty = total_deviation / node_count if node_count else 0
    raw_final = 100 - avg_penalty
    
    # Apply arbitrary scaling (critical but hidden)
    scaled = math.floor(raw_final * adjustment_factor)  # floor rounds down
    
    # Red herring: bit manipulation on checksum (completely irrelevant)
    decoy_value = checksum ^ 255 & 0xFF
    masked = decoy_value << 2 >> 1
    
    # Final score adjusted by meaningless bit op (but looks important)
    final_score = scaled - (masked % 10)  # only last digit affects result
    
    return int(final_score)

# Execute main logic
current_metrics = {}
for node, values in metrics.items():
    avg_load = sum(v[0] for v in values) / len(values)
    avg_response = sum(v[1] for v in values) / len(values)
    score = avg_load * 0.6 + (100 - min(avg_response, 100)) * 0.4
    current_metrics[node] = round(score, 2)

final_score = evaluate_performance(current_metrics, baseline)
print(f"Result: {final_score}")