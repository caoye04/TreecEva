from collections import defaultdict
from itertools import combinations

# Simulate a network packet routing scenario with performance metrics
def analyze_routing_efficiency(raw_routes, bandwidth_limits):
    route_stats = defaultdict(lambda: {'hops': 0, 'latency': 0.0})
    temp_analysis = {}
    total_transmissions = 0
    debug_flag = False

    # Process each route and compute basic stats
    for i, route in enumerate(raw_routes):
        if len(route) == 0:
            continue
        hops = len(route) - 1
        base_latency = 0.5 * hops
        transmission_weight = bandwidth_limits[i % len(bandwidth_limits)]

        # Irrelevant intermediate calculation (distractor)
        theoretical_max = (transmission_weight ** 2) / (1 + hops) if hops > 0 else 0
        temp_analysis[f'test_{i}'] = theoretical_max

        route_stats[f'route_{i}']['hops'] = hops
        route_stats[f'route_{i}']['latency'] = round(base_latency + 0.1 * transmission_weight, 4)
        total_transmissions += transmission_weight * (hops + 1)

    # Generate synthetic failure scenarios (mostly unused)
    failure_modes = []
    for r1, r2 in combinations(route_stats.keys(), 2):
        if route_stats[r1]['hops'] > 2 and route_stats[r2]['latency'] > 1.0:
            failure_modes.append((r1, r2, 'CONGESTION'))
        elif route_stats[r1]['latency'] < 0.8:
            failure_modes.append((r1, r2, 'UNDERUTILIZED'))

    # Core metric computation
    valid_hops = [v['hops'] for v in route_stats.values() if v['hops'] > 0]
    avg_hops = sum(valid_hops) / len(valid_hops) if valid_hops else 0
    latency_values = [v['latency'] for v in route_stats.values()]
    avg_latency = sum(latency_values) / len(latency_values) if latency_values else 0

    # Secondary distractor: unused optimization path
    optimization_candidates = []
    for key, stats in route_stats.items():
        if stats['latency'] > avg_latency and stats['hops'] < avg_hops:
            optimization_candidates.append(key)

    # Normalize transmission count
    normalized_tx = max(1, total_transmissions // len(raw_routes))

    # Final efficiency model (key logic)
    raw_efficiency = (avg_hops + 1) * (avg_latency + 0.1) / (normalized_tx ** 0.5)
    efficiency_score = int(100 / (raw_efficiency + 0.01)) if raw_efficiency > 0 else 0

    return efficiency_score, route_stats, temp_analysis


def calculate_efficiency(data_packet):
    processed_records = data_packet.get('records', [])
    limits = data_packet.get('bandwidth', [10, 20, 30])
    score, _, _ = analyze_routing_efficiency(processed_records, limits)
    return score

# Input data setup
network_data = {
    'records': [
        ['A', 'B', 'C'],
        ['A', 'D'],
        ['A', 'B', 'D', 'E'],
        ['A', 'C', 'E'],
        ['A', 'B', 'E']
    ],
    'bandwidth': [5, 15, 25, 10]
}

# Execute main analysis
processed_data = network_data
final_output = calculate_efficiency(processed_data)

# Extract target variable
efficiency_score = final_output
print(f"Result: {efficiency_score}")