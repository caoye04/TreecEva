def analyze_signal_strength(signal_data, threshold=0.75):
    strong_signals = [s for s in signal_data if s > threshold]
    normalized = [round(s / max(strong_signals), 3) for s in strong_signals] if strong_signals else [0.0]
    avg_normalized = sum(normalized) / len(normalized)
    return avg_normalized

signal_readings = [0.82, 0.45, 0.91, 0.67, 0.76, 0.88, 0.53]
dummy_stat = analyze_signal_strength(signal_readings, 0.5)  # Irrelevant call, distractor

link_matrix = [
    [1, 0, 1, 1],
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 0, 1, 0]
]

efficiency_map = {
    (0, 0): 0.91, (0, 2): 0.87, (0, 3): 0.75,
    (1, 1): 0.95, (1, 2): 0.68,
    (2, 0): 0.82, (2, 1): 0.79, (2, 2): 0.93, (2, 3): 0.81,
    (3, 0): 0.65, (3, 2): 0.71
}

# Red herring: unused matrix transformation
def transform_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

dummy_matrix = transform_matrix(link_matrix)

# Tracking active links and their effective capacity
total_links = 0
active_efficiencies = []
redundant_pairs = set()

for i, row in enumerate(link_matrix):
    for j, active in enumerate(row):
        if active:
            total_links += 1
            key = tuple(sorted((i, j)))
            if key not in redundant_pairs:
                redundant_pairs.add(key)
                if (i, j) in efficiency_map:
                    active_efficiencies.append(efficiency_map[(i, j)])

# Compute baseline metrics
avg_efficiency = sum(active_efficiencies) / len(active_efficiencies) if active_efficiencies else 0
max_efficiency = max(active_efficiencies) if active_efficiencies else 0

# Simulate load distribution across nodes
node_load = [0] * len(link_matrix)
for i, row in enumerate(link_matrix):
    node_load[i] = sum(row)

# Secondary metric: correlation between load and efficiency (not used in final result)
load_efficiency_corr = 0.0
if len(node_load) == len(active_efficiencies):
    mean_load = sum(node_load) / len(node_load)
    mean_eff = avg_efficiency
    cov = sum((node_load[i // 4] - mean_load) * (eff - mean_eff) 
              for i, eff in enumerate(active_efficiencies))
    load_efficiency_corr = cov / (len(active_efficiencies) or 1)

# Core calculation function
def calculate_network_capacity(links, efficiency_lookup):
    total_capacity = 0.0
    for i, row in enumerate(links):
        for j, enabled in enumerate(row):
            if enabled and (i, j) in efficiency_lookup:
                base_power = (i + 1) * (j + 1)  # arbitrary weight
                efficiency_factor = efficiency_lookup[(i, j)]
                link_contribution = base_power * efficiency_factor
                total_capacity += link_contribution
    return round(total_capacity, 4)

# Critical statement
final_capacity = calculate_network_capacity(link_matrix, efficiency_map)

print(f"Result: {final_capacity}")