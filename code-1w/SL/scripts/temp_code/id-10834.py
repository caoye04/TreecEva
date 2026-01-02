def calculate_network_balance():
    # Simulate data packet flows in a network segment
    inflows = [120, 150, 94, 212, 87]
    outflows = [97, 145, 89, 205, 110]

    # Auxiliary diagnostic variables (minimal interference)
    peak_inflow = max(inflows)
    avg_outflow = sum(outflows) / len(outflows)
    flow_efficiency = list(map(lambda x: x * 0.95, inflows))  # hypothetical loss adjustment

    # Key computational step
    net_flow = sum(inflows) - sum(outflows)
    
    # Additional benign operation to slightly increase logic depth
    if net_flow > 0:
        net_flow += 10  # bonus for surplus
    else:
        net_flow -= 5

    return net_flow

result = calculate_network_balance()
print(f"Result: {result}")