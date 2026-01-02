def analyze_growth_potential(soil_nutrients, temperature):
    # Irrelevant analysis with decoy logic
    base_index = 0
    for nutrient in soil_nutrients:
        if nutrient > 50:
            base_index += 1
    adjusted_temp = temperature if temperature > 20 else 20
    return base_index * adjusted_temp // 3

# Unused function - red herring
def estimate_pest_risk(plant_density, humidity):
    risk_score = 0
    for i in range(len(plant_density)):
        risk_score += plant_density[i] * (humidity / 100)
    return int(risk_score % 7)

# Distractor variables
tank_capacity = 5000
irrigation_cycles = [3, 7, 2, 8]
efficiency_logs = [0.88, 0.91, 0.85, 0.93]

# Simulated sensor offsets (unused)
sensor_offset_x = 0.023
sensor_offset_y = -0.041

# Real input data
field_data = {
    'plots': [101, 102, 105, 106],
    'crop_type': 'maize',
    'soil_ph': [6.2, 6.4, 6.3, 6.5],
    'moisture': [35, 40, 38, 42]
}

weather_conditions = {
    'temperature_avg': 25,
    'sunlight_hours': 12,
    'rainfall_mm': 85
}

# Decoy transformation chain
transformed_data = []
for p in field_data['plots']:
    transformed = (p * 1.5) + 2
    transformed_data.append(int(transformed))

# Dummy accumulation with no effect on result
total_diagnostics = 0
for i in range(4):
    total_diagnostics += len(str(transformed_data[i]))

# Core calculation function
def calculate_harvest_efficiency(fields, weather):
    base_efficiency = 0
    plot_count = len(fields['plots'])
    
    # Summation and conditional scaling
    ph_sum = sum(fields['soil_ph'])
    avg_ph = ph_sum / plot_count
    
    # Conditional expression used meaningfully
    temp_factor = 1.2 if weather['temperature_avg'] >= 24 else 0.9
    light_factor = weather['sunlight_hours'] / 10
    
    # Bit manipulation as distraction (not affecting final result)
    masked_value = plot_count ^ 0b1101 & 0b1010
    shift_probe = (masked_value << 2) >> 1
    
    # Accumulation with combinatorics-like adjustment
    moisture_boost = 0
    for m in fields['moisture']:
        if m > 37:
            moisture_boost += 0.05
    
    # Main formula
    raw_yield = (avg_ph * 10) * temp_factor * light_factor
    
    # Integer division and rounding
    base_efficiency = int(raw_yield + 0.5)  # Round to nearest int
    
    # Secondary adjustment based on rainfall
    if weather['rainfall_mm'] < 100:
        deficit = (100 - weather['rainfall_mm']) / 100
        base_efficiency = base_efficiency * (1 - deficit)
    else:
        surplus = (weather['rainfall_mm'] - 100) / 200
        base_efficiency = base_efficiency * (1 - surplus)
    
    # Final adjustment via conditional expression
    final_adjustment = moisture_boost if moisture_boost > 0.1 else 0.08
    
    # The actual answer computation
    final_yield = int(base_efficiency + final_adjustment * 100)
    
    # Dead code path - never executed
    if False:
        backup_model = analyze_growth_potential([60, 70, 55], 25)
        final_yield = backup_model
        
    return final_yield

# Execution point of interest
final_yield = calculate_harvest_efficiency(field_data, weather_conditions)

# Output result as required
print(f"Target result: {final_yield}")