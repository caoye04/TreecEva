from collections import defaultdict, Counter
import math

# Simulated agricultural yield optimization with red herrings
def analyze_soil_composition(data):
    # Irrelevant computation: soil nutrient analysis (not used in final result)
    nutrients = defaultdict(int)
    for entry in data:
        for nutrient in entry.get('nutrients', []):
            nutrients[nutrient] += 1
    return dict(nutrients)

def compute_rainfall_deviation(historical, current):
    # Distractor function: computes rainfall stats but not used
    avg = sum(historical) / len(historical)
    deviation = abs(avg - current)
    z_score = deviation / (math.sqrt(sum((x - avg) ** 2 for x in historical) / len(historical)) + 1e-9)
    return round(z_score, 4)

def evaluate_pest_resistance(plant_variety):
    # Dead code path: never actually contributes to output
    resistance_profile = {
        'A': [0.8, 0.6, 0.9],
        'B': [0.5, 0.7, 0.4],
        'C': [0.9, 0.3, 0.6]
    }
    if plant_variety in resistance_profile:
        base = sum(resistance_profile[plant_variety])
        adjusted = base * 1.15 if base > 2.0 else base * 0.85
        return round(adjusted, 3)
    return 0.0

def calculate_harvest_efficiency(fields, settings):
    efficiency_map = {}
    total_area = 0
    effective_yield = 0
    
    # Real logic begins here — nested and interwoven with distractions
    modifier_chain = lambda x, m: x * m if x > 0 else x + m
    
    for field_id, details in fields.items():
        area = details['area_sqkm']
        base_yield = details['base_yield_tons_per_km2']
        crop_type = details['crop']
        
        # Relevant conditional logic tree (3 levels deep)
        if area > 0:
            temp_modifier = settings['climate_modifiers'].get(details['zone'], 1.0)
            if crop_type == 'wheat':
                yield_potential = base_yield * temp_modifier
                if details['irrigated']:
                    yield_potential = modifier_chain(yield_potential, 1.25)
                pest_factor = evaluate_pest_resistance(crop_type)  # Called but does NOT affect anything
                yield_potential -= 0.1  # Fixed loss adjustment
            elif crop_type == 'corn':
                yield_potential = base_yield * 0.95
            else:
                yield_potential = base_yield * 0.7
            
            # Accumulate real values
            efficiency_map[field_id] = round(yield_potential, 3)
            total_area += area
            effective_yield += yield_potential * area
        
    # Final aggregation step
    if total_area > 0:
        overall_efficiency = effective_yield / total_area
    else:
        overall_efficiency = 0
    
    # Secondary transformation
    adjustment_factor = settings['yield_adjustment_factor']
    final_result = overall_efficiency * adjustment_factor
    
    # Decoy intermediate print (not actual result)
    _debug_value = sum(efficiency_map.values()) * 0.1
    
    return round(final_result, 6)

# Setup input data
field_data = {
    'F01': {'area_sqkm': 12.5, 'base_yield_tons_per_km2': 4.8, 'crop': 'wheat', 'zone': 'temperate', 'irrigated': True},
    'F02': {'area_sqkm': 8.0, 'base_yield_tons_per_km2': 5.2, 'crop': 'wheat', 'zone': 'temperate', 'irrigated': False},
    'F03': {'area_sqkm': 15.3, 'base_yield_tons_per_km2': 3.9, 'crop': 'corn', 'zone': 'continental', 'irrigated': True},
    'F04': {'area_sqkm': 6.7, 'base_yield_tons_per_km2': 4.1, 'crop': 'wheat', 'zone': 'temperate', 'irrigated': True}
}

test_config = {
    'climate_modifiers': {
        'temperate': 1.1,
        'continental': 0.95,
        'tropical': 1.05
    },
    'yield_adjustment_factor': 1.08,
    'simulation_depth': 5,
    'buffer_threshold': 0.25
}

# Irrelevant preprocessing (distractor)
historical_rainfall = [890, 920, 870, 940, 905]
current_rainfall = 915
rain_dev = compute_rainfall_deviation(historical_rainfall, current_rainfall)

soil_analysis = analyze_soil_composition([
    {'nutrients': ['N', 'P', 'K', 'Mg']},
    {'nutrients': ['Ca', 'S', 'N']}
])

# Key execution point
final_yield = calculate_harvest_efficiency(field_data, test_config)

Result: {final_yield}