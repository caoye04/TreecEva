def calculate_network_flow(capacity_map, state):
    total_nodes = len(capacity_map)
    residual = {i: {} for i in range(total_nodes)}
    inflow = [0] * total_nodes
    outflow = [0] * total_nodes

    # Initialize residual graph
    for u in capacity_map:
        for v, cap in capacity_map[u].items():
            residual[u][v] = cap
            residual[v][u] = residual.get(v, {}).get(u, 0)  # symmetric init

    # Simulate forward flow with constraints
    temp_debug_log = []
    max_iterations = 10
    iteration_count = 0
    source, sink = 0, total_nodes - 1

    while iteration_count < max_iterations:
        parent = [-1] * total_nodes
        visited = [False] * total_nodes
        stack = [source]
        visited[source] = True

        # DFS to find augmenting path
        while stack:
            node = stack.pop()
            for neighbor in residual[node]:
                if not visited[neighbor] and residual[node][neighbor] > 0:
                    visited[neighbor] = True
                    parent[neighbor] = node
                    stack.append(neighbor)
                    if neighbor == sink:
                        break

        if not visited[sink]:
            break

        # Calculate bottleneck flow
        path_flow = float('inf')
        current = sink
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual[prev][current])
            current = prev

        # Update residual capacities
        current = sink
        while current != source:
            prev = parent[current]
            residual[prev][current] -= path_flow
            residual[current][prev] += path_flow  # reverse edge
            outflow[prev] += path_flow
            inflow[current] += path_flow
            current = prev

        iteration_count += 1
        temp_debug_log.append(f"Iteration {iteration_count}: flow={path_flow}")

    # Post-processing: analyze effective throughput
    used_edges = 0
    total_residual = 0
    for u in residual:
        for v in residual[u]:
            if residual[u][v] < capacity_map.get(u, {}).get(v, 0):
                used_edges += 1
            total_residual += residual[u][v]

    # Irrelevant aggregation (distractor)
    avg_inflow = sum(inflow) / total_nodes if total_nodes else 0
    avg_outflow = sum(outflow) / total_nodes if total_nodes else 0
    flow_efficiency = (sum(inflow) + 1) / (total_residual + 1)  # smoothing

    # Core answer computation
    base_capacity = sum(capacity_map[0].values())
    utilization_rate = sum(inflow) / (base_capacity + 1e-5)
    enhanced_factor = 1 + (used_edges / (len(capacity_map) + 1))

    final_capacity = int((base_capacity * utilization_rate * enhanced_factor))

    # Dead code branch (misleading)
    if False:
        backup_estimator = 0
        for i in range(total_nodes):
            for j in range(i + 1, total_nodes):
                backup_estimator += (inflow[i] + outflow[j]) % 5
        final_capacity = backup_estimator

    return final_capacity

# Setup network topology
capacities = {
    0: {1: 10, 2: 20},
    1: {3: 10},
    2: {3: 15, 4: 5},
    3: {4: 10},
    4: {}
}
flow_state = {'active': True, 'mode': 'high'}

# Execute main logic
final_capacity = calculate_network_flow(capacities, flow_state)
print(f"Result: {final_capacity}")