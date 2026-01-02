def analyze_growth_potential(temperature, rainfall):
    # Irrelevant agricultural metrics (distractors)
    evaporation_rate = temperature * 0.6
    humidity_index = min(rainfall / 2.5, 100)
    growth_score = (temperature - 15) * (rainfall / 10)
    if growth_score > 80:
        growth_category = 'Excellent'
    elif growth_score > 50:
        growth_category = 'Good'
    else:
        growth_category = 'Marginal'
    return growth_score  # Only this matters

# Misleading auxiliary function (dead path)
def calculate_irrigation_need(soil_type, moisture_level):
    base_need = 20
    if soil_type == 'clay':
        return base_need * 0.5
    elif soil_type == 'sand':
        return base_need * 1.8
    return base_need  # Unused in main logic

# Complex but partially irrelevant data preprocessing
def preprocess_climate_data(raw_data):
    cleaned = []
    for entry in raw_data:
        temp_c = entry['temp'] - 273.15
        precip_mm = entry['precip'] * 10
        normalized = {'temp': temp_c, 'precip': precip_mm}
        # Distractor: unused field
        normalized['dew_point'] = temp_c - (100 - entry.get('humidity', 50)) / 5
        cleaned.append(normalized)
    return cleaned

# Core logic buried within distractions
def evaluate_stress_factors(temp_seq, precip_seq):
    heat_stress = 0
    drought_stress = 0
    for t in temp_seq:
        if t > 35:
            heat_stress += (t - 35) * 0.3
    for p in precip_seq:
        if p < 20:
            drought_stress += (20 - p) * 0.1
    return heat_stress, drought_stress

# Real computation hidden among red herrings
def optimize_harvest(climate_data, soil_profiles):
    # Step 1: Preprocess climate (some output used, some not)
    processed_data = preprocess_climate_data(climate_data)
    temps = [entry['temp'] for entry in processed_data]
    rains = [entry['precip'] for entry in processed_data]
    
    # Step 2: Compute growth potential (used later)
    total_potential = 0
    for i in range(len(temps)):
        score = analyze_growth_potential(temps[i], rains[i])
        total_potential += score
    
    # Step 3: Evaluate stress factors (used)
    heat, drought = evaluate_stress_factors(temps, rains)
    
    # Step 4: Simulate soil nutrient retention (mostly irrelevant)
    retained_nutrients = 0
    for profile in soil_profiles:
        ph = profile['ph']
        organic_matter = profile['organic']
        # Following lines are decoys
        cec = organic_matter * 5 + (7 - abs(ph - 6.5)) * 2
        leaching_risk = 'low' if organic_matter > 3 and ph > 5.5 else 'high'
        retained_nutrients += organic_matter * 10  # Unused sum
    
    # Step 5: Apply complex yield formula (key calculation)
    base_yield = total_potential * 0.4
    stress_penalty = (heat * 1.2) + (drought * 1.5)
    efficiency_factor = 0.85 if len(soil_profiles) > 2 else 0.7
    adjustment_map = {0: 1.0, 1: 0.95, 2: 0.9, 3: 0.85, 4: 0.8}
    size_factor = adjustment_map.get(len(processed_data), 0.7)
    
    # Final computation
    final_yield = (base_yield - stress_penalty) * efficiency_factor * size_factor
    
    # Red herring: modifying unused variables
    dummy_result = {'status': 'optimized', 'iterations': 12, 'converged': True}
    dummy_result['yield_backup'] = final_yield * 0.9  # Not used
    
    return final_yield

# Input data with realistic structure
climate_data = [
    {'temp': 298.15, 'precip': 80, 'humidity': 60},
    {'temp': 305.15, 'precip': 40, 'humidity': 45},
    {'temp': 310.15, 'precip': 15, 'humidity': 30},
    {'temp': 308.15, 'precip': 25, 'humidity': 35},
    {'temp': 302.15, 'precip': 60, 'humidity': 50}
]

soil_profiles = [
    {'ph': 6.2, 'organic': 3.5, 'texture': 'loam'},
    {'ph': 5.8, 'organic': 2.8, 'texture': 'silt'},
    {'ph': 6.5, 'organic': 4.1, 'texture': 'clay-loam'}
]

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Target result: {final_yield}")