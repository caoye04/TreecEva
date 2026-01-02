from itertools import combinations

# System resource parameters
cpu_units = [2, 4, 6, 8]
memory_gb = [16, 32, 64]
storage_tb = [1, 2, 4, 8]

# Simulated performance degradation factors (irrelevant for final result)
degradation_factors = {i: 1 - 0.02 * i for i in range(5)}
baseline_score = 95.0

# Auxiliary function to compute efficiency score (partially relevant)
def compute_efficiency(cpus, mem):
    base_eff = cpus * 10 + mem / 2
    penalty = 0
    if cpus < 4:
        penalty += 5
    if mem < 32:
        penalty += 10
    return max(base_eff - penalty, 5)

# Function to validate configuration feasibility (used once)
def is_feasible(cpus, mem, storage):
    return cpus >= 2 and mem >= 16 and storage >= 1

# Secondary metric: redundancy index (distractor)
def calculate_redundancy(config_list):
    total_copies = 0
    for cfg in config_list:
        total_copies += cfg[0] // 2  # arbitrary heuristic
    return total_copies * 1.5

# Core calculation function
def calculate_system_capacity(config):
    c, m, s = config
    raw_capacity = c * m * s
    efficiency = compute_efficiency(c, m)
    scaling_factor = 1.2 if m >= 64 else 1.0
    adjusted = raw_capacity * efficiency * scaling_factor
    return int(adjusted)

# Generate all possible configurations
all_configs = []
for c in cpu_units:
    for m in memory_gb:
        for s in storage_tb:
            if is_feasible(c, m, s):  # Always true, but adds logic depth
                all_configs.append((c, m, s))

# Filter configurations above threshold (semi-relevant filtering)
efficient_configs = []
for cfg in all_configs:
    eff = compute_efficiency(cfg[0], cfg[1])
    if eff > 65:
        efficient_configs.append(cfg)

# Compute redundancy index (distractor computation)
redundancy_index = calculate_redundancy(efficient_configs)

# Find optimal config by capacity-efficiency balance
best_score = -1
optimal_config = None
for cfg in efficient_configs:
    cap = calculate_system_capacity(cfg)
    eff = compute_efficiency(cfg[0], cfg[1])
    balance_score = cap * 0.7 + eff * 30  # weighted combination

    # Early return simulation: skip underperforming
    if cap < 1000:
        continue

    if balance_score > best_score:
        best_score = balance_score
        optimal_config = cfg

# Introduce misleading intermediate (dead-end path)
temp_analysis = []
for subset in combinations(optimal_config, 2):
    temp_analysis.append(sum(subset) ** 1.5)  # unused later

# Final capacity determination
final_capacity = calculate_system_capacity(optimal_config)

# Print result as required
print(f"Result: {final_capacity}")