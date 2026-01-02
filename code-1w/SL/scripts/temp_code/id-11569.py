from itertools import combinations

def analyze_traffic(patterns):
    total_load = 0
    peak_moments = []
    for i, p in enumerate(patterns):
        load = sum(p) * (i + 1)
        total_load += load
        if load > 50:
            peak_moments.append(i)
    
    # Distractor: irrelevant analysis
    avg_load = total_load / len(patterns) if patterns else 0
    fluctuation = max([sum(p) for p in patterns]) - min([sum(p) for p in patterns]) if patterns else 0

    return total_load, peak_moments

def simulate_latency(nodes):
    latency_map = {}
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            distance = abs(nodes[i] - nodes[j])
            latency_map[(i,j)] = distance * 0.25
    
    # Dead computation: not used later
    total_latency = sum(latency_map.values())
    high_latency_pairs = [pair for pair, lat in latency_map.items() if lat > 1.0]
    
    return latency_map

def optimize_bandwidth(configurations, traffic_patterns, node_positions):
    base_score = 0
    temp_result = []
    
    for config in configurations:
        multiplier = config['speed'] / config['cost'] if config['cost'] != 0 else 0
        base_score += multiplier * len(config['ports'])
    
    # Use of slicing and combinations - relevant to final result
    valid_slices = [config['ports'][1:-1] for config in configurations if len(config['ports']) > 2]
    all_subgroups = []
    for s in valid_slices:
        all_subgroups.extend(list(combinations(s, 2)))
    
    connection_score = len(all_subgroups) * 1.5
    
    # Traffic analysis - actually contributes
    traffic_load, peaks = analyze_traffic(traffic_patterns)
    
    # Simulate but only use part of info - distractor in full map
    _ = simulate_latency(node_positions)
    
    # Core calculation path
    position_factor = sum([pos ** 2 for pos in node_positions if pos % 2 == 0])
    efficiency = base_score * 0.8 + connection_score
    
    # Final bandwidth depends on traffic, position factor, and efficiency
    final_bandwidth = int((efficiency * 100 + traffic_load) // (position_factor + 1))
    
    # Red herring variables
    theoretical_max = efficiency * 150
    degraded_ratio = theoretical_max / (final_bandwidth + 1) if final_bandwidth != -1 else 0
    
    return final_bandwidth

# Input data
configs = [
    {'speed': 100, 'cost': 10, 'ports': [1, 2, 3, 4]},
    {'speed': 200, 'cost': 25, 'ports': [5, 6, 7, 8, 9]},
    {'speed': 150, 'cost': 15, 'ports': [10]}
]

traffic = [
    [10, 20, 15],
    [5, 80, 12],
    [30, 10, 5],
    [5, 5, 85]
]

positions = [0, 3, 4, 6, 8]

# Execution
final_bandwidth = optimize_bandwidth(configs, traffic, positions)
print(f"Result: {final_bandwidth}")