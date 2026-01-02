from collections import defaultdict

# Simulate distributed node health monitoring and load computation
def monitor_node_load():
    node_weights = [3, 7, 2, 8, 5]
    node_health = [True, False, True, True, False]
    transfer_rates = [1.2, 0.0, 0.8, 1.5, 0.0]

    # Distractor: irrelevant performance counter
    perf_counter = 0
    for _ in range(len(node_weights)):
        perf_counter += 2  # Fake work, not used later

    # Track active nodes and their effective weights
    active_nodes = []
    inactive_count = 0
    health_status_log = defaultdict(int)

    for idx, (weight, health) in enumerate(zip(node_weights, node_health)):
        if health:
            active_nodes.append(weight)
            health_status_log['healthy'] += 1
        else:
            health_status_log['unhealthy'] += 1
            inactive_count += 1  # Semi-relevant but unused later

    # Distractor: dead code path due to constant condition
    debug_mode = False
    if debug_mode:
        print(f'Debug: {inactive_count} nodes inactive')

    # Compute aggregate metrics
    active_nodes_sum = sum(active_nodes)
    avg_rate = sum(transfer_rates) / len(transfer_rates)  # Slight red herring

    # System readiness depends on majority health and minimum weight threshold
    system_ready = len(active_nodes) >= 3 and active_nodes_sum > 10

    # Efficiency factor based on healthy node distribution
    peak_weight = max(active_nodes)
    efficiency_factor = 0.9 if peak_weight >= 7 else 0.7

    # Key statement with conditional assignment
    final_load = active_nodes_sum * efficiency_factor if system_ready else 0

    # Distractor: unrelated scaling attempt (no effect)
    temp_scale = 1.0
    for rate in transfer_rates:
        if rate > 1.0:
            temp_scale *= 1.05

    # Final output
    print(f"Result: {final_load}")

    return final_load

# Execute and capture result
result = monitor_node_load()