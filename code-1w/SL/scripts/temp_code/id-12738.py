def calculate_energy_output(solar_panels, wind_turbines):
    base_solar = 150
    base_wind = 200
    efficiency_factor = 0.85

    solar_contribution = [base_solar * hours * efficiency_factor for hours in solar_panels]
    wind_contribution = [base_wind * speed * efficiency_factor for speed in wind_turbines]
    
    # Combine outputs where both sources exceed minimum threshold
    combined_output = []
    for i in range(min(len(solar_contribution), len(wind_contribution))):
        if solar_contribution[i] > 100 and wind_contribution[i] > 150:
            combined_output.append(solar_contribution[i] + wind_contribution[i])
    
    fallback_output = [x * 0.9 for x in solar_contribution if x <= 100]
    optimized_output = combined_output + fallback_output
    
    energy_capacity = sum(optimized_output)
    return energy_capacity

# Simulate input data
solar_hours = [6, 4, 8, 3]
wind_speeds = [3.5, 2.0, 4.2, 1.8]

result = calculate_energy_output(solar_hours, wind_speeds)
print(f"Target result: {result}")