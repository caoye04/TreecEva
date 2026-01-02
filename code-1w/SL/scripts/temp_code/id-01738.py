from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.6, 'errors': 2, 'priority': 'high'},
    {'node': 'B', 'load': 0.3, 'errors': 0, 'priority': 'medium'},
    {'node': 'C', 'load': 0.8, 'errors': 5, 'priority': 'high'},
    {'node': 'A', 'load': 0.7, 'errors': 1, 'priority': 'high'},
    {'node': 'B', 'load': 0.9, 'errors': 8, 'priority': 'medium'},
    {'node': 'D', 'load': 0.4, 'errors': 0, 'priority': 'low'},
    {'node': 'C', 'load': 0.6, 'errors': 3, 'priority': 'high'}
]

# Irrelevant utility function (dead code path)
def normalize_vector(v):
    mag = sum(x**2 for x in v) ** 0.5
    return [x/mag for x in v] if mag else v

# Decoy transformation (never used)
decoy_map = {i: (i * i) % 17 for i in range(100)}

# Aggregation placeholder
aggregated = defaultdict(lambda: {'total_load': 0.0, 'error_count': 0, 'entries': 0})

for entry in telemetry_stream:
    key = entry['node']
    aggregated[key]['total_load'] += entry['load']
    aggregated[key]['error_count'] += entry['errors']
    aggregated[key]['entries'] += 1

# Compute averages
node_stats = {}
for node, data in aggregated.items():
    avg_load = data['total_load'] / data['entries']
    error_rate = data['error_count'] / data['entries']
    node_stats[node] = {
        'avg_load': avg_load,
        'error_rate': error_rate,
        'health': 'stable' if avg_load < 0.75 and error_rate < 3 else 'unstable'
    }

# Red herring: unused health summary
temp_summary = Counter([s['health'] for s in node_stats.values()])

# Spurious sorting operation with no impact
sorted_nodes = sorted(node_stats.keys(), key=lambda x: (-node_stats[x]['avg_load'], x))

# Another decoy structure
shadow_copy = {k: {**v} for k, v in node_stats.items()}
for node in shadow_copy:
    shadow_copy[node]['diagnostic_flag'] = False
    if shadow_copy[node]['avg_load'] > 0.8:
        shadow_copy[node]['diagnostic_flag'] = True  # never accessed

# Critical recursive transformation function
def calculate_decay_factor(n, base=0.95):
    if n <= 1:
        return base
    return base * calculate_decay_factor(n - 1, base)

# Misleading intermediate calculation (appears important)
baseline_penalty = sum(math.log(1 + s['error_rate']) for s in node_stats.values())

# Core metric processor
def extract_metrics(stats):
    metrics = []
    for node, data in stats.items():
        raw_score = 100 * (1 - data['avg_load'])
        penalty = 10 * data['error_rate']
        adjusted = raw_score - penalty
        # Apply decay based on node name length (subtle but valid)
        decay = calculate_decay_factor(len(node), 0.9)
        final_node_score = adjusted * decay
        metrics.append(final_node_score)
    return metrics

# Secondary filter that looks important but only removes outliers
metric_data = [m for m in extract_metrics(node_stats) if m > -20]

# Dummy normalization (distraction)
if len(metric_data) > 0:
    max_val = max(metric_data)
    min_val = min(metric_data)
    range_val = max_val - min_val or 1
    normalized = [(m - min_val) / range_val for m in metric_data]

# Unused clustering attempt
cluster_centers = []
for i in range(1, 3):
    center = sum(normalized[j] for j in range(0, len(normalized), i)) / len(normalized)
    cluster_centers.append(center)

# The actual evaluation logic buried in distractions
def evaluate_performance(data):
    if not data:
        return 0
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    # Final adjustment using standard deviation as dampener
    result = mean_val * (1 - std_dev / (std_dev + 10))
    return round(result, 6)

# Execution point of interest
final_score = evaluate_performance(metric_data)

# Print required output
print(f"Target result: {final_score}")