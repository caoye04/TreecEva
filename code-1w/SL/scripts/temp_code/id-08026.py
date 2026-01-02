def analyze_flow():
    # Simulate sensor readings for fluid dynamics analysis
    raw_readings = [23.5, 18.2, 45.7, 12.8, 33.1, 27.4, 19.6, 36.3]
    
    # Preprocess: filter anomalous spikes and normalize
    filtered_readings = [x for x in raw_readings if x > 15]
    normalized = [round(x * 1.03, 2) for x in filtered_readings]  # calibration factor
    
    # Segment into inflow and outflow zones
    inflows = normalized[::2]  # every even-indexed as inflow
    outflows = normalized[1::2]  # every odd-indexed as outflow
    
    # Dummy transformation: simulate pressure adjustment (not used in final)
    adjusted_outflows = [max(0, x - 3.5) for x in outflows]
    temp_storage = [x * 0.95 for x in adjusted_outflows]  # red herring
    
    # Calculate system metrics
    total_inflow = sum(inflows)
    total_outflow = sum(outflows)
    midpoint = len(outflows) // 2
    
    # Key computation with slicing
    net_flow = sum(inflows) - sum(outflows[:midpoint])
    
    # Extraneous diagnostics
    avg_inflow = total_inflow / len(inflows) if inflows else 0
    fluctuation_index = max(inflows) - min(inflows)
    dummy_flag = True if fluctuation_index > 20 else False
    
    # Final result output
    print(f"Result: {net_flow}")

analyze_flow()