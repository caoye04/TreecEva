def analyze_soil_composition(data):
    # Irrelevant transformation
    ph_levels = list(map(lambda x: round(x * 1.07 + 0.3, 2), data['ph']))
    nutrient_score = sum([int(n * 2) for n in data['nutrients']]) // len(data['nutrients'])
    return nutrient_score

# Simulate agricultural yield prediction with noise
soil_data = {
    'ph': [6.2, 5.8, 6.4, 7.0, 6.1],
    'nutrients': [0.88, 0.76, 0.94, 0.67, 0.82],
    'moisture': [30, 34, 29, 38, 32]
}

field_ids = ['F1', 'F2', 'F3', 'F4', 'F5']
base_yield_per_acre = 120
yield_adjustment_factor = 0.93

# Distractor: unused climate model
climate_trend = (lambda x: x ** 0.5 * 1.8)(sum(soil_data['moisture']) / len(soil_data['moisture']))

# Real processing begins
composite_nutrient = analyze_soil_composition(soil_data)
adjusted_base = base_yield_per_acre * (1 + composite_nutrient / 100)

processed_fields = []
for fid in field_ids:
    temp_mod = 1.05 if 'F3' in fid or 'F1' in fid else 0.98
    moisture_level = soil_data['moisture'][int(fid[1]) - 1]
    moisture_mod = 1 + (moisture_level - 32) * 0.01
    
    # Distractor variables
    dummy_calc = (moisture_level * temp_mod) % 7
    flag_status = dummy_calc > 3
    
    effective_yield = adjusted_base * temp_mod * moisture_mod * yield_adjustment_factor
    processed_fields.append(effective_yield)

# Summation and accumulation pattern
total_accum = 0
for val in processed_fields:
    total_accum += val * 0.95  # post-harvest loss adjustment

# Final calculation obscured by lambda
amplify = lambda x: x * 1.02
final_yield = 0
intermediate_result = total_accum * 0.88
final_yield = amplify(intermediate_result)

# Key assignment point
final_yield = calculate_harvest(processed_fields)

# Helper function buried after usage (but defined here for execution)
def calculate_harvest(fields):
    baseline = sum(fields) * 0.95
    penalty = 0
    for idx, yld in enumerate(fields):
        if yld < 115:
            penalty += 5
    return int(baseline - penalty)

print(f"Result: {final_yield}")