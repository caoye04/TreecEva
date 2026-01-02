def analyze_network_flow():
    # Simulate network node performance under variable load
    node_ids = ['N1', 'N2', 'N3', 'N4', 'N5']
    base_capacity = [80, 120, 95, 110, 75]
    maintenance_overhead = [8, 15, 10, 12, 9]
    traffic_load = [70, 95, 88, 105, 60]
    efficiency_factor = [0.92, 0.88, 0.90, 0.85, 0.94]

    # Irrelevant diagnostic metrics (distractor)
    latency_spikes = [3, 1, 4, 0, 2]
    packet_loss_rate = [0.01, 0.03, 0.02, 0.05, 0.01]
    security_checks_passed = [True, True, False, True, True]

    # Compute adjusted capacity with overhead (semi-relevant)
    adjusted_capacity = [
        (cap - overhead) * eff
        for cap, overhead, eff in zip(base_capacity, maintenance_overhead, efficiency_factor)
    ]

    # Simulate redundant status check (dead code path - distractor)
    system_status = []
    for i, chk in enumerate(security_checks_passed):
        if chk:
            system_status.append(f'{node_ids[i]}: SECURE')
        else:
            system_status.append(f'{node_ids[i]}: WARNING')

    # Misleading utilization attempt (not used in final result)
    temp_utilization = [
        load / adj_cap for load, adj_cap in zip(traffic_load, adjusted_capacity)
    ]

    # Critical function: actual calculation logic
    def calculate_utilization(nodes, loads):
        total_available = 0
        total_used = 0
        for idx, (node, base, overhead, eff) in enumerate(
            zip(node_ids, base_capacity, maintenance_overhead, efficiency_factor)
        ):
            net_capacity = (base - overhead) * eff
            if net_capacity > 90:  # Filter high-capacity nodes only
                total_available += net_capacity
                total_used += loads[idx]

        # Apply correction for burst tolerance
        burst_buffer = sum(1 for x in latency_spikes if x > 2) * 5  # Distractor usage
        return int((total_used / total_available) * 100) if total_available > 0 else 0

    # Execute main computation
    final_capacity = calculate_utilization(network_nodes=node_ids, traffic_load=traffic_load)

    # Redundant aggregation (irrelevant)
    avg_latency = sum(latency_spikes) / len(latency_spikes)
    total_loss = sum(packet_loss_rate)

    print(f"Result: {final_capacity}")

analyze_network_flow()