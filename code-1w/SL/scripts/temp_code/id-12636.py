def analyze_network_traffic():
    # Simulate network node traffic analysis with extraneous computations
    timestamps = [100, 105, 110, 115, 120]
    base_load = 7
    inflows = [t % 13 + base_load for t in timestamps if t > 102]
    outflows = [max((125 - t), 5) for t in timestamps]

    # Distractor: Irrelevant signal processing simulation
    signal_strength = [t * 0.8 for t in timestamps]
    avg_signal = sum(signal_strength) / len(signal_strength)
    thresholded = [s if s > 80 else 0 for s in signal_strength]  # Dead code branch

    # Distractor: Unused data transformation
    temp_buffer = []
    for i, val in enumerate(inflows):
        shifted = val << 1  # Bit shift not used in final logic
        temp_buffer.append(shifted)

    # Real computation begins
    backup_inflows = inflows.copy()
    correction_factor = 0
    for idx, out in enumerate(outflows):
        if out % 5 == 0:
            correction_factor += idx

    # Key state tracking with minor interference
    active_nodes = 0
    for inflow in inflows:
        if inflow > 8:
            active_nodes += 1

    # Core result calculation
    net_flow = sum(inflows) - sum(outflows)

    # Additional red herring: unused diagnostic metric
    efficiency_ratio = (sum(inflows) / (sum(outflows) + 1)) if outflows else 0

    # Output the required result
    print(f"Result: {net_flow}")

analyze_network_traffic()