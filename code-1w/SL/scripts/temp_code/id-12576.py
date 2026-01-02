def analyze_water_flow():
    # Simulate sensor readings for water flow in a treatment plant
    raw_inflow_data = [120, 135, 140, 130, 150, 160, 145]
    raw_outflow_data = [110, 130, 138, 132, 148, 155, 142]

    # Filter valid readings (above threshold)
    min_valid_flow = 125
    filtered_inflows = [x for x in raw_inflow_data if x >= min_valid_flow]
    filtered_outflows = [x for x in raw_outflow_data if x >= min_valid_flow]

    # Calculate base sums
    inflow_sum = sum(filtered_inflows)
    outflow_sum = sum(filtered_outflows)

    # Track peak values (distractor - not used in final result)
    peak_inflow = max(filtered_inflows)
    peak_outflow = max(filtered_outflows)
    flow_margin = peak_inflow - peak_outflow  # Red herring

    # Efficiency calculation (irrelevant to net flow)
    efficiency_ratio = 0.0
    if inflow_sum > 0:
        efficiency_ratio = outflow_sum / inflow_sum * 100

    # Historical average comparison (distractor)
    historical_avg_inflow = 142
    deviation_score = abs(inflow_sum / len(filtered_inflows) - historical_avg_inflow)

    # Core logic: compute net water flow imbalance
    net_flow = inflow_sum - outflow_sum

    # Log intermediate stats (dead code path - no effect)
    debug_stats = {
        'total_in': inflow_sum,
        'total_out': outflow_sum,
        'peak_diff': flow_margin,
        'efficiency': efficiency_ratio
    }

    # Final output
    print(f"Result: {net_flow}")

analyze_water_flow()