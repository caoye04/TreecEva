def calculate_agricultural_output(temperature_data, rainfall_data):
    base_yield = 120
    stress_threshold = 35
    optimal_rainfall = 100
    
    # Irrelevant environmental metrics (distractors)
    wind_speed_avg = 14.2
    soil_ph = 6.8
    elevation_m = 220
    uv_index = 8
    
    # Simulate crop stress from temperature
    heat_stress_days = 0
    for temp in temperature_data:
        if temp > stress_threshold:
            heat_stress_days += 1
    
    # Compute temperature adjustment factor
    temp_penalty = 0.02 * heat_stress_days
    
    # Rainfall efficiency with conditional expression
    total_rainfall = sum(rainfall_data)
    rain_efficiency = 1.0 if abs(total_rainfall - optimal_rainfall) < 20 else 0.7

    # Dummy loop to track irrelevant drought cycles (dead computation)
    drought_cycles = 0
    wet_days = 0
    for r in rainfall_data:
        if r < 5:
            drought_cycles += 1
        elif r > 15:
            wet_days += 1  # Not used later
    
    # Primary productivity calculation
    crop_health = base_yield * (1 - temp_penalty) * rain_efficiency
    
    # Resilience factor based on data consistency using enumerate and zip
    variation_score = 0
    for i, (t, r) in enumerate(zip(temperature_data, rainfall_data)):
        variation_score += abs(t - temperature_data[0]) * (i + 1) % 3
    
    resilience_factor = 1.0 - (variation_score / 100.0)
    
    # Final yield computation (key statement)
    final_yield = crop_productivity * resilience_factor
    
    # Unused intermediate stats (distractor variables)
    avg_temp = sum(temperature_data) / len(temperature_data)
    peak_rainfall = max(rainfall_data)
    growing_days = len(rainfall_data)
    
    return final_yield

# Input data
temps = [30, 32, 36, 38, 33]
rains = [95, 110, 80, 120, 90]

crop_productivity = 100  # Set after function definition (semi-misleading order)

result = calculate_agricultural_output(temps, rains)
print(f"Result: {result}")