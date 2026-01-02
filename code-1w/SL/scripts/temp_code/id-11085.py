def analyze_system_efficiency(elements, threshold=0.75):
    # Irrelevant transformation: normalize elements (not used in final result)
    normalized = [round(e / sum(elements), 3) for e in elements]
    above_threshold = [e for e in normalized if e > threshold]
    return len(above_threshold)

# System node parameters (simulated sensor readings)
thermal_nodes = [23.4, 19.8, 21.2, 25.1, 18.7]
pressure_adj = [3.2, 4.1, 2.8, 5.5, 3.9]
dummy_weights = [0.91, 0.96, 0.88, 0.77, 0.92]  # Unused weighting factors

# Misleading intermediate calculation (dead-end path)
weighted_thermal = [temp * (w + 0.1) for temp, w in zip(thermal_nodes, dummy_weights)]
avg_weighted = sum(weighted_thermal) / len(weighted_thermal)

# Set operations: identify high-variance sensors
thermal_set = set(round(t) for t in thermal_nodes)
pressure_set = set(round(p) for p in pressure_adj)
overlap_sensors = thermal_set & pressure_set  # intersection: minor distraction
unique_sensors = thermal_set ^ pressure_set  # symmetric difference

# Logical filtering: determine active nodes based on combined thresholds
active_flags = []
for i in range(len(thermal_nodes)):
    is_thermal_active = thermal_nodes[i] > 20.0
    is_pressure_critical = pressure_adj[i] >= 4.0
    # Complex condition with short-circuit behavior
    flag = is_thermal_active and (is_pressure_critical or dummy_weights[i] > 0.9)
    active_flags.append(flag)

# Calculate derived pressures with irrelevant offset
adjusted_pressures = []
for p in pressure_adj:
    adj_p = p * 1.08 - 0.5
    adjusted_pressures.append(adj_p)

# Core computation: net flow depends only on original thermal and pressure values
def calculate_net_flow(temps, press):
    base_flow = 0.0
    for i in range(len(temps)):
        if temps[i] > 20.0 and press[i] > 4.0:
            base_flow += temps[i] * press[i] * 0.3
        elif temps[i] > 20.0:
            base_flow += temps[i] * 0.8
        else:
            base_flow -= press[i] * 0.5
    return int(base_flow)  # Final answer is integer

# Execution point of interest
net_flux = calculate_net_flow(thermal_nodes, pressure_adj)

# Additional red herring: unused function call
redundant_count = analyze_system_efficiency([len(thermal_nodes), len(pressure_adj), 5])

print(f"Result: {net_flux}")