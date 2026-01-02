def analyze_traffic(hubs):
    traffic_scores = {}
    for hub in hubs:
        base_score = len(hub['nodes']) * hub['load_factor']
        adjustment = 1 + (hub['uptime'] // 100) * 0.05
        traffic_scores[hub['id']] = base_score * adjustment
    return traffic_scores

hubs_data = [
    {'id': 'A', 'nodes': [1, 2, 3, 4], 'load_factor': 2.1, 'uptime': 987},
    {'id': 'B', 'nodes': [5, 6], 'load_factor': 3.5, 'uptime': 1003},
    {'id': 'C', 'nodes': [7, 8, 9], 'load_factor': 1.8, 'uptime': 750},
    {'id': 'D', 'nodes': [10], 'load_factor': 4.0, 'uptime': 1200}
]

# Irrelevant preprocessing step (distractor)
temp_summary = []
for h in hubs_data:
    temp_summary.append(f"Hub {h['id']}: {len(h['nodes'])} nodes")

traffic_analysis = analyze_traffic(hubs_data)

# Simulate filtering active hubs
active_hub_ids = set()
for h in hubs_data:
    if h['uptime'] > 900:
        active_hub_ids.add(h['id'])

processed_hubs = []
for h in hubs_data:
    normalized_load = h['load_factor'] / (h['uptime'] / 100)
    processed_hubs.append({
        'id': h['id'],
        'efficiency': len(h['nodes']) / normalized_load if normalized_load != 0 else 0,
        'critical': h['id'] in active_hub_ids
    })

# Secondary analysis with red herring computations
redundant_metrics = []
for p in processed_hubs:
    dummy_val = p['efficiency'] ** 0.5 * 100
    redundant_metrics.append(dummy_val)  # unused later

# Real logic begins: count critical hubs
critical_count = sum(1 for p in processed_hubs if p['critical'])
total_bandwidth = 1500.0
bandwidth_per_critical = total_bandwidth / critical_count if critical_count > 0 else 0

# Optimization function with conditional logic and distractors
def optimize_distribution(hubs, bandwidth):
    total_efficiency = sum(h['efficiency'] for h in hubs)
    avg_efficiency = total_efficiency / len(hubs) if hubs else 0

    # Distractor: complex but unused calculation
    hypothetical_gains = []
    for h in hubs:
        projected = h['efficiency'] * 1.2 if h['critical'] else h['efficiency'] * 0.8
n        hypothetical_gains.append(projected * 10)

    # Actual capacity logic
    scaling_factor = 0.8 if avg_efficiency > 2.0 else 0.6
    base_capacity = bandwidth * scaling_factor

    # Bonus only if exactly 2 or 3 critical hubs
    if critical_count == 2:
        bonus = 120
    elif critical_count == 3:
        bonus = 80
    else:
        bonus = 0

    final = base_capacity + bonus

    # More distraction: unused set operations
    hub_names = {h['id'] for h in hubs}
    extra_set = {'A', 'B', 'E'}
    intersection = hub_names & extra_set  # not used

    return int(final)

# Execute key computation
final_capacity = optimize_distribution(processed_hubs, total_bandwidth)
print(f"Result: {final_capacity}")