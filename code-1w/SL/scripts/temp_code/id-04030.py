def analyze_water_reservoir():
    # Simulate a water reservoir system with inflows and outflows over time
    base_inflow = 120
    seasonal_factor = 1.25
    evaporation_rate = 0.08
    maintenance_loss = 5

    # Daily inflow variations due to rainfall (over 7 days)
    rainfall_contributions = [18, 23, 15, 0, 0, 31, 19]
    temperature_fluctuations = [32, 35, 31, 29, 30, 34, 36]  # in Celsius, irrelevant for final calc

    # Compute daily inflows
    inflows = []
    for i in range(7):
        adjusted_rainfall = rainfall_contributions[i] * 2.1
        total_daily_inflow = base_inflow + adjusted_rainfall
        if i % 3 == 0:
            total_daily_inflow *= seasonal_factor  # periodic boost
        inflows.append(int(total_daily_inflow))

    # Outflows: usage, evaporation, and scheduled drainage
    base_outflow = 95
    usage_pattern = [110, 90, 105, 88, 93, 115, 102]
    drainage_schedule = [0, 0, 20, 0, 0, 25, 0]  # extra drainage on day 3 and 6

    # Evaporation increases with temperature but we use fixed rate
    evaporation_losses = [int(evaporation_rate * 150) for _ in temperature_fluctuations]

    outflows = []
    temp_tracker = []  # dead variable - collects nothing useful
    for i in range(7):
        daily_outflow = usage_pattern[i] + evaporation_losses[i] + drainage_schedule[i]
        if daily_outflow > 130:
            daily_outflow -= maintenance_loss  # minor correction
        outflows.append(daily_outflow)

        # Useless tracking for distraction
        temp_tracker.append(temperature_fluctuations[i] + evaporation_losses[i])

    # Key computational step
    net_flow = sum(inflows) - sum(outflows)

    # Post-analysis red herring computations
    peak_inflow = max(inflows)
    peak_outflow = max(outflows)
    flow_ratio = peak_inflow / peak_outflow if peak_outflow != 0 else 0
    cumulative_surplus = 0
    for x in inflows:
        cumulative_surplus += x * 0.1  # irrelevant accumulation

    # Result printing
    print(f"Result: {net_flow}")

    return net_flow

# Execute function
analyze_water_reservoir()