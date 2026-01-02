def analyze_water_reservoir():
    # Initial reservoir parameters
    base_capacity = 50000
    current_level = 32780
    max_inflow_rate = 420
    min_outflow_rate = 380

    # Simulated hourly data over a day (24 hours)
    hourly_rainfall = [0, 0, 0, 2, 5, 8, 12, 18, 25, 30, 28, 20, 15, 10, 7, 5, 3, 2, 1, 1, 0, 0, 0, 0]
    temperature_celsius = [18, 17, 16, 15, 15, 16, 18, 20, 23, 25, 27, 28, 29, 30, 29, 28, 27, 25, 24, 23, 22, 21, 20, 19]

    # Evaporation rate depends on temperature (simplified model: 0.5% per degree above 20)
    evaporation_rates = [(0.005 * (temp - 20)) if temp > 20 else 0 for temp in temperature_celsius]

    # Compute total evaporation loss over the day (in cubic meters)
    total_evaporation_loss = sum(evap * current_level for evap in evaporation_rates)

    # Rainwater contributes to inflow (each mm rainfall adds 100 m³)
    total_rain_contribution = sum(rain_mm * 100 for rain_mm in hourly_rainfall)

    # Operational constraints
    maintenance_mode = False
    emergency_release = False

    # Complex logic for inflow and outflow
    planned_inflow = 0
    for hour in range(24):
        if hour in range(6, 12):  # Peak collection period
            planned_inflow += max_inflow_rate * 1.2  # 20% boost during peak
        elif hour in range(12, 18):
            planned_inflow += max_inflow_rate * 0.8
        else:
            planned_inflow += max_inflow_rate * 0.3

    # Outflow includes scheduled supply and leakage
    scheduled_supply = sum([min_outflow_rate * (1 + 0.1 * i) for i in range(1, 25)])
    base_leakage = 1200  # Fixed daily leakage

    # Environmental compliance checks (irrelevant to final answer but adds cognitive load)
    protected_species_present = True
    seasonal_restrictions = (temperature_celsius[12] > 28)
    compliance_buffer = 500 if protected_species_present and seasonal_restrictions else 0

    # Actual inflow combines planned and rain contribution
    inflow = planned_inflow + total_rain_contribution

    # Outflow calculation
    environmental_release = 0
    if current_level > base_capacity * 0.9:
        environmental_release = 800

    outflow = scheduled_supply + base_leakage + environmental_release + total_evaporation_loss

    # Key computation step
    net_flow = inflow - outflow

    # Post-analysis (distractor computations)
    utilization_ratio = current_level / base_capacity
    peak_demand_met = (min_outflow_rate * 1.5) < max_inflow_rate
    contingency_plan_needed = (net_flow < 0) and (utilization_ratio > 0.8)

    # Irrelevant set operations to meet language-specific requirements
    hours_with_rain = {i for i, rain in enumerate(hourly_rainfall) if rain > 0}
    high_temp_hours = {i for i, temp in enumerate(temperature_celsius) if temp >= 25}
    critical_hours = hours_with_rain & high_temp_hours  # overlap analysis (unused)

    # Slicing operation on temperature data (semi-relevant)
    afternoon_temps = temperature_celsius[12:18]
    avg_afternoon_temp = sum(afternoon_temps) / len(afternoon_temps)

    # Final reporting
    print(f"Result: {net_flow}")

analyze_water_reservoir()