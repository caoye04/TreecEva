def compute_fluid_balance():
    inflows = [120, 250, 180, 95]
    outflows = [90, 300, 75, 60]
    
    # Calculate cumulative inflow and outflow
    total_in = sum(inflows)
    total_out = sum(outflows)
    
    # Compute net flow (positive means surplus, negative means deficit)
    net_flow = sum(inflows) - sum(outflows)
    
    # Auxiliary calculation: average flow rate (not directly used in answer)
    avg_flow = (total_in + total_out) / 8 if total_in + total_out > 0 else 0
    
    # Determine status based on net flow
    status_flag = 1 if net_flow > 0 else 0
    
    # Print final result as required
    print(f"Result: {net_flow}")

compute_fluid_balance()