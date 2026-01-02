def analyze_soil_composition(traces):
    # Irrelevant computation: analyzes trace elements but not used in final result
    heavy_metals = {elem for elem in traces if elem in ['Pb', 'Cd', 'Hg']}
    nutrient_levels = {k: v for k, v in traces.items() if k in ['N', 'P', 'K']}
    avg_nutrient = sum(nutrient_levels.values()) / len(nutrient_levels) if nutrient_levels else 0
    return avg_nutrient

traces = {'N': 14, 'P': 8, 'K': 12, 'Fe': 5, 'Cd': 2, 'Mn': 3}
analyze_soil_composition(traces)

# Simulate seasonal weather patterns (some values are red herrings)
seasonal_rainfall = [120, 85, 100, 0, 60, 95, 130, 75, 0, 45]
valid_days = [i for i, r in enumerate(seasonal_rainfall) if r > 0]
dry_spells = [i for i, r in enumerate(seasonal_rainfall) if r == 0]  # Not used later

def compute_growth_index(rain_data):
    peak_periods = rain_data[2:8]  # Slicing: relevant segment
    base_growth = sum(peak_periods) / len(peak_periods)
    fluctuation = max(peak_periods) - min(peak_periods)
    adjusted_growth = base_growth - (fluctuation * 0.1)
    return adjusted_growth

growth_index = compute_growth_index(seasonal_rainfall)

# Crop rotation history – complex data structure with unused fields
rotation_log = [
    {'crop': 'wheat', 'yield': 3.2, 'year': 2020},
    {'crop': 'corn', 'yield': 4.1, 'year': 2021},
    {'crop': 'soy', 'yield': 3.8, 'year': 2022}
]

current_rotation_score = sum(entry['yield'] for entry in rotation_log) / len(rotation_log)
projected_increase = current_rotation_score * 0.05  # Minor factor, not directly used

# Land parcel data with slicing and character counting
land_parcel = {
    'id': 'FIELD-7B',
    'soil_type': 'loam',
    'area_acres': 45,
    'recent_crops': ['corn', 'wheat', 'barley'],
    'historical_notes': 'Fertile loam soil with good drainage. No contamination detected.'
}

# Count vowel characters in notes (distractor)
vowel_count = sum(1 for c in land_parcel['historical_notes'].lower() if c in 'aeiou')

# Core logic hidden among distractions
def calculate_optimal_harvest(parcel):
    base_area = parcel['area_acres']
    recent_crops = parcel['recent_crops']
    
    # Use slicing to analyze crop continuity
    recent_two = recent_crops[-2:]  # last two crops
    
    # Character count as proxy for record detail (semi-relevant)
    detail_score = len(parcel['historical_notes'])
    
    # Key calculation chain
    modifier = 1.0
    if 'corn' in recent_two:
        modifier += 0.1
    if 'wheat' in recent_two:
        modifier += 0.05
    
    # Hidden dependency on growth_index from earlier
    environmental_factor = growth_index / 100.0  # normalized
    
    # Final yield formula combines area, modifier, and environment
    potential_yield = base_area * modifier * (1 + environmental_factor)
    
    # Dead code branch (never executed due to fixed input)
    if parcel['soil_type'] == 'clay':
        potential_yield *= 0.7  # reduced drainage
    
    # Redundant assignment (distraction)
    potential_yield = round(potential_yield, 2)
    
    return potential_yield

final_yield = calculate_optimal_harvest(land_parcel)
print(f"Target result: {final_yield}")