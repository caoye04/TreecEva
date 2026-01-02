def calculate_network_equilibrium():
    nodes = [12, 7, 9, 15, 4, 8]
    connections = [5, 3, 6, 2, 7, 5]
    
    # Irrelevant preprocessing: normalize node values (not used in final calculation)
    normalized_nodes = [round(n / sum(nodes), 3) for n in nodes]
    temp_sum = 0
    for val in normalized_nodes:
        temp_sum += val * 100
    scaling_factor = temp_sum / len(nodes)

    # Distractor: simulate dummy cycles
    dummy_cycles = 0
    for i in range(len(connections)):
        if connections[i] % 2 == 0:
            dummy_cycles += 1

    # Actual logic begins
    flow_map = []
    for idx, (node, conn) in enumerate(zip(nodes, connections)):
        contribution = node * (conn + 1)
        adjustment = 0
        for _ in range(2):
            adjustment += idx % 3
        flow_map.append(contribution - adjustment)

    # Secondary distractor: unused energy tracking
    energy_levels = []
    for i, flow in enumerate(flow_map):
        energy = flow * 0.85 if i % 2 == 0 else flow * 0.75
        energy_levels.append(round(energy, 2))

    # Core computation
    total_flow = sum(flow_map)
    cycle_count = 0
    for i, n in enumerate(nodes):
        if n > 8:
            cycle_count += 1
        if i > 0 and nodes[i] < nodes[i-1]:
            cycle_count += 1

    # Key statement
    equilibrium = total_flow / (cycle_count + 1)
    
    print(f"Result: {equilibrium}")

if __name__ == "__main__":
    calculate_network_equilibrium()