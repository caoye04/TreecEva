def analyze_traffic(hubs):
    traffic_scores = []
    for hub in hubs:
        base_score = hub['incoming'] + hub['outgoing']
        adjusted_score = base_score * (1 + hub.get('priority', 0.1))
        normalized = adjusted_score / (hub['latency'] + 1)
        traffic_scores.append(normalized)
    return traffic_scores

hubs_data = [
    {'incoming': 85, 'outgoing': 92, 'latency': 4, 'priority': 0.2},
    {'incoming': 77, 'outgoing': 81, 'latency': 3, 'priority': 0.15},
    {'incoming': 93, 'outgoing': 68, 'latency': 5, 'priority': 0.1},
    {'incoming': 64, 'outgoing': 90, 'latency': 2, 'priority': 0.25}
]

traffic_analysis = analyze_traffic(hubs_data)

# Irrelevant computation: simulate signal degradation (not used later)
signal_levels = [round(100 / (lat + 1), 2) for lat in [hub['latency'] for hub in hubs_data]]
degradation_penalty = sum([abs(signal_levels[i] - signal_levels[i-1]) for i in range(1, len(signal_levels))])

# Preprocessing step with slicing and filtering
raw_utilization = [hub['incoming'] * 1.1 + hub['outgoing'] * 0.9 for hub in hubs_data]
peak_utilization = raw_utilization[1:3]
avg_peak = sum(peak_utilization) / len(peak_utilization)

# Simulate redundant health check (dead code path)
def check_health(hub_list):
    total_nodes = len(hub_list)
    if total_nodes > 10:
        return 'OVERLOADED'
    elif total_nodes > 5:
        return 'STRESSED'
    else:
        return 'HEALTHY'

status = check_health(hubs_data)  # Not used beyond this point

# Set operations to identify high-throughput hubs
high_incoming = {i for i, hub in enumerate(hubs_data) if hub['incoming'] > 80}
high_outgoing = {i for i, hub in enumerate(hubs_data) if hub['outgoing'] > 85}
balanced_hubs = high_incoming & high_outgoing  # intersection: indices 0 and 3

# Process only balanced hubs using list comprehension and slicing
efficiency_map = {idx: hubs_data[idx]['incoming'] / (hubs_data[idx]['outgoing'] + 1) for idx in balanced_hubs}
processed_hubs = [efficiency_map[idx] for idx in sorted(balanced_hubs)]

# Introduce misleading normalization factor (semi-relevant)
normalizer = max(efficiency_map.values()) if efficiency_map else 1
scaled_factors = [val / normalizer for val in efficiency_map.values()]

# Dummy transformation chain
transformed = [f * f * 1.5 for f in scaled_factors]
aggregate_metric = sum(transformed) * 0.8  # distraction

# Key logic: efficiency factor derived from average traffic score
mean_traffic = sum(traffic_analysis) / len(traffic_analysis)
efficiency_factor = round(mean_traffic / 50, 3)

# Core algorithm: optimize distribution based on processed hubs and factor
def optimize_distribution(hub_ratios, factor):
    adjusted = [r * factor for r in hub_ratios]
    capacity_base = sum(adjusted)
    penalty = len(hub_ratios) * 0.1
    final = int(capacity_base * (1 - penalty / 10))
    return final

final_capacity = optimize_distribution(processed_hubs, efficiency_factor)
print(f"Target result: {final_capacity}")