def calculate_harvest_potential(climate_data):
    base_yield = 0
    temperature_factor = 1.0
    rainfall_factor = 1.0
    sunlight_factor = 1.0
    stress_index = 0
    cumulative_rainfall = 0
    
    # Extract relevant metrics
    avg_temp = climate_data['temperature']
    total_rain = climate_data['rainfall']
    daylight_hours = climate_data['sunlight']
    wind_speed = climate_data['wind']  # Irrelevant distractor
    humidity = climate_data['humidity']  # Not used in final calculation

    # Process temperature effects
    if 20 <= avg_temp <= 28:
        temperature_factor = 1.2
    elif avg_temp < 20:
        temperature_factor = 0.8 + (avg_temp - 10) * 0.04
    else:
        temperature_factor = 1.0 - (avg_temp - 28) * 0.03

    # Rainfall processing with intermediate tracking
    if total_rain < 50:
        rainfall_factor = 0.6
    elif total_rain > 150:
        excess_water = total_rain - 150
        cumulative_rainfall += excess_water  # Semi-relevant but not critical
        rainfall_factor = 0.7
    else:
        rainfall_factor = 1.1

    # Sunlight analysis
    ideal_sunlight = 8
    if daylight_hours < 4:
        sunlight_factor = 0.5
    elif daylight_hours > 12:
        sunlight_factor = 0.8
    else:
        sunlight_factor = 0.9 + (min(daylight_hours, 10) - 6) * 0.1

    # Secondary computations (distractors)
    evaporation_rate = 0.02 * total_rain * (avg_temp / 25)  # Unused
    microclimate_score = (temperature_factor + rainfall_factor) / 2  # Dead computation

    # Core yield formula
    base_yield = 500 * temperature_factor * rainfall_factor * sunlight_factor
    
    # Final adjustment based on string-encoded condition
    alert_status = climate_data['alert']
    if alert_status.upper().strip() == 'CRITICAL':
        base_yield *= 0.7
    elif alert_status.lower().find('warning') != -1:
        base_yield *= 0.85

    # Additional irrelevant transformation
    formatted_yield = f"Yield:{base_yield:.1f}kg"  # String distractor
    yield_parts = formatted_yield.split(':')
    
    # Final assignment
    final_yield = int(round(base_yield))
    return final_yield

# Main execution
climate_data = {
    'temperature': 26,
    'rainfall': 120,
    'sunlight': 9,
    'wind': 15,
    'humidity': 60,
    'alert': 'normal'
}

result_tracker = []
result_tracker.append('start')
final_yield = calculate_harvest_potential(climate_data)
result_tracker.append('complete')

print(f"Result: {final_yield}")