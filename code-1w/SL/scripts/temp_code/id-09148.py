def analyze_flow_network():
    # Simulate a flow network with sensors and redundant calculations
    nodes = ['source', 'junction_a', 'junction_b', 'sink']
    base_inflows = [12, 8, 15]
    base_outflows = [9, 11, 7]

    # Redundant transformation: scale flows by sensor factor (not affecting final relative balance)
    sensor_correction = 1.05
    corrected_inflows = list(map(lambda x: x * sensor_correction, base_inflows))
    corrected_outflows = list(map(lambda x: x * sensor_correction, base_outflows))

    # Additional derived metrics (distractors)
    peak_inflow = max(corrected_inflows)
    avg_outflow = sum(corrected_outflows) / len(corrected_outflows)
    flow_variance = sum((x - avg_outflow) ** 2 for x in corrected_outflows)

    # Secondary validation check (dead-end computation)
    valid_nodes = []
    for i, node in enumerate(nodes[1:-1]):
        inflow_at_junction = corrected_inflows[i] if i < len(corrected_inflows) else 0
        outflow_at_junction = corrected_outflows[i] if i < len(corrected_outflows) else 0
        if abs(inflow_at_junction - outflow_at_junction) < 5 * sensor_correction:
            valid_nodes.append(node)

    # Compute auxiliary structure: zipped diagnostics (semi-relevant)
    diagnostics = []
    for idx, (in_val, out_val) in enumerate(zip(corrected_inflows, corrected_outflows)):
        balance = in_val - out_val
        diagnostics.append({'step': idx, 'imbalance': balance})

    # Core logic: actual net flow calculation (target)
    temp_buffer = [x for x in corrected_inflows if x > 10]
    buffer_energy = sum(temp_buffer) * 0.01  # unused energy metric (distractor)

    inflows = [int(x) for x in corrected_inflows]  # discretize for final use
    outflows = [int(x) for x in corrected_outflows]
    net_flow = sum(inflows) - sum(outflows)

    # Print result as required
    print(f"Result: {net_flow}")

    return net_flow

analyze_flow_network()