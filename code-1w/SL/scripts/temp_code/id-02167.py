from itertools import combinations

def calculate_system_efficiency(configurations, base_load):
    efficiencies = []
    temp_storage = []
    total_configs = 0

    for r in range(2, len(configurations) + 1):
        for combo in combinations(configurations, r):
            total_configs += 1
            load = base_load
            
            # Simulate dynamic load adjustment (irrelevant to final result)
            adjusted_load = load * (len(combo) % 7 + 1)
            temp_storage.append(adjusted_load)
            
            # Core efficiency calculation
            power_input = sum([c['watts'] for c in combo])
            throughput = sum([c['tps'] for c in combo])
            
            if power_input > 0:
                efficiency = throughput / power_input
                efficiencies.append(round(efficiency, 4))
    
    # Dead code path - never executed under current logic
    if len(efficiencies) > 100:
        fallback = sum(temp_storage) / len(temp_storage)
        efficiencies.append(fallback)

    # Misleading normalization step (not used)
    normalized = [e / max(efficiencies) for e in efficiencies] if efficiencies else [0]
    
    peak_efficiency = max(efficiencies) if efficiencies else 0.0
    return peak_efficiency

# System configuration data
configs = [
    {'id': 'A', 'watts': 50, 'tps': 120},
    {'id': 'B', 'watts': 75, 'tps': 180},
    {'id': 'C', 'watts': 30, 'tps': 60},
    {'id': 'D', 'watts': 100, 'tps': 220},
    {'id': 'E', 'watts': 45, 'tps': 95}
]

base_workload = 1000

# Execute main computation
result = calculate_system_efficiency(configs, base_workload)

# Irrelevant post-processing (distractor)
decay_factor = 0.95
adjusted_result = result * decay_factor ** 2

# Output the target variable
print(f"Result: {result}")