def analyze_growth_factors(conditions):
    growth_index = 0
    stress_factor = 0
    for condition in conditions:
        if condition['temp'] > 30:
            stress_factor += 0.1
        elif condition['temp'] < 15:
            stress_factor += 0.2
        humidity_ratio = condition['humidity'] / 100.0
        growth_index += (condition['light'] * humidity_ratio) - stress_factor
    return growth_index

soil_profiles = [
    {'type': 'clay', 'ph': 6.2, 'nutrients': 3.4},
    {'type': 'loam', 'ph': 6.8, 'nutrients': 4.1},
    {'type': 'sand', 'ph': 5.9, 'nutrients': 2.7}
]

current_stats = {
    'readings': 0,
    'total_rainfall': 0,
    'peak_light': 0
}

climate_data = [
    {'temp': 25, 'humidity': 65, 'light': 800, 'rainfall': 12},
    {'temp': 28, 'humidity': 70, 'light': 850, 'rainfall': 8},
    {'temp': 23, 'humidity': 60, 'light': 700, 'rainfall': 15},
    {'temp': 32, 'humidity': 55, 'light': 900, 'rainfall': 5}
]

# Irrelevant tracking variables
observation_log = []
diagnostic_mode = False
system_health = {'status': 'nominal', 'checks': 0}

for entry in climate_data:
    current_stats['readings'] += 1
    current_stats['total_rainfall'] += entry['rainfall']
    if entry['light'] > current_stats['peak_light']:
        current_stats['peak_light'] = entry['light']
    observation_log.append(f"Log-{current_stats['readings']}: Active")

    # Dead code path (never executed unless diagnostic_mode=True)
    if diagnostic_mode and entry['temp'] > 30:
        system_health['status'] = 'overheat_risk'
        system_health['checks'] += 1

base_yield = 0
for profile in soil_profiles:
    if profile['ph'] >= 6.0 and profile['ph'] <= 7.0:
        base_yield += profile['nutrients'] * 10

# Simulate nutrient depletion over time (irrelevant to final computation)
temporal_decay = 0
for i in range(3):
    temporal_decay += 0.05 * (i + 1)

adjusted_base = base_yield - (temporal_decay * 10)  # Minor adjustment, not used later

# Core calculation uses dictionary aggregation and filtering
suitable_soils = [p for p in soil_profiles if p['type'] in ['loam', 'silt']]
nutrient_sum = sum(p['nutrients'] for p in suitable_soils)
pH_avg = sum(p['ph'] for p in suitable_soils) / len(suitable_soils) if suitable_soils else 6.5

# Secondary irrelevant computation: environmental stress score
stress_scores = []
for data in climate_data:
    score = 0
    if data['temp'] > 30: score += 2
    if data['humidity'] < 50: score += 1
    if data['light'] > 850: score += 1
    stress_scores.append(score)

avg_stress = sum(stress_scores) / len(stress_scores) if stress_scores else 0

# Main yield calculation function
def calculate_harvest_potential(weather, soils):
    total_yield = 0
    growth_multiplier = analyze_growth_factors(weather) / 100.0
    
    # Use of dictionary keys and conditional weighting
    for soil in soils:
        key = soil['type']
        if key == 'loam':
            total_yield += soil['nutrients'] * 12 * growth_multiplier
        elif key == 'clay':
            total_yield += soil['nutrients'] * 8 * growth_multiplier
        elif key == 'sand':
            total_yield += soil['nutrients'] * 6 * growth_multiplier
    
    # Apply pH sensitivity
    for data in weather:
        if data['temp'] > 30:
            total_yield *= 0.9  # Heat penalty
    
    return int(total_yield)

final_yield = calculate_harvest_potential(climate_data, soil_profiles)
print(f"Target result: {final_yield}")