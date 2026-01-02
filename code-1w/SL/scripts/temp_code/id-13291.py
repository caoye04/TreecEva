from functools import reduce

# Simulate data transformation pipeline for network flow analysis
def main():
    nodes = ['A', 'B', 'C', 'D', 'E']
    base_weights = [4, 7, 2, 9, 5]
    
    # Irrelevant transformation: unused weight mapping
    temp_scale = lambda x: (x * 1.8) + 32
    scaled_temps = list(map(temp_scale, base_weights))

    # Relevant edge structure: directional flows between nodes
    edges = [
        ('A', 'B', 8), ('B', 'C', 6), ('C', 'D', 7), ('D', 'E', 5),
        ('A', 'C', 3), ('B', 'D', 4), ('C', 'E', 9)
    ]

    # State tracking with extra fields (some irrelevant)
    state_map = {node: {
        'active': True,
        'buffer': idx * 2,
        'priority': base_weights[idx],
        'last_seen': None,  # Unused field
        'flow_cap': 0
    } for idx, node in enumerate(nodes)}

    # Misleading pre-computation (dead-end calculation)
    total_potential = sum(w[2] for w in edges) * len(nodes)
    shadow_factor = total_potential // 10

    # Initialize flow tracking
    flow_registry = {node: 0 for node in nodes}
    
    # Update flow capacity using indirect priority mapping
    for node, props in state_map.items():
        if props['priority'] > 4:
            state_map[node]['flow_cap'] = props['priority'] * 2
        else:
            state_map[node]['flow_cap'] = props['priority']

    # Auxiliary function to compute derived weight (not directly used later)
    def get_derived_flow(edge):
        src, dst, base = edge
        return base + state_map[src]['buffer'] - (state_map[dst]['priority'] // 3)
    
    derived_flows = [get_derived_flow(e) for e in edges]

    # Real computation begins: filter and aggregate effective flows
    valid_paths = list(filter(lambda e: e[2] > 5, edges))
    
    # Accumulate flow per destination
    for src, dst, weight in valid_paths:
        flow_registry[dst] += weight
        flow_registry[src] -= weight // 2  # Reverse impact

    # Secondary adjustment based on flow_cap
    adjustment_rule = lambda f, cap: f + (cap // 4)
    
    for node in nodes:
        flow_registry[node] = adjustment_rule(flow_registry[node], state_map[node]['flow_cap'])
    
    # Core calculation isolated in function to increase nesting depth
    def calculate_net_flow(edges, state):
        total_flow = 0
        for e in edges:
            src, dst, w = e
            src_prio = state[src]['priority']
            dst_prio = state[dst]['priority']
            if src_prio < dst_prio:
                total_flow += w * 2
            elif src_prio == dst_prio:
                total_flow += w
            else:
                total_flow -= w // 3
        return total_flow + shadow_factor  # Incorporates misleading global

    intermediate_check = reduce(lambda a, b: a * b // 2, [e[2] for e in valid_paths if e[2] < 9], 1)

    final_flux = calculate_net_flow(edges, state_map)

    # Print result as required
    print(f"Result: {final_flux}")

main()