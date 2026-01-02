def calculate_water_flow():
    # Simulate sensor readings from irrigation system over 24 hours
    hourly_readings = [23, 18, 25, 30, 20, 15, 12, 35, 40, 38, 33, 28, 26, 29, 31, 34, 27, 24, 22, 20, 19, 17, 16, 14]

    # Extract daytime (6 AM - 6 PM) and nighttime flows for analysis
    daytime = hourly_readings[6:18]
    nighttime = hourly_readings[18:] + hourly_readings[:6]

    # Calculate peak and average flows (distractor computations)
    peak_daytime_flow = max(daytime)
    peak_night_flow = max(nighttime)
    avg_flow = sum(hourly_readings) / len(hourly_readings)

    # Identify maintenance periods (hours with flow below threshold)
    low_flow_hours = [i for i, x in enumerate(hourly_readings) if x < 18]
    maintenance_count = len(low_flow_hours)

    # Classify high-demand periods
    high_demand = [x for x in hourly_readings if x > 30]
    demand_intensity = sum(high_demand)

    # Actual inflow/outflow modeling
    base_inflow = [x * 1.1 for x in daytime]  # Daytime adjusted inflows
    base_outflow = [x * 0.9 for x in nighttime]  # Nighttime adjusted outflows

    # Apply weather correction factor (simulated constant)
    corrected_inflows = [int(x * 0.95) for x in base_inflow]
    corrected_outflows = [int(x * 1.05) for x in base_outflow]

    # Final computation step
    inflows = corrected_inflows[1::2]  # Every other hour inflow (reduced data)
    outflows = corrected_outflows[::2]   # Alternating outflow sampling

    # Key statement
    net_flow = sum(inflows) - sum(outflows)

    # Additional irrelevant tracking
    flow_efficiency = (sum(inflows) / sum(outflows)) if sum(outflows) > 0 else 0
    fluctuation_index = max(inflows) - min(outflows)

    return net_flow

result = calculate_water_flow()
print(f"Result: {result}")