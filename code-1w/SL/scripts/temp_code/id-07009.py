def calculate_fluid_dynamics():
    inflows = [12.5, 8.0, 14.3, 6.7, 9.1]
    outflows = [3.2, 7.8, 5.4, 11.0, 2.9]
    adjustments = [0.0, -1.2, 4.5]

    # Initial pressure calculation (irrelevant to final result)
    base_pressure = inflows[0] * 0.8
    temp_buffer = [x * 1.1 for x in outflows]

    # Key computation step
    net_flow = sum(inflows[:3]) - sum(outflows[1:4]) + adjustments[-1]

    # Post-processing (no effect on net_flow)
    if net_flow > 0:
        status = "positive"
    else:
        status = "non-positive"

    # Final output
    print(f"Result: {net_flow}")

calculate_fluid_dynamics()