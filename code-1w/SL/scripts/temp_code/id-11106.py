def analyze_growth_potential(temperature, rainfall):
    # Irrelevant helper function with misleading calculations
    base_rate = 0.5
    stress_factor = 1.0
    if temperature > 35:
        stress_factor *= 0.7
    if rainfall < 200:
        stress_factor *= 0.8
    return base_rate * stress_factor  # Not used in final result

# Distractor data arrays
temp_records = [22, 25, 37, 19, 41]
rain_records = [180, 210, 150, 300, 90]

# Unused transformation
historical_yields = [analyze_growth_potential(t, r) for t, r in zip(temp_records, rain_records)]

soil_composition = {
    'ph': 6.8,
    'nitrogen': 140,
    'organic_matter': 3.2,
    'compaction': 2.1  # Higher is worse
}

# Misleading intermediate metric
theoretical_capacity = (soil_composition['nitrogen'] * soil_composition['organic_matter']) / 100

climate_data = {
    'avg_temp': 24.5,
    'total_rainfall': 520,
    'sunlight_hours': 6.8,
    'frost_days': 3
}

soil_quality = {
    'ph_level': 6.8,
    'nutrient_score': 87,
    'moisture_retention': 4.3,
    'toxicity_index': 0.15
}

# Complex but irrelevant scoring matrix
def calculate_ecoscore(data):
    score = 0
    score += min(data['avg_temp'] * 0.8, 30)
    score += min(data['total_rainfall'] / 15, 25)
    score += data['sunlight_hours'] * 2.5
    if data['frost_days'] == 0:
        score += 10
    elif data['frost_days'] <= 5:
        score += 5
    return score

# Dead code path with decoy logic
decoys = []
for i in range(3):
    decoy_val = (i + 1) * 113
    decoys.append(decoy_val)

# Unused conditional altering nonexistent flow
if len(decoys) > 2 and theoretical_capacity > 4.0:
    climate_data['adjusted'] = True

# Real computation buried among distractions
def evaluate_stress_factors(temp, rain, toxicity):
    temp_penalty = max(0, (temp - 30) * 0.02) if temp > 30 else 0
    drought_penalty = max(0, (300 - rain) * 0.001) if rain < 300 else 0
    toxicity_penalty = toxicity * 0.5
    return 1 - (temp_penalty + drought_penalty + toxicity_penalty)

# Main optimization function - actual answer source
def optimize_harvest(climate, soil):
    # Primary yield base calculation
    base_yield = 1000
    
    # Environmental modifiers
    temp_mod = 1.0
    if 22 <= climate['avg_temp'] <= 26:
        temp_mod = 1.15
    elif climate['avg_temp'] > 30:
        temp_mod = 0.85
    
    rain_mod = 1.0
    if climate['total_rainfall'] > 400:
        rain_mod = 1.1
    elif climate['total_rainfall'] < 200:
        rain_mod = 0.7
    
    # Soil nutrient multiplier
    nutrient_boost = 1 + (soil['nutrient_score'] / 1000)
    
    # Moisture efficiency factor
    moisture_factor = soil['moisture_retention'] / 5.0
    
    # Combined effect with non-linear interaction
    environmental_multiplier = temp_mod * rain_mod * moisture_factor
    
    # Stress penalty layer
    stress_adjustment = evaluate_stress_factors(
        climate['avg_temp'],
        climate['total_rainfall'],
        soil['toxicity_index']
    )
    
    # Final composition using list comprehension (required feature)
    components = [base_yield, nutrient_boost * 80]
    additive_benefit = sum([c * 0.1 for c in components])
    
    # Key statement: final yield calculation
    final_yield = (
        base_yield * environmental_multiplier * 
        nutrient_boost * stress_adjustment + additive_benefit
    )
    
    # Conditional expression (required feature)
    final_yield = final_yield if final_yield > 0 else 0.0
    
    return final_yield

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_quality)

# Print target result
print(f"Target result: {final_yield}")