from collections import defaultdict, Counter

# Simulate agricultural yield prediction based on climate and soil data
def preprocess_climate_records(raw_data):
    processed = defaultdict(float)
    scaling_factor = 1.05
    for key, value in raw_data.items():
        if 'temp' in key:
            processed[key] += value * scaling_factor
        elif 'precip' in key:
            processed[key] += value * 0.95
    return processed

def evaluate_soil_nutrients(profiles):
    nutrient_score = 0
    dummy_counter = Counter()
    for p in profiles:
        dummy_counter[p['type']] += 1
        if p['ph'] > 6.0 and p['ph'] < 7.2:
            nutrient_score += 10
        if p['organic_content'] > 3.0:
            nutrient_score += 5
    # Irrelevant aggregation
    total_types = sum(dummy_counter.values())
    return nutrient_score

def calculate_growth_window(climate):
    window = 0
    temp_summer = climate.get('temp_summer_avg', 0)
    if 18 <= temp_summer <= 30:
        window += 120
    elif 15 <= temp_summer < 18:
        window += 90
    else:
        window += 60
    # Distractor calculation
    adjusted_rainfall = climate.get('precip_spring_total', 0) * 1.1
    return window

def calculate_harvest_potential(climate_input, soil_input):
    # Step 1: Preprocess climate data
    climate_data = preprocess_climate_records(climate_input)
    
    # Step 2: Evaluate soil nutrient score
    soil_nutrient_index = evaluate_soil_nutrients(soil_input)
    
    # Step 3: Calculate viable growth window
    growing_days = calculate_growth_window(climate_data)
    
    # Step 4: Compute baseline yield from temperature-adjusted metrics
    base_temp_effect = climate_data.get('temp_summer_avg', 25) - 20
    if base_temp_effect < 0:
        base_temp_effect = 0
    
    # Step 5: Combine factors into yield potential
    intermediate_yield = (soil_nutrient_index * 2.5) + (growing_days * 0.8)
    
    # Step 6: Apply precipitation weighting (only if sufficient summer rain)
    precip_weight = 1.0
    if climate_data.get('precip_summer_total', 0) > 200:
        precip_weight = 1.2
    elif climate_data.get('precip_summer_total', 0) < 100:
        precip_weight = 0.8
    
    # Step 7: Final yield calculation
    final_yield = intermediate_yield * precip_weight * (1 + base_temp_effect * 0.02)
    
    # Irrelevant final normalization
    max_possible = 1000.0
    normalized = (final_yield / max_possible) * 100
    
    return final_yield

# Input data
climate_input_data = {
    'temp_winter_avg': 5.2,
    'temp_spring_avg': 12.3,
    'temp_summer_avg': 26.8,
    'temp_autumn_avg': 14.1,
    'precip_spring_total': 240,
    'precip_summer_total': 215,
    'precip_autumn_total': 180
}

soil_profiles_data = [
    {'type': 'loam', 'ph': 6.5, 'organic_content': 3.8},
    {'type': 'clay', 'ph': 5.8, 'organic_content': 2.4},
    {'type': 'sandy_loam', 'ph': 6.9, 'organic_content': 4.1}
]

# Execute main function
final_yield = calculate_harvest_potential(climate_input_data, soil_profiles_data)
print(f"Target result: {final_yield}")