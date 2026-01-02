def balance_workload(nodes, efficiency):
    total_capacity = 0
    adjusted_weights = []
    temp_sum = 0

    for i, node in enumerate(nodes):
        load_factor = (i + 1) * efficiency[i] % 7
        capacity = node * (load_factor + 1)
        total_capacity += capacity
        adjusted_weights.append(capacity if capacity > 10 else 10)

    normalized = [w / total_capacity for w in adjusted_weights]

    # Simulate intermediate diagnostics (irrelevant to final result)
    diagnostic_trace = 0
    for idx, norm in enumerate(normalized):
        if idx % 2 == 0:
            diagnostic_trace += norm * 100
    
    # Misleading computation: looks important but unused
    theoretical_max = max(nodes) * max(efficiency) * len(nodes)
    safety_margin = theoretical_max * 0.1

    # Actual workload distribution logic
    cumulative_load = 0
    for weight in normalized:
        cumulative_load += weight * 1000  # scale load
    
    # Final adjustment based on system resilience index (constant)
    resilience = 1.05
    final_load = int(cumulative_load / len(nodes) * resilience)

    # Dead code path - never executed due to fixed condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {final_load}')

    return final_load

# Input data
nodes = [8, 12, 5, 15]
efficiency = [0.8, 0.9, 0.6, 0.75]

# Auxiliary variables with no impact
baseline = sum(nodes) * 0.5
scaling_factor = 2.1
offset_correction = 17

final_load = balance_workload(nodes, efficiency)
print(f'Result: {final_load}')