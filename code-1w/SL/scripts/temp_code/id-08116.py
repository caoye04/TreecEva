def compute_fluid_dynamics():
    # Simulate a fluid dynamics calculation with irrelevant heat and pressure variables
    inflows = [12, 15, 23, 19, 14]
    outflows = [8, 17, 20, 12]

    # Irrelevant thermal data (distractor)
    temperatures = [22.1, 23.5, 21.8, 24.0, 22.7]
    avg_temp = sum(temperatures) / len(temperatures)
    temp_variance = sum((t - avg_temp) ** 2 for t in temperatures) / len(temperatures)

    # Pressure coefficients (dead code path)
    pressures = [101.3, 102.1, 100.9, 103.0]
    if len(pressures) > 5:
        max_pressure = max(pressures)
    else:
        max_pressure = None  # Unused fallback

    # Real computation starts here
    total_in = 0
    for idx, val in enumerate(inflows):
        total_in += val * 1.0  # Simulate sensor weighting (neutral effect)

    total_out = 0
    for flow in outflows:
        total_out += flow

    # Auxiliary container for unrelated metadata
    metadata = {
        'version': '2.1',
        'calibration': 'passed',
        'inflow_count': len(inflows),
        'outflow_count': len(outflows)
    }

    # Key computational step
    net_flow = sum(inflows) - sum(outflows)

    # Additional distraction: zipping unrelated sequences
    paired_data = list(zip(inflows, temperatures[:len(inflows)]))
    weighted_thermal_flow = 0
    for inflow, temp in paired_data:
        weighted_thermal_flow += inflow * (temp / avg_temp)

    # Final output
    print(f"Result: {net_flow}")

compute_fluid_dynamics()