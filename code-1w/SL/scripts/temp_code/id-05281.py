def preprocess_sensor_readings(readings):
    cleaned = []
    for val in readings:
        if isinstance(val, str):
            val = val.strip().lower()
            if val.isdigit():
                cleaned.append(int(val))
        elif isinstance(val, (int, float)) and val > 0:
            cleaned.append(int(val))
    return sorted(cleaned, reverse=True)

# Simulate soil nutrient index based on historical data
def compute_nutrient_baseline(samples):
    nutrient_levels = {}
    for key, values in samples.items():
        if 'nitrogen' in key:
            nutrient_levels[key] = sum(v * 0.8 for v in values if v > 0)
        elif 'phosphorus' in key:
            nutrient_levels[key] = sum(v * 0.6 for v in values if v < 10)
        else:
            nutrient_levels[key] = len(values)
    return nutrient_levels

# Core function with mixed reasoning
def calculate_harvest_efficiency(climate, crops):
    temp_avg = sum(climate['temps']) / len(climate['temps'])
    rainfall_total = sum(climate['rainfall'])
    humidity_mode = max(set(climate['humidity']), key=climate['humidity'].count)
    
    # Distractor: wind patterns not used in final calculation
    wind_data = climate.get('wind_speed', [])
    avg_wind = sum(wind_data) / len(wind_data) if wind_data else 0
    wind_categories = {w: 'calm' if w < 5 else 'moderate' for w in wind_data}
    
    # Relevant processing
    viable_zones = 0
    total_yield = 0
    crop_bonuses = {'wheat': 1.2, 'corn': 1.5, 'barley': 1.1}
    
    for row in crops:
        for plot in row:
            if not plot or not plot['active']:
                continue
            base_yield = plot['size'] * 10
            crop_type = plot['crop']
            
            # Conditional yield adjustment
            bonus = crop_bonuses.get(crop_type, 1.0)
            if temp_avg > 25 and crop_type == 'wheat':
                bonus *= 0.7
            elif humidity_mode < 60:
                bonus *= 0.9
            
            adjusted_yield = base_yield * bonus
            
            # Threshold filter
            if adjusted_yield > 100:
                total_yield += adjusted_yield
                viable_zones += 1
    
    # Final efficiency score
    efficiency_factor = 0.8 if rainfall_total > 200 else 0.6
    final_yield = int((total_yield * efficiency_factor) / (viable_zones if viable_zones else 1))
    
    # Dead code path - misleading computation
    if avg_wind > 10:
        final_yield -= 50  # never reached due to data
    
    return final_yield

# Sensor input simulation (mixed types)
sensor_input = [' 42 ', '38', 'invalid', 45.6, -5, '50', 'no_data', 41]
calibrated = preprocess_sensor_readings(sensor_input)

# Nutrient data setup (semi-relevant structure)
nutrient_samples = {
    'nitrogen_a': [8, 7, 9],
    'phosphorus_b': [4, 12, 6],
    'potassium_c': [3, 5]
}
baseline_nutrients = compute_nutrient_baseline(nutrient_samples)

# Climate input data
climate_data = {
    'temps': [22, 25, 27, 24, 26],
    'rainfall': [45, 60, 55, 40],
    'humidity': [65, 70, 65, 50, 80],
    'wind_speed': [3, 4, 2]  # unused beyond avg
}

crop_map = [
    [{'crop': 'wheat', 'size': 12, 'active': True}, {'crop': 'corn', 'size': 8, 'active': True}],
    [{'crop': 'barley', 'size': 15, 'active': True}, {'crop': 'wheat', 'size': 5, 'active': False}],
    [{'crop': 'corn', 'size': 10, 'active': True}, {'crop': 'wheat', 'size': 14, 'active': True}]
]

# Execution point of interest
final_yield = calculate_harvest_efficiency(climate_data, crop_map)
print(f"Result: {final_yield}")