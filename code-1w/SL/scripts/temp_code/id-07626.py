def analyze_growth_potential(temperature, rainfall):
    # Irrelevant helper function (dead code path)
    base_index = temperature * 0.7 + rainfall * 0.3
    adjusted = base_index * (1.2 if temperature > 25 else 0.9)
    return adjusted

# Distractor variables
temperature_log = [22, 25, 27, 24, 20]
rainfall_record = [80, 105, 90, 70, 60]
phantom_coefficient = 0.87
theoretical_yield = 0

# Simulated sensor calibration (irrelevant computation)
sensor_offset = 0.05
raw_readings = [100, 102, 98, 105]
adjusted_readings = [r * (1 + sensor_offset) for r in raw_readings]
avg_reading = sum(adjusted_readings) / len(adjusted_readings)

# Core data structures
climate_data = {
    'temp_avg': 24.5,
    'rain_mm': 85,
    'sunlight_hours': 7.2,
    'extreme_events': 2
}

soil_health = {
    'ph': 6.8,
    'nitrogen': 45,
    'moisture': 32,
    'compaction': 18
}

# Misleading intermediate calculation (not used in final result)
optimal_ph_range = (6.0, 7.5)
is_ph_balanced = optimal_ph_range[0] <= soil_health['ph'] <= optimal_ph_range[1]
theoretical_multiplier = 1.1 if is_ph_balanced else 0.8

# Unused transformation pipeline
def transform_nutrient_levels(data):
    levels = []
    for key, val in data.items():
        if 'nitrogen' in key.lower():
            levels.append(val * 1.15)
        elif 'ph' in key.lower():
            levels.append(val * 1.05)
    return levels

# Decoy algorithm with red herring logic
def predict_growth_score(temp, nitrogen_level):
    score = 0
    if temp > 20:
        score += 50
    if nitrogen_level > 40:
        score += 30
    humidity_factor = 1.2
    score *= humidity_factor
    return score  # Never called

# Conditional expression and core logic intertwined with noise
def calculate_harvest_efficiency(climate, soil):
    temp_factor = 0.8 if climate['temp_avg'] < 22 else (1.05 if climate['temp_avg'] <= 26 else 0.95)
    rain_factor = 1.1 if 70 <= climate['rain_mm'] <= 100 else 0.85
    
    # Critical nested logic with distractors
    if soil['nitrogen'] > 40:
        if soil['moisture'] > 30:
            nitrogen_efficiency = 1.2
            # Unused branch creating confusion
            if soil['compaction'] < 20:
                nitrogen_efficiency *= 1.05
        else:
            nitrogen_efficiency = 0.8
    else:
        nitrogen_efficiency = 0.6
    
    sunlight_factor = climate['sunlight_hours'] / 8.0
    
    # Complex composite formula (actual answer path)
    base_efficiency = temp_factor * rain_factor * sunlight_factor * nitrogen_efficiency
    
    # Red herring adjustment (looks important but unused)
    event_penalty = 0.9 if climate['extreme_events'] > 0 else 1.0
    hypothetical_loss = base_efficiency * (1 - event_penalty)
    
    # Final determination using conditional expression
    final_efficiency = base_efficiency if base_efficiency > 0.8 else base_efficiency * 0.92
    
    # Key assignment point
    final_yield = int(950 * final_efficiency)
    
    return final_yield

# Execution trace
interim_check = analyze_growth_potential(climate_data['temp_avg'], climate_data['rain_mm'])

# Target execution point
final_yield = calculate_harvest_efficiency(climate_data, soil_health)

# Output result
print(f"Result: {final_yield}")