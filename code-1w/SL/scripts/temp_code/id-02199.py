def calculate_thermal_metric(state):
    base_factor = 1.7
    penalty_rate = 0.3
    efficiency_map = {0: 0.1, 1: 0.4, 2: 0.9, 3: 1.5}
    overload_adjustment = 0
    transient_buffer = 0

    # Irrelevant initialization (distractor)
    diagnostic_log = []
    for i in range(len(state)):
        if state[i] > 2:
            diagnostic_log.append(f"Node {i} overheating")

    # Real computation begins
    active_nodes = 0
    total_stress = 0
    stress_profile = []

    for level in state:
        if level >= 1:
            active_nodes += 1
        total_stress += level * level  # Stress grows quadratically
        stress_profile.append(level * base_factor)

    avg_stress = total_stress / len(state) if state else 0

    # Secondary irrelevant computation (misleading adjustment)
    for reading in stress_profile:
        transient_buffer += reading * 0.05
        if transient_buffer > 10:
            overload_adjustment += 1  # Dead code path, never reached

    # Core logic: capacity depends on active nodes and average stress
    raw_capacity = active_nodes * efficiency_map.get(int(avg_stress), 1.5)

    # Final adjustment using only relevant factors
    if avg_stress > 2.0:
        raw_capacity -= int(avg_stress)

    return int(raw_capacity)

# Simulated cluster thermal state (0=off, 1=low, 2=medium, 3=high)
cluster_state = [2, 3, 1, 3, 2, 0, 3, 1]

# Misleading pre-computations (distractors)
baseline_diagnostic = sum([x ** 0.5 for x in cluster_state if x > 0])
stale_flag = False
for i in range(len(cluster_state)):
    if cluster_state[i] == 0:
        stale_flag = True
        break

# Key assignment
thermal_capacity = calculate_thermal_metric(cluster_state)

# Output result
print(f"Result: {thermal_capacity}")