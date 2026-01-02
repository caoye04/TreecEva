def analyze_growth_potential(temperature, moisture):
    # Irrelevant intermediate calculation (distractor)
    base_index = temperature * 0.8 + moisture * 1.2
    stress_factor = 0 if temperature < 35 and moisture > 40 else 0.3
    return base_index - stress_factor

# Misleading auxiliary function that is never called
def calculate_fertilizer_need(nutrients):
    required = 0
    for level in nutrients:
        if level < 20:
            required += (20 - level) * 1.5
    return required  # Dead code path

# Simulate sensor calibration (irrelevant preprocessing)
sensor_offsets = [0.1, -0.2, 0.15]
adjusted_readings = []
for i in range(3):
    adjusted_readings.append(round(25 + i*3 + sensor_offsets[i], 2))

# Core data
climate_data = [28, 32, 25, 38]  # Temperature readings in Celsius
soil_conditions = [45, 37, 50, 30]   # Moisture percentages
nutrient_levels = [18, 22, 15, 25]  # Nitrogen content (unused)

# Tracking variables for non-critical metrics
consistency_score = 0
fluctuation_count = 0
for i in range(len(climate_data) - 1):
    if abs(climate_data[i+1] - climate_data[i]) > 5:
        fluctuation_count += 1
consistency_score = len(climate_data) - fluctuation_count

# Conditional expression used for state classification
climate_states = ['optimal' if temp < 35 and moist > 40 else 'stress' 
                   for temp, moist in zip(climate_data, soil_conditions)]

# Primary logic with nested conditions and list processing
def optimize_harvest(temps, moisture_levels):
    yield_estimate = 0
    adjustment_factor = 1.0
    
    for i in range(len(temps)):
        # Intermediate irrelevant computation
        daily_analysis = analyze_growth_potential(temps[i], moisture_levels[i])
        
        if temps[i] > 35:
            adjustment_factor = 0.8
        elif moisture_levels[i] < 35:
            adjustment_factor = 0.9
        else:
            adjustment_factor = 1.1
        
        # Actual yield contribution logic
        base_yield = temps[i] * 0.5 + moisture_levels[i] * 0.7
        
        # Apply conditional bonus using inline expression
        bonus = 5 if moisture_levels[i] > 45 and temps[i] < 30 else 0
        yield_estimate += base_yield * adjustment_factor + bonus
    
    # Final nonlinear correction (critical step)
    if 'stress' not in climate_states:
        yield_estimate *= 1.05
    
    return int(yield_estimate)

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_conditions)

# Output result as required
print(f"Result: {final_yield}")