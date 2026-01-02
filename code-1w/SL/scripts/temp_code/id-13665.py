from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_logs = [
    {'node': 'A', 'load': 0.85, 'errors': 2, 'timestamp': 100},
    {'node': 'B', 'load': 0.72, 'errors': 0, 'timestamp': 101},
    {'node': 'A', 'load': 0.91, 'errors': 5, 'timestamp': 102},
    {'node': 'C', 'load': 0.65, 'errors': 1, 'timestamp': 103},
    {'node': 'B', 'load': 0.74, 'errors': 0, 'timestamp': 104},
    {'node': 'C', 'load': 0.69, 'errors': 3, 'timestamp': 105},
]

# Irrelevant utility function (decoy)
def calculate_entropy(data):
    total = sum(data)
    entropy = 0
    for x in data:
        if x > 0:
            p = x / total
            entropy -= p * math.log(p)
    return round(entropy, 4)

# Misleading data aggregation (unused)
node_requests = defaultdict(int)
for log in telemetry_logs:
    node_requests[log['node']] += 1

# Core metric computation
error_count_per_node = defaultdict(list)
for log in telemetry_logs:
    error_count_per_node[log['node']].append(log['errors'])

avg_errors = {}
for node, errors in error_count_per_node.items():
    avg_errors[node] = sum(errors) / len(errors)

# Dummy transformation chain
transformed_metrics = []
for entry in telemetry_logs:
    transformed = {
        'id': hash(entry['node'] + str(entry['timestamp'])) % 1000,
        'val': entry['load'] * (entry['errors'] + 1)
    }
    transformed_metrics.append(transformed)

# Red herring: unused complex structure
aggregated = defaultdict(lambda: defaultdict(list))
for t in transformed_metrics:
    bucket = 'high' if t['val'] > 0.8 else 'low'
    aggregated[t['id'] % 5][bucket].append(t['val'])

# Real processing begins here
raw_scores = []
for log in telemetry_logs:
    score = (1 - log['load']) * 100
    penalty = log['errors'] * 5
    raw_scores.append(max(score - penalty, 0))

# Intermediate decoy statistic
median_raw = sorted(raw_scores)[len(raw_scores)//2]

# Threshold-based normalization
thresholds = {
    'performance_floor': 40,
    'stability_bonus': 10,
    'consistency_window': 3
}

# Actual evaluation logic (obscured by noise)
def evaluate_performance(metrics, config):
    base = sum(metrics) / len(metrics)
    
    # Conditional bonus path (misleading - not triggered)
    if base > 60:
        bonus = config['stability_bonus']
    else:
        bonus = 0  # Not taken
    
    # Consistency check across nodes
    node_contributions = defaultdict(list)
    for i, log in enumerate(telemetry_logs):
        node_contributions[log['node']].append(raw_scores[i])
    
    consistency_factors = []
    for node, scores in node_contributions.items():
        variation = max(scores) - min(scores)
        consistency_factors.append(10 - min(variation, 10))
    
    consistency_score = sum(consistency_factors) / len(consistency_factors)
    
    # Final composition
    adjusted = base + (consistency_score * 0.8)
    
    # Apply floor
    if adjusted < config['performance_floor']:
        adjusted = config['performance_floor']
    
    return int(round(adjusted))

# Unused alternative algorithm (dead code path)
def legacy_evaluation(logs):
    weights = {'load': -1.2, 'errors': -2.0}
    total = 0
    for log in logs:
        total += weights['load'] * log['load'] + weights['errors'] * log['errors']
    return abs(total)

# Critical execution point
final_score = evaluate_performance(raw_scores, thresholds)

# Output result
print(f"Result: {final_score}")