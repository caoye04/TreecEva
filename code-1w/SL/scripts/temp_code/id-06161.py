from collections import defaultdict

# Simulate system health monitoring with performance metrics
raw_data = [
    {'cpu': 75, 'mem': 80, 'disk': 40, 'net_in': 30, 'net_out': 25},
    {'cpu': 85, 'mem': 60, 'disk': 55, 'net_in': 45, 'net_out': 40},
    {'cpu': 90, 'mem': 95, 'disk': 30, 'net_in': 60, 'net_out': 55},
    {'cpu': 65, 'mem': 70, 'disk': 50, 'net_in': 35, 'net_out': 30}
]

# Weight configuration for different subsystems
weights = defaultdict(float)
weights['cpu'] = 0.30
weights['mem'] = 0.25
weights['disk'] = 0.20
weights['network'] = 0.25  # Combined network weight

# Derived transformation: split network into two but keep combined weight
network_split_ratio = 0.6  # Arbitrary ratio for internal use only
net_in_weight = weights['network'] * network_split_ratio
net_out_weight = weights['network'] * (1 - network_split_ratio)

# Historical baselines (distractor - not used in final calculation)
historical_avg = {
    'cpu': 70, 'mem': 65, 'disk': 45, 'net_in': 40, 'net_out': 38
}

drift_analysis = {}
for key in historical_avg:
    drift_analysis[key] = raw_data[-1][key] - historical_avg[key] if key in raw_data[-1] else 0

# Aggregate metrics across time (only some components are actually used later)
aggregated = defaultdict(float)
for entry in raw_data:
    for k, v in entry.items():
        aggregated[k] += v

# Normalize aggregated values to average per observation
for k in aggregated:
    aggregated[k] /= len(raw_data)

# Secondary derived variables - mostly distractions
peak_load = max(sum(entry.values()) for entry in raw_data)
system_balance = (aggregated['cpu'] + aggregated['mem']) / 2  # unused metric
utilization_gap = abs(aggregated['disk'] - historical_avg['disk'])  # red herring

# Focus on current state for evaluation
current_state = raw_data[-1]

# Prepare normalized metric inputs for scoring
metrics = {}
metrics['cpu'] = current_state['cpu'] / 100.0
metrics['mem'] = current_state['mem'] / 100.0
metrics['disk'] = current_state['disk'] / 100.0
metrics['network'] = (current_state['net_in'] + current_state['net_out']) / 200.0

# Additional irrelevant normalization
baseline_normalized = {}
for k in historical_avg:
    baseline_normalized[k] = aggregated[k] / (historical_avg[k] or 1) if k in historical_avg else 0

# Core evaluation logic
weighted_sum = 0.0
total_weight = 0.0

# Only cpu, mem, disk, and network contribute
for component in ['cpu', 'mem', 'disk', 'network']:
    if component in metrics and component in weights:
        weighted_sum += metrics[component] * weights[component]
        total_weight += weights[component]

# Final adjustment based on consistency check (extra logic that doesn't alter core)
consistency_factor = 1.0
if abs(aggregated['cpu'] - aggregated['mem']) < 20:
    consistency_factor = 1.05

# Compute final score
final_score = int(weighted_sum * 100 * consistency_factor)

# Irrelevant post-processing
projected_load = final_score * 1.15  # unused forecast
trend_index = (final_score - 70) * 2  # distraction metric

Result: {final_score}