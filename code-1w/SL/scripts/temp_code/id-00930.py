from itertools import combinations, cycle

def analyze_cluster_density(nodes):
    density_map = {}
    for i, node in enumerate(nodes):
        density_map[f'node_{i}'] = (node ** 2 + len(nodes)) / (i + 1)
    return density_map

def filter_active_segments(raw_data, threshold=0.5):
    # Irrelevant filtering - distractor
    return [x for x in raw_data if abs(x) > threshold]

def compute_momentum(base_sequence, cycles):
    momentum = 1.0
    temp_buffer = []
    for cycle in range(cycles):
        for val in base_sequence:
            if cycle % 2 == 0:
                momentum *= (val + 0.1) / (cycle + 1)
            else:
                temp_buffer.append(val - 0.1)
    return momentum  # Used only indirectly

def calculate_optimal_yield(scores, iterations):
    adjusted_scores = [s * 1.1 for s in scores]
    
    # Generate all 2-element combinations as part of analysis
    combo_risks = list(combinations(adjusted_scores, 2))
    risk_penalty = 0
    for a, b in combo_risks:
        if a > b:
            risk_penalty += (a - b) * 0.05
    
    # Simulate cyclic growth phases
    growth_pattern = cycle([1, -1, 0])
    fluctuation = 0
    for _ in range(iterations * 2):
        fluctuation += next(growth_pattern)

    # Core yield logic
    base_yield = sum(adjusted_scores)
    stability_factor = len(combo_risks) / (len(scores) + 1)
    final_yield = int(base_yield - risk_penalty + fluctuation * stability_factor)
    
    # Dead code path - red herring
    if False:
        backup_system = [x for x in adjusted_scores if x < 0]
        final_yield = max(final_yield, sum(backup_system))
        
    return final_yield

# Main execution block
sensor_nodes = [3, 7, 2, 8, 5]
density_profile = analyze_cluster_density(sensor_nodes)
raw_fluctuations = [-0.6, 0.2, 1.1, -0.3, 0.9]
filtered_data = filter_active_segments(raw_fluctuations)

momentum_factor = compute_momentum([2, 4, 6], 3)
cluster_scores = [v for k, v in density_profile.items() if 'node_' in k]
growth_cycles = len(sensor_nodes) + 2

intermediate_stat = sum(filter(lambda x: x > 5, cluster_scores))  # Distractor stat

final_yield = calculate_optimal_yield(cluster_scores, growth_cycles)
print(f"Target result: {final_yield}")