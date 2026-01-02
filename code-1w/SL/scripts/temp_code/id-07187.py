def calculate_harvest_potential(climate_data):
    base_temperature = 25
    water_retention = 0.85
    nutrient_factor = 1.1
    
    # Irrelevant atmospheric metrics (distractor)
    ozone_level = 320
    uv_index = 7
    wind_speed_kmh = 14
    
    # Process daily temperature fluctuations
    temp_amplitude = climate_data['max_temp'] - climate_data['min_temp']
    effective_temp = (climate_data['max_temp'] + climate_data['min_temp']) / 2
    
    # Misleading environmental adjustment (not used in final calc)
    false_adjustment = (ozone_level / uv_index) * 0.01 if uv_index > 5 else 0
    
    # Core yield factors
    thermal_efficiency = max(0, 1 - abs(effective_temp - base_temperature) / 15)
    hydration_score = min(1, climate_data['rainfall_mm'] / 120)
    
    # Destructuring assignment (tuple unpacking)
    (sun_hours, cloud_cover) = (climate_data['sunlight'], climate_data['cloud_cover'])
    
    # Conditional expression for sunlight utilization
    photosynthesis_rate = 0.9 if sun_hours > 6 else 0.6
    
    # Complex interaction of factors with irrelevant intermediate
    dummy_buffer = [0] * 3
    dummy_buffer[1] = wind_speed_kmh * 0.05  # Dead computation
    
    # Nested logic determining final yield
    if thermal_efficiency > 0.7:
        if hydration_score > 0.5:
            base_yield = 8.2
        else:
            base_yield = 5.4
    else:
        base_yield = 3.1
    
    # Final calculation with nutrient and water retention
    adjusted_yield = base_yield * nutrient_factor * hydration_score * photosynthesis_rate * water_retention
    
    # Secondary distractor: unused growth index
    potential_growth_index = (effective_temp / 20) * (climate_data['rainfall_mm'] / 100)
    stress_factor = 1 if temp_amplitude < 10 else 0.85
    
    # Final yield computed but not yet returned
    final_yield = round(adjusted_yield * stress_factor, 4)
    
    return final_yield

# Input data
climate_data = {
    'max_temp': 31,
    'min_temp': 19,
    'rainfall_mm': 95,
    'sunlight': 7.2,
    'cloud_cover': 30
}

# Execution point
final_yield = calculate_harvest_potential(climate_data)
print(f"Result: {final_yield}")