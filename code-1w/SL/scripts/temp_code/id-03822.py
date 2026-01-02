def calculate_water_balance():
    inflows = [120, 85, 200, 90]
    outflows = [110, 95, 75, 100]
    
    # Calculate total rainfall contribution
    total_rainfall = sum(inflows[:2])
    
    # Calculate irrigation usage (irrelevant to final result)
    irrigation_used = outflows[1] * 0.8
    
    # Track number of monitoring stations
    station_count = len(inflows)
    
    # Compute net water flow in reservoir
    net_flow = sum(inflows) - sum(outflows)
    
    # Normalize flow per station (distractor)
    normalized_flow = net_flow / station_count if station_count else 0
    
    # Print final result as required
    print(f"Result: {net_flow}")

calculate_water_balance()