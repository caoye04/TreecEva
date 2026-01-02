def calculate_grid_stability(solar_output, wind_output, base_load):
    # Simulate renewable energy generation (in MW)
    solar_capacity_factor = 0.85
    wind_capacity_factor = 0.67
    
    adjusted_solar = solar_output * solar_capacity_factor
    adjusted_wind = wind_output * wind_capacity_factor

    # Total energy generation from renewables
    total_generation = adjusted_solar + adjusted_wind

    # Unrelated diagnostic variable (minor distraction)
    system_uptime_hours = 987.2

    # Energy demand calculation across sectors
    residential_demand = base_load * 0.45
    commercial_demand = base_load * 0.35
    industrial_demand = base_load * 0.20
    total_demand = residential_demand + commercial_demand + industrial_demand

    # Key computation point
    net_energy_balance = total_generation - total_demand

    # Diagnostic flag (irrelevant to result)
    status_code = 'OK' if net_energy_balance > 0 else 'DEFICIT'

    return net_energy_balance

# Main execution
energy_result = calculate_grid_stability(solar_output=1200, wind_output=950, base_load=1500)
Result: {energy_result}