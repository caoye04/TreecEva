def analyze_network_efficiency(nodes, edges, traffic_load):
    # Simulate network congestion analysis with irrelevant intermediate metrics
    base_capacity = 100
    overload_threshold = 85
    node_utilization = [traffic_load * (i + 1) % 90 for i in range(nodes)]
    
    # Distractor: Compute unused metric
    avg_latency = sum((i * 1.5) + 2 for i in range(nodes)) / nodes if nodes > 0 else 0
    
    # Real computation begins: construct flow matrix
    flow_matrix = [[0] * nodes for _ in range(nodes)]
    for i in range(nodes):
        for j in range(nodes):
            if i != j:
                flow_matrix[i][j] = (i + 1) * (j + 1) % 7 * (traffic_load // 5)

    # Distractor: Track redundant edge stats
    edge_load = {}
    for e in range(edges):
        src, dst = e % nodes, (e + 1) % nodes
        key = tuple(sorted([src, dst]))
        edge_load[key] = (src * dst + traffic_load) % 100
    
    # Critical function: optimize routing based on capacity constraints
    def optimize_routing(flow, capacity):
        total_flow = 0
        congestion_nodes = set()
        safe_nodes = set(range(nodes))

        for idx, usage in enumerate(node_utilization):
            if usage > overload_threshold:
                congestion_nodes.add(idx)
                safe_nodes.discard(idx)

        # Use set difference to find viable relay nodes
        relay_candidates = safe_nodes.difference({0})  # Exclude source
        backup_links = set()

        # Generate fallback paths (some are never used)
        for c in congestion_nodes:
            for r in relay_candidates:
                if flow[r][c] > 0:
                    backup_links.add((r, c))

        # Core logic: re-route flows through relays
        adjusted_flow = [row[:] for row in flow]
        for src in range(nodes):
            for dst in range(nodes):
                if src != dst and node_utilization[dst] > overload_threshold:
                    # Re-route via relay if possible
                    if relay_candidates:
                        relay = min(relay_candidates)
                        adjusted_flow[src][dst] = max(0, flow[src][dst] - 2)
                        adjusted_flow[src][relay] += 1
                        adjusted_flow[relay][dst] += 1

        # Final bandwidth calculation
        raw_sum = sum(sum(row) for row in adjusted_flow)
        penalty = len(congestion_nodes) * 3
        bonus = len(backup_links) // 2
        return int((raw_sum - penalty + bonus) * (capacity / base_capacity))

    node_capacity = 120
    final_bandwidth = optimize_routing(flow_matrix, node_capacity)
    
    # Red herring: unused diagnostic trace
    debug_trace = [f"Node {i}: {'CRITICAL' if u > overload_threshold else 'OK'}"
                   for i, u in enumerate(node_utilization)]
    
    print(f"Result: {final_bandwidth}")

# Execute scenario
dataset_nodes = 5
links = 8
current_load = 40
analyze_network_efficiency(dataset_nodes, links, current_load)