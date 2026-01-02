def analyze_water_flow():
    # Sensor readings from different stations (in cubic meters per hour)
    station_a_in = {80, 120, 100, 90}
    station_b_in = {110, 95, 105}
    station_c_out = {75, 85, 95, 105}
    station_d_out = {100, 90}

    # Auxiliary monitoring data (irrelevant to final calculation)
    pressure_readings = [101.3, 102.1, 100.8, 103.5, 99.7]
    temperature_log = [-2.1, 0.5, 1.3, -1.0]  # Degraded sensors, not used

    # Compute total inflow from stations A and B
    inflow_union = station_a_in.union(station_b_in)
    inflow_filtered = {x for x in inflow_union if x > 85}  # Only significant flows
    inflow_sum = sum(inflow_filtered)

    # Compute total outflow from stations C and D
    outflow_combined = station_c_out | station_d_out
    outflow_filtered = outflow_combined.difference({95})  # Remove known calibration error
    outflow_sum = sum(outflow_filtered)

    # Track auxiliary state (dead code path - never accessed later)
    flow_stability_score = 0
    if len(inflow_filtered) > len(outflow_filtered):
        flow_stability_score += 10
    else:
        flow_stability_score -= 5

    # Misleading intermediate computation (not used in final result)
    peak_diff = max(inflow_filtered) - min(outflow_filtered)
    avg_inflow = round(sum(inflow_filtered) / len(inflow_filtered), 2)

    # Core calculation: net water flow
    net_flow = inflow_sum - outflow_sum

    # Additional red herring: historical comparison (not affecting result)
    historical_baseline = 380
    deviation_index = abs(net_flow - historical_baseline) / historical_baseline

    # Output target result
    print(f"Result: {net_flow}")

analyze_water_flow()