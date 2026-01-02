from itertools import combinations

# Simulate fluid dynamics in a closed network with pressure adjustments
def calculate_network_state():
    nodes = [103, 155, 201, 98, 134]
    baseline_offset = 42
    threshold = 50
    temp_accumulator = 0
    debug_sequence = []

    # Irrelevant preprocessing: generate all 2-node combos (not used in final logic)
    pair_magnitudes = []
    for pair in combinations(nodes, 2):
        magnitude = (pair[0] + pair[1]) % 7
        pair_magnitudes.append(magnitude)

    # Real computation begins
    inflow = 0
    outflow = 0
    adjustment_factor = 0

    for idx, node in enumerate(nodes):
        if idx % 2 == 0:
            inflow += node * (idx + 1)
            temp_accumulator += node  # semi-relevant, distracts from core
        else:
            outflow += node // ((idx + 1) // 2 + 1)
            if node > 100:
                adjustment_factor += 5
            else:
                adjustment_factor -= 2

    # Secondary distraction: simulate unused error checking
    error_flags = []
    for val in nodes:
        if val < 0:
            error_flags.append(True)
    # This block does nothing since all vals are positive

    net_flow = inflow - outflow + adjustment_factor

    # Key statement
    equilibrium_score = net_flow if abs(net_flow) > threshold else baseline_offset

    # Debug logging (irrelevant to result)
    for i in range(3):
        debug_sequence.append(equilibrium_score % (i + 2))

    # Final output
    print(f"Result: {equilibrium_score}")

    return equilibrium_score

calculate_network_state()