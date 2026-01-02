def calculate_harvest_potential(climate_data):
    base_temperature = 20.0
    optimal_rainfall = 100.0
    stress_factor = 0.0
    cumulative_score = 0.0
    harvest_modifier = 1.0
    
    # Extract and preprocess climate metrics
    temp_series = [entry['temp'] for entry in climate_data if entry['season'] == 'summer']
    rainfall_series = [entry['rain'] for entry in climate_data]
    wind_data = [entry['wind'] for entry in climate_data]
    
    # Compute average temperature during growing season
    avg_temp = sum(temp_series) / len(temp_series) if temp_series else 0
    temp_deviation = abs(avg_temp - base_temperature)
    
    # Calculate moisture adequacy index
    total_rainfall = sum(rainfall_series)
    moisture_ratio = total_rainfall / optimal_rainfall
    
    # Assess drought stress (irrelevant if rainfall is sufficient)
    dry_days = 0
    for entry in climate_data:
        if entry['rain'] < 5 and entry['temp'] > 25:
            dry_days += 1
    prolonged_dry_stretch = dry_days > 10
    if prolonged_dry_stretch:
        stress_factor += 0.15

    # Wind impact analysis (semi-relevant, capped influence)
    max_gust = max(wind_data) if wind_data else 0
    if max_gust > 40:
        harvest_modifier *= 0.9
    
    # Temperature suitability scoring
    if temp_deviation < 2:
        cumulative_score += 40
    elif temp_deviation < 5:
        cumulative_score += 30
    else:
        cumulative_score += 15
    
    # Rainfall efficiency calculation
    if 0.8 <= moisture_ratio <= 1.2:
        cumulative_score += 50
    elif moisture_ratio > 1.5:
        cumulative_score += 20  # Excess water penalty
    else:
        cumulative_score += 35
    
    # Phantom computation: unrelated to final result
    phantom_cycle = 0
    for i in range(len(rainfall_series)):
        phantom_cycle += (i * rainfall_series[i]) % 7
    normalized_phantom = phantom_cycle / (len(rainfall_series) + 1e-5)
    
    # Final yield potential determined by combined score
    baseline_yield = 5000
    adjusted_yield = baseline_yield * (cumulative_score / 100)
    final_yield = int(adjusted_yield * harvest_modifier)
    
    # Unused string processing to increase cognitive load
    summary_log = f"Harvest assessment complete. Max gust: {max_gust} km/h"
    log_tokens = summary_log.split(' ')
    token_count = len([t for t in log_tokens if len(t) > 3])
    
    return final_yield

# Simulated climate dataset for growing season
climate_input = [
    {'season': 'spring', 'temp': 18, 'rain': 85, 'wind': 22},
    {'season': 'summer', 'temp': 23, 'rain': 95, 'wind': 18},
    {'season': 'summer', 'temp': 21, 'rain': 105, 'wind': 20},
    {'season': 'summer', 'temp': 25, 'rain': 40, 'wind': 25},
    {'season': 'autumn', 'temp': 16, 'rain': 120, 'wind': 30},
    {'season': 'summer', 'temp': 19, 'rain': 110, 'wind': 15},
    {'season': 'spring', 'temp': 17, 'rain': 90, 'wind': 24}
]

final_yield = calculate_harvest_potential(climate_input)
print(f"Result: {final_yield}")