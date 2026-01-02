def calculate_harvest_potential(climate_data):
    base_yield = 150
    temp_factor = 0.0
    rain_factor = 0.0
    sunlight_factor = 0.0

    # Irrelevant transformation: case conversion for non-impactful metadata
    location_name = climate_data['region'].upper()
    season_tag = climate_data['season'].lower()

    temperature = climate_data['avg_temp']
    rainfall = climate_data['total_rainfall']
    sunlight_hours = climate_data['sunlight_hours']
    elevation = climate_data['elevation']  # Unused distractor
    humidity = climate_data['humidity']    # Semi-relevant but not used in final calc

    # Dummy dictionary for alternate scenario (dead code path)
    alternate_factors = {
        'coastal': {'temp_mod': 0.8, 'rain_mod': 1.3},
        'mountain': {'temp_mod': 0.6, 'rain_mod': 0.9}
    }

    # Actual yield logic begins
    if temperature > 25:
        temp_factor = 0.7
    elif temperature > 20:
        temp_factor = 0.9
    else:
        temp_factor = 0.5

    if rainfall < 80:
        rain_factor = 0.6
    elif rainfall < 120:
        rain_factor = 1.0
    else:
        rain_factor = 0.8

    # Sunlight impact
    if sunlight_hours > 10:
        sunlight_factor = 1.1
    elif sunlight_hours > 7:
        sunlight_factor = 0.95
    else:
        sunlight_factor = 0.7

    # Accumulate irrelevant stats (distractor computation)
    total_diurnal_shift = 0
    for hour in range(1, 25):
        total_diurnal_shift += hour % 3  # Meaningless sum

    # Core calculation (dependent on three factors)
    adjusted_yield = base_yield * temp_factor
    adjusted_yield *= rain_factor
    adjusted_yield *= sunlight_factor

    # Final adjustment based on region-specific empirical data (dictionary lookup)
    empirical_boost = {
        'tropical': 1.15,
        'temperate': 1.05,
        'arid': 0.95
    }
    region = climate_data['region']
    if region in empirical_boost:
        adjusted_yield *= empirical_boost[region]

    # Spurious loop with no effect (adds interference)
    convergence_test = 1.0
    for i in range(5):
        convergence_test *= 0.99  # Simulates decay, unused

    final_yield = int(round(adjusted_yield))

    return final_yield

# Input data
climate_data = {
    'region': 'temperate',
    'season': 'Summer',
    'avg_temp': 22,
    'total_rainfall': 110,
    'sunlight_hours': 8,
    'elevation': 150,
    'humidity': 68
}

# Execution point
final_yield = calculate_harvest_potential(climate_data)
print(f"Result: {final_yield}")