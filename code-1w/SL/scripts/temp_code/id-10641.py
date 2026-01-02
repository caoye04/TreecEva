def analyze_growth_factors(conditions):
    # Irrelevant processing: analyzing light cycles (not used in final result)
    photoperiod = sum([c.get('light', 0) for c in conditions])
    temperature_stress = 0
    for c in conditions:
        if c['temp'] > 35 or c['temp'] < 10:
            temperature_stress += 1

    # Distractor computation: water efficiency ratio (not used)
    total_water = sum([c['water'] for c in conditions])
    efficiency_ratio = total_water / (len(conditions) + 1e-5)

    # Relevant transformation: normalize humidity values
    humidity_scores = [min(max((h['humidity'] - 40) / 20, 0), 1) for h in conditions]
    return humidity_scores


def calculate_harvest_potential(climate, soil):
    # Step 1: Extract base fertility from soil composition
    base_fertility = sum(soil['nutrients'].values()) * 0.8

    # Step 2: Process climate data through multiple filters
    processed_climate = analyze_growth_factors(climate)
    climate_score = sum(processed_climate) * 2.5

    # Step 3: Apply seasonal adjustment factor
    season_weights = {'spring': 1.2, 'summer': 1.0, 'fall': 0.8, 'winter': 0.3}
    current_season = 'summer'
    adjusted_yield = base_fertility * climate_score * season_weights[current_season]

    # Step 4: Simulate pest impact (but only if extreme temp occurred – not triggered)
    pest_factor = 1.0
    for entry in climate:
        if entry['temp'] > 40:
            pest_factor *= 0.9
    adjusted_yield *= pest_factor

    # Step 5: Apply field age depreciation (distractor: complex but unused)
    field_installation_year = 2018
    depreciation_rate = 0.03
    years_active = 2023 - field_installation_year
    residual_value = 1 - (depreciation_rate * years_active)

    # Step 6: Final adjustment based on historical averages (semi-relevant)
    historical_avg = [420, 435, 410, 450]
    trend_correction = sum(historical_avg) / len(historical_avg) / 400

    # Step 7: Compute final yield (this is the key line)
    final_yield = int(adjusted_yield * trend_correction)

    # Dead code path: logging unused diagnostics
    if False:
        print(f'Diagnostics: {locals()}')

    return final_yield

# Main execution context
soil_quality = {
    'ph': 6.5,
    'texture': 'loam',
    'nutrients': {
        'nitrogen': 120,
        'phosphorus': 45,
        'potassium': 180,
        'magnesium': 30
    }
}

device_id = "AGRI-SENSOR-7X"
calibration_offset = 0.021

climate_data = [
    {'temp': 22, 'humidity': 60, 'light': 8, 'water': 25},
    {'temp': 25, 'humidity': 55, 'light': 9, 'water': 28},
    {'temp': 27, 'humidity': 50, 'light': 8, 'water': 26},
    {'temp': 24, 'humidity': 65, 'light': 7, 'water': 27},
    {'temp': 26, 'humidity': 58, 'light': 9, 'water': 29}
]

# String manipulation distractor (no effect on result)
data_tag = f"{device_id.lower().replace('-', '_')}_q{calibration_offset:.3f}".upper()
diagnostic_log = [f"Sample_{i}: {tag}" for i, tag in enumerate(data_tag.split('_')) if 'Q' in tag]

# Key execution point
final_yield = calculate_harvest_potential(climate_data, soil_quality)
print(f"Result: {final_yield}")