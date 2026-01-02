def calculate_harvest_potential(climate_data):
    base_yield = 100
    temperature_factor = 0.0
    precipitation_factor = 0.0
    sunlight_accumulator = 0
    stress_index = 0
    yield_adjustment = 0
    
    # Irrelevant tracking variables (distractors)
    day_count = len(climate_data['temperatures'])
    avg_temp = sum(climate_data['temperatures']) / day_count
    total_rainfall = sum(climate_data['precipitation'])
    peak_sunlight = max(climate_data['sunlight'])
    
    # Semi-relevant preprocessing (modular arithmetic for seasonal cycles)
    adjusted_days = [(i % 7) + 1 for i in range(day_count)]
    weekly_cycle_mod = day_count % 7
    
    # Real computation: temperature factor
    for temp in climate_data['temperatures']:
        if 20 <= temp <= 30:
            temperature_factor += 1.2
        elif temp < 10 or temp > 40:
            temperature_factor -= 0.5
        else:
            temperature_factor += 0.8
    
    # Real computation: precipitation factor with accumulation
    cumulative_rain = 0
    for rain in climate_data['precipitation']:
        cumulative_rain += rain
        if rain > 15:
            stress_index += 1
        elif rain < 2:
            stress_index += 0.5
    
    precipitation_factor = max(0.5, min(1.5, (cumulative_rain / day_count) * 0.1))
    
    # Sunlight accumulator (partially relevant, but only total matters)
    for sun_hours in climate_data['sunlight']:
        if sun_hours > 8:
            sunlight_accumulator += 8 + (sun_hours - 8) * 0.3
        else:
            sunlight_accumulator += sun_hours
    
    # Actual yield adjustment logic
    yield_adjustment = (temperature_factor / day_count) * precipitation_factor
    
    # Distractor: unused dictionary operations
    metadata = {
        'version': '2.1',
        'region': 'N45W120',
        'last_updated': '2023-10-05'
    }
    metadata['processed_days'] = day_count
    metadata['yield_version'] = 'A'
    metadata.pop('last_updated')  # Red herring operation
    
    # Final calculation (key statement)
    final_yield = base_yield * yield_adjustment
    
    # Print result as required
    print(f"Result: {final_yield}")
    return final_yield

# Input data
climate_input = {
    'temperatures': [25, 28, 32, 21, 18, 35, 29, 24],
    'precipitation': [12, 3, 18, 1, 5, 22, 4, 8],
    'sunlight': [9, 6, 10, 5, 7, 11, 6, 8]
}

# Execute
final_yield = calculate_harvest_potential(climate_input)