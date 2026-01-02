from collections import defaultdict, Counter

# Simulated system telemetry data
telemetry_logs = [
    {'node': 'A', 'status': 'active', 'load': 0.65, 'errors': 2},
    {'node': 'B', 'status': 'idle',   'load': 0.20, 'errors': 0},
    {'node': 'C', 'status': 'active', 'load': 0.80, 'errors': 1},
    {'node': 'A', 'status': 'active', 'load': 0.70, 'errors': 1},
    {'node': 'D', 'status': 'active', 'load': 0.90, 'errors': 3},
    {'node': 'B', 'status': 'active', 'load': 0.45, 'errors': 0},
]

# Irrelevant utility function (dead code path)
def analyze_throughput(logs):
    total = 0
    for log in logs:
        if log['status'] == 'active':
            total += log['load'] * 100
    return int(total)

# Unused aggregation map
telemetry_map = defaultdict(list)
for entry in telemetry_logs:
    telemetry_map[entry['node']].append(entry['load'])

# Historical error trends (distractor data)
historical_errors = Counter([log['errors'] for log in telemetry_logs])

# System health thresholds (red herring constants)
THRESHOLDS = {
    'critical_load': 0.85,
    'high_error_rate': 2,
    'optimal_range': (0.4, 0.7)
}

# Faux normalization function (misleading intermediate)
def normalize_value(x, min_val=0, max_val=1):
    return (x - min_val) / (max_val - min_val) if max_val > min_val else 0

# Simulate lagging indicators (irrelevant computation)
lagging_indicators = []
for i in range(len(telemetry_logs)):
    if i > 0 and telemetry_logs[i]['load'] > telemetry_logs[i-1]['load']:
        lagging_indicators.append(1)
    else:
        lagging_indicators.append(0)

# Core evaluation logic begins here
def calculate_stability_factor(node_data):
    loads = [entry['load'] for entry in node_data]
    avg_load = sum(loads) / len(loads)
    variance = sum((x - avg_load) ** 2 for x in loads) / len(loads)
    return 1 / (1 + variance)  # Higher stability = lower variance

# Weighted scoring model
weights = {
    'stability': 0.4,
    'avg_load': 0.3,
    'error_penalty': 0.3
}

# Node performance cache (cross-reference structure)
node_performance = {}
for node_id in set(log['node'] for log in telemetry_logs):
    node_logs = [log for log in telemetry_logs if log['node'] == node_id]
    avg = sum(log['load'] for log in node_logs) / len(node_logs)
    err = sum(log['errors'] for log in node_logs)
    stab = calculate_stability_factor(node_logs)
    node_performance[node_id] = {
        'avg': avg,
        'err': err,
        'stab': stab,
        'count': len(node_logs)
    }

# Secondary sorting for tie-breaking (distractor logic)
sorted_nodes = sorted(node_performance.keys(), key=lambda x: (node_performance[x]['avg'], x))

# Auxiliary transformation (unused outcome)
transformed_scores = {}
for k, v in node_performance.items():
    raw = v['avg'] * v['stab']
    transformed_scores[k] = round(raw, 4)

# Actual metric extraction for final evaluation
metrics = {}
overall_avg_load = sum(m['avg'] for m in node_performance.values()) / len(node_performance)
composite_stability = sum(m['stab'] for m in node_performance.values()) / len(node_performance)
error_sum = sum(m['err'] for m in node_performance.values())

metrics['stability'] = composite_stability
metrics['avg_load'] = max(min(overall_avg_load, 1.0), 0.0)  # Clamp to [0,1]
metrics['error_penalty'] = -min(error_sum * 0.05, 0.5)  # Cap penalty

# Decoy calculation with similar naming (deliberate confusion)
temp_score = 0
for val in metrics.values():
    temp_score += val * 0.8  # Not used

# Final evaluation using correct weights
final_score = 0
for key in metrics:
    final_score += metrics[key] * weights[key]

# Normalize final score into bounded performance index
final_score = max(0, min(final_score * 100, 100))  # Scale to 0-100 range

# Redundant consistency check (no effect)
if abs(final_score) < 1e-5:
    final_score = 0.0

# Output result as required
print(f"Result: {final_score}")