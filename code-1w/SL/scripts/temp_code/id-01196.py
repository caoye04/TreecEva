def compute_fluid_dynamics():
    # Simulate a fluid dynamics scenario with multiple input/output channels
    
    # Channel data: index 0 = inflow, index 1 = outflow (in liters per second)
    channel_readings = [
        [12.5, 8.3], [15.0, 9.1], [7.2, 10.4], [18.3, 7.9],
        [9.8, 12.2], [14.1, 6.7], [11.6, 13.5], [16.7, 8.8]
    ]
    
    # Extract inflow and outflow sequences using slicing
    all_inflows = [entry[0] for entry in channel_readings]
    all_outflows = [entry[1] for entry in channel_readings]
    
    # Misleading intermediate calculations (distractors)
    peak_inflow = max(all_inflows)
    peak_outflow = max(all_outflows)
    avg_inflow = sum(all_inflows) / len(all_inflows)
    avg_outflow = sum(all_outflows) / len(all_outflows)
    
    # Secondary analysis (not used in final result)
    sustained_high_inflow = [x for x in all_inflows if x > 10.0]
    fluctuation_index = len(sustained_high_inflow) / len(all_inflows)
    
    # Accumulation logic with conditional filtering
    threshold = 10.5
    filtered_inflows = []
    filtered_outflows = []
    
    for i in range(len(channel_readings)):
        reading_pair = channel_readings[i]
        if all_inflows[i] >= threshold:
            filtered_inflows.append(all_inflows[i])
        if all_outflows[i] < avg_outflow:
            filtered_outflows.append(all_outflows[i])
    
    # Compute total inflow from high-throughput channels
    inflow_sum = sum(filtered_inflows)
    
    # Compute total outflow from below-average channels
    outflow_sum = sum(filtered_outflows)
    
    # Key statement
    net_flow = inflow_sum - outflow_sum
    
    # Additional irrelevant transformation (dead-end)
    normalized_net = net_flow / (peak_inflow + peak_outflow) if peak_inflow else 0
    efficiency_ratio = fluctuation_index * 100 if normalized_net > 0 else 0
    
    # Final output
    print(f"Result: {net_flow}")
    
compute_fluid_dynamics()