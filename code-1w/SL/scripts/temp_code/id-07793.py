from itertools import combinations

# System calibration constants (some are red herrings)
default_offset = 0.87
scaling_factor = 2.3
baseline_correction = -0.05
irrelevant_threshold = 42.0

# Input data for thermal simulation
temperature_zones = [23.5, 25.1, 26.3, 24.9, 27.8]
pressure_levels = [101.3, 102.1, 99.7, 103.4]
efficiency_factor = 0.91

# Simulated energy distribution across grid nodes
energy_map = {
    'node_A': 1850,
    'node_B': 1930,
    'node_C': 1780,
    'node_D': 1880,
    'node_E': 1950
}

# Misleading precomputation (distractor)
aggregate_score = sum([v ** 0.5 for v in energy_map.values()]) / len(energy_map)
score_adjusted = aggregate_score * scaling_factor

# Helper function to compute auxiliary metric (not directly used but looks important)
def compute_variance(data):
    mean_val = sum(data) / len(data)
    return sum((x - mean_val) ** 2 for x in data) / len(data)

# Real computational core
def calculate_thermal_output(energy_dict, efficiency):
    # Step 1: Extract base energy levels
    base_energy = sum(energy_dict.values())
    
    # Step 2: Apply efficiency correction
    adjusted_energy = base_energy * efficiency
    
    # Step 3: Use itertools to explore interaction pairs (simulated load balancing)
    keys = list(energy_dict.keys())
    pair_interactions = list(combinations(keys, 2))
    interaction_bonus = 0
    
    # This loop computes a fake bonus based on node pairings (only some affect result)
    for pair in pair_interactions:
        node1, node2 = pair
        diff = abs(energy_dict[node1] - energy_dict[node2])
        if diff < 100:
            interaction_bonus += diff * 0.05  # Small contribution
    
    # Step 4: Add baseline correction (real use of previously defined constant)
    final_output = adjusted_energy + interaction_bonus + baseline_correction
    
    # Irrelevant transformations (dead computations - distraction)
    normalized_pairs = [p for p in pair_interactions if 'A' in p]
    dummy_metric = len(normalized_pairs) * default_offset
    _ = dummy_metric ** 2  # Unused computation
    
    return final_output

# Additional distracting state tracking
status_flags = {zone: temp > 25 for zone, temp in zip(['Z1','Z2','Z3','Z4','Z5'], temperature_zones)}
active_zones = sum(status_flags.values())

# Key execution point
thermal_capacity = calculate_thermal_output(energy_map, efficiency_factor)

# Print result as required
print(f"Target result: {thermal_capacity}")