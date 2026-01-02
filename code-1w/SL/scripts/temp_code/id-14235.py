from collections import defaultdict, Counter
import itertools

# Simulate system telemetry data
telemetry_logs = [
    {'node': 'A', 'status': 'active', 'load': 0.65, 'errors': 2},
    {'node': 'B', 'status': 'idle',   'load': 0.20, 'errors': 0},
    {'node': 'C', 'status': 'active', 'load': 0.88, 'errors': 5},
    {'node': 'A', 'status': 'active', 'load': 0.70, 'errors': 1},
    {'node': 'D', 'status': 'active', 'load': 0.92, 'errors': 8},
    {'node': 'B', 'status': 'active', 'load': 0.30, 'errors': 0},
    {'node': 'C', 'status': 'failed', 'load': 0.00, 'errors': 12},
    {'node': 'E', 'status': 'active', 'load': 0.76, 'errors': 3}
]

# Irrelevant helper (decoy)
def analyze_throughput(logs):
    total = 0
    for entry in logs:
        if entry['status'] == 'active':
            total += entry['load'] * 100
    return total // len(logs)

# Unused aggregation (red herring)
node_summary = defaultdict(lambda: {'count': 0, 'total_load': 0.0})
for log in telemetry_logs:
    node = log['node']
    node_summary[node]['count'] += 1
    node_summary[node]['total_load'] += log['load']

# Misleading transformation (distractor)
expanded_logs = []
for log in telemetry_logs:
    expanded_logs.append({
        'id': f"{log['node']}-{len(expanded_logs)}",
        'health': 'good' if log['errors'] < 5 else 'critical',
        'priority': 1 if log['load'] > 0.8 else (2 if log['load'] > 0.5 else 3)
    })

# Real processing begins here
def collect_active_metrics(logs):
    active_metrics = []
    for entry in logs:
        if entry['status'] == 'active' and entry['load'] > 0:
            normalized_error = min(entry['errors'] / 10.0, 1.0)
            score = (entry['load'] * 0.7) - (normalized_error * 0.3)
            active_metrics.append(max(score, 0))
    return active_metrics

# Weighted evaluation with irrelevant parameters
def apply_weighting(scores, strategy='balanced'):
    if strategy == 'aggressive':
        return [s ** 1.1 for s in scores]
    elif strategy == 'conservative':
        return [s ** 0.9 for s in scores]
    else:
        return [s ** 1.0 for s in scores]  # balanced

# Fake recursive function (dead path)
def calculate_depth(data, depth=0):
    if not data or depth > 3:
        return depth
    return calculate_depth(data[1:], depth + 1)

# Real evaluation logic
def evaluate_performance(raw_logs, weight_config):
    base_scores = collect_active_metrics(raw_logs)
    
    # Apply weighting (actually does nothing since exponent is 1.0)
    adjusted_scores = apply_weighting(base_scores, weight_config['strategy'])
    
    # Secondary filter: only top 75% of scores contribute
    threshold = sorted(adjusted_scores)[int(len(adjusted_scores) * 0.25)]
    filtered_scores = [s for s in adjusted_scores if s >= threshold]
    
    # Compute final metric using combined formula
    avg_score = sum(filtered_scores) / len(filtered_scores) if filtered_scores else 0
    peak_utilization = max(entry['load'] for entry in raw_logs if entry['status'] == 'active')
    stability_penalty = sum(1 for entry in raw_logs if entry['errors'] > 5 and entry['status'] == 'active') * 0.05
    
    # Final weighted combination
    result = (avg_score * weight_config['weights'][0] + 
              peak_utilization * weight_config['weights'][1] - 
              stability_penalty * weight_config['weights'][2])
    
    # Normalize to 0-100 scale
    return max(result * 100, 0)

# Decoy data structure (unused)
critical_nodes = set()
for log in telemetry_logs:
    if log['errors'] > 6:
        critical_nodes.add(log['node'])

# Another red herring: pairwise combinations (irrelevant)
pairwise_status = list(itertools.combinations([log['status'] for log in telemetry_logs], 2))
valid_pairs = [p for p in pairwise_status if p[0] != p[1]]

# Configuration with misleading fields
config = {
    'strategy': 'balanced',
    'debug_mode': True,
    'version': '2.1a',
    'weights': [0.4, 0.5, 0.1],  # Contribution: average, peak, penalty
    'timeout': 3000,
    'retries': 3
}

# Extract metrics (this is where real computation starts)
metrics = telemetry_logs

# Dead code: unused transformation chain
intermediate_flow = [m['load'] for m in metrics if m['node'] in ['A','C','E']]
smoothed = list(itertools.accumulate(intermediate_flow))
if smoothed:
    smoothed = [x / len(smoothed) for x in smoothed]

# Trigger final evaluation
final_score = evaluate_performance(metrics, config)

# Output result as required
print(f"Target result: {final_score}")