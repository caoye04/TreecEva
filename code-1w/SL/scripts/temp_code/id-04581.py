def calculate_network_load():
    # Simulate time-based packet arrival across network nodes
    timestamps = [1.1, 1.3, 1.5, 1.7, 1.9, 2.1, 2.3, 2.5]
    packets = [12, 8, 15, 6, 20, 10, 18, 14]

    # Node configuration: id -> base_capacity mapping
    node_config = {0: 25, 1: 30, 2: 20, 3: 35}

    # Initialize load tracking per node
    node_loads = {node: 0 for node in node_config}

    # Auxiliary computation: average inter-arrival time (distractor)
    total_interval = 0
    for i in range(1, len(timestamps)):
        total_interval += timestamps[i] - timestamps[i]
    avg_interval = total_interval / (len(timestamps) - 1) if len(timestamps) > 1 else 0

    # Real processing: distribute packets to nodes cyclically
    temp_buffer = []
    for idx, (ts, pkt_size) in enumerate(zip(timestamps, packets)):
        assigned_node = idx % len(node_config)
        # Apply exponential decay on older packets (simulated with index distance)
        decay_factor = 0.95 ** (len(packets) - idx - 1)
        effective_size = int(pkt_size * decay_factor)
        temp_buffer.append(effective_size)

        if assigned_node in node_loads:
            node_loads[assigned_node] += effective_size

    # Misleading intermediate: normalize loads by capacity (not used later)
    normalized = {}
    for node, load in node_loads.items():
        cap = node_config[node]
        norm_value = load / cap if cap > 0 else 0
        normalized[node] = round(norm_value, 3)

    # Extract current loads as list for final evaluation
    current_loads = [node_loads[n] for n in sorted(node_loads)]

    # Key statement
    final_load = max(current_loads)

    # Print result for verification
    print(f"Result: {final_load}")

    return final_load

# Execute function
calculate_network_load()