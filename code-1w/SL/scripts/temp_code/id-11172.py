def analyze_traffic(hubs):
    traffic_scores = []
    for hub in hubs:
        score = 0
        if hub['load'] > 80:
            score += 20
        elif hub['load'] > 50:
            score += 10
        if hub['uptime'] < 90:
            score -= 5
        traffic_scores.append(score)
    return traffic_scores

hubs = [
    {'name': 'hub_alpha', 'load': 85, 'uptime': 95, 'region': 'north'},
    {'name': 'hub_beta', 'load': 45, 'uptime': 88, 'region': 'south'},
    {'name': 'hub_gamma', 'load': 75, 'uptime': 92, 'region': 'east'},
    {'name': 'hub_delta', 'load': 92, 'uptime': 85, 'region': 'west'}
]

# Irrelevant helper: computes unused latency metric
def compute_latency_penalty(hub_list):
    total_penalty = 0
    for h in hub_list:
        if h['uptime'] < 90 and h['load'] > 70:
            total_penalty += 3
    return total_penalty

latency_warning = compute_latency_penalty(hubs)  # Dead-end computation

# Preprocessing with list comprehension (relevant)
filtered_hubs = [h for h in hubs if h['load'] > 50]
processed_hubs = []
for h in filtered_hubs:
    h['adjusted_load'] = h['load'] * 0.9
    processed_hubs.append(h)

# Dummy set operation (semi-relevant distraction)
available_regions = {h['region'] for h in hubs}
active_regions = {h['region'] for h in processed_hubs}
coverage_gap = available_regions - active_regions

# Core logic: capacity optimization based on adjusted metrics
def optimize_distribution(hub_list):
    base_capacity = 100
    adjustment_factor = 0.0
    for h in hub_list:
        if h['adjusted_load'] > 70:
            adjustment_factor += 0.25
        else:
            adjustment_factor += 0.1
    final_adj = base_capacity * (1 + adjustment_factor)
    return int(final_adj)

# Secondary irrelevant calculation
total_load_sum = sum(h['load'] for h in hubs)
normalized_score = total_load_sum / len(hubs)  # Not used later

final_capacity = optimize_distribution(processed_hubs)
print(f"Result: {final_capacity}")