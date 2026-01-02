def evaluate_system_load():
    node_loads = [12, 15, 8, 22, 17, 9]
    threshold = 10
    high_load_nodes = {i for i, load in enumerate(node_loads) if load > threshold}
    low_load_nodes = {i for i, load in enumerate(node_loads) if load <= threshold}

    # Irrelevant computation: simulate latency adjustments (not used later)
    base_latency = 2.5
    adjusted_latencies = [base_latency * (1 + (load / 100)) for load in node_loads]
    average_latency = sum(adjusted_latencies) / len(adjusted_latencies)

    # State tracking with distraction
    activation_log = {}
    for idx in range(len(node_loads)):
        if idx in high_load_nodes:
            activation_log[idx] = 'HIGH'
        else:
            activation_log[idx] = 'LOW'

    # Core logic begins
    nominal_capacity = 500
    overload_penalty = len(high_load_nodes) * 20
    system_reserve = nominal_capacity - overload_penalty

    # Distractor: unused capacity redistribution
    redistribution_factor = 0.1
    redistributed = {idx: node_loads[idx] * redistribution_factor for idx in high_load_nodes}

    operational_nodes = len(node_loads) - len(high_load_nodes) // 2  # Some nodes can handle load

    # Key statement
    final_capacity = system_reserve // operational_nodes

    # Dead code path - never executed but adds cognitive load
    if False:
        fallback_mode = True
        final_capacity = max(final_capacity, 30)

    # Print result as required
    print(f"Result: {final_capacity}")

    return final_capacity

# Execute function
evaluate_system_load()