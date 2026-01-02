from itertools import compress, cycle
import math

# Simulated environmental sensor data (irrelevant in part)
temperature_readings = [23, 25, 22, 28, 30, 27, 24]
humidity_levels = [65, 70, 75, 60, 55, 68, 72]

# Core agricultural model inputs
soil_profiles = [
    {'ph': 6.5, 'moisture': 0.3, 'nutrients': 7, 'depth': 40},
    {'ph': 5.8, 'moisture': 0.2, 'nutrients': 5, 'depth': 30},
    {'ph': 7.0, 'moisture': 0.4, 'nutrients': 9, 'depth': 50}
]

current_crop_rotation = ['corn', 'wheat', 'soy']
expected_pest_pressure = 0.67

# Distractor: unused legacy function
def legacy_yield_model(data):
    return sum(d.get('nutrients', 0) * 10 for d in data)

# Distractor: irrelevant computation chain
baseline_evaporation = 0
for temp in temperature_readings:
    baseline_evaporation += math.log(temp + 1) * 1.5

# Simulated climate stress factors
climate_data = {
    'seasonal_rainfall': [80, 120, 150, 90],
    'drought_days': 12,
    'frost_risk': True,
    'uv_index_avg': 6.4
}

# Secondary metric with partial relevance
biomass_accumulation = list(map(lambda x: x['moisture'] * x['nutrients'] * 200, soil_profiles))

# Complex helper functions with mixed relevance

def calculate_ph_balance(profiles):
    balanced_count = 0
    for p in profiles:
        if 6.0 <= p['ph'] <= 7.0:
            balanced_count += 1
    return balanced_count

# Irrelevant auxiliary function dealing with crop rotation (dead path)
def update_rotation(crops, new_crop):
    crops.append(new_crop)
    return crops[:-1]

# Key transformation using itertools and slicing
filtered_rainfall = list(compress(
    climate_data['seasonal_rainfall'],
    [r > 100 for r in climate_data['seasonal_rainfall']]
))

rainfall_cycler = cycle([1, 0, 1])
mask_pattern = [next(rainfall_cycler) for _ in range(4)]
decoded_stress = [r * m for r, m in zip(climate_data['seasonal_rainfall'], mask_pattern)]

# Misleading intermediate yield estimate (decoy)
estimated_base_yield = sum(filtered_rainfall) / 10

# Real computational core with recursion and conditionals
def assess_stress_factor(data):
    factor = 1.0
    if data['drought_days'] > 10:
        factor *= 0.85
    if data['frost_risk']:
        factor *= 0.9
    if data['uv_index_avg'] > 6:
        factor *= 0.95
    return factor

# Recursive nutrient availability simulation
def simulate_nutrient_leaching(levels, depth, step=0):
    if step >= 2 or depth < 35:
        return levels * 0.9
    return simulate_nutrient_leaching(levels * 0.95, depth - 5, step + 1)

# Main optimization function combining multiple concepts
def optimize_harvest(climate, soils):
    base_yield = 0
    stress_factor = assess_stress_factor(climate)
    ph_balance_score = calculate_ph_balance(soils)
    
    # Meaningful slicing operation on biomass
    peak_biomass = max(biomass_accumulation[1:], default=0)
    
    for idx, profile in enumerate(soils):
        nutrients = profile['nutrients']
        depth = profile['depth']
        moisture = profile['moisture']
        
        # Apply recursive leaching model only to deep soils
        if depth >= 40:
            nutrients = simulate_nutrient_leaching(nutrients, depth)
        
        # Primary yield contribution
        local_yield = nutrients * moisture * 50
        
        # Boost from balanced pH zones
        if 6.2 <= profile['ph'] <= 6.8:
            local_yield *= 1.15
        
        base_yield += local_yield
    
    # Final adjustment using itertools-derived pattern
    correction_factor = sum(decoded_stress) / 100
    
    # Critical calculation
    final = (base_yield * stress_factor + ph_balance_score * 10) - correction_factor * 5
    
    # Distractor: unused refinement
    if final > 200:
        final = round(final, 1)
    
    return final

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print result as required
print(f"Result: {final_yield}")