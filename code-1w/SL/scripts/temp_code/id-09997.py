def analyze_soil_composition(samples):
    # Irrelevant analysis with misleading computations
    ph_levels = [6.5, 7.2, 8.1, 5.9, 6.8]
    nutrient_score = 0
    for sample in samples:
        nutrient_score += (sample % 3) * 1.5
    avg_ph = sum(ph_levels) / len(ph_levels)
    return nutrient_score if avg_ph > 6.0 else 0


def validate_irrigation_pattern(pattern):
    # Distractor function: looks important but not used in final logic
    total_cycles = 0
    for row in pattern:
        for cell in row:
            if cell == 'on':
                total_cycles += 1
    return total_cycles > 5

# Simulated sensor data (not all used)
sensor_readings = [120, 135, 140, 115, 150]
soil_samples = [2.3, 1.8, 3.1, 2.7]
irrigation_map = [['on', 'off'], ['on', 'on'], ['off', 'on']]

# Misleading intermediate calculations
temp_buffer = [x ** 0.5 for x in sensor_readings if x > 125]
dummy_metric = sum(temp_buffer) / len(temp_buffer)

# Core data structure with relevant information
land_parcel = {
    'plots': [
        {'size': 10, 'crop_type': 'wheat', 'yield_history': [80, 85, 83]},
        {'size': 15, 'crop_type': 'corn',  'yield_history': [90, 92, 88]},
        {'size': 12, 'crop_type': 'wheat', 'yield_history': [82, 84, 86]}
    ],
    'soil_quality': 'loam',
    'avg_rainfall': 45
}

# Conditional expression and string method usage
def classify_crop_stability(history):
    trend = 'stable' if history[-1] - history[0] >= 0 else 'declining'
    return trend.upper().replace('ING', 'ING_OR_FLAT')

# Helper function with some dead code paths
def calculate_plot_productivity(plot):
    base_yield = sum(plot['yield_history']) / len(plot['yield_history'])
    size_factor = plot['size'] * 0.8
    
    # Unused branch (dead code path)
    if plot['crop_type'].startswith('tomato'):
        adjustment = 1.2
    elif plot['crop_type'] == 'corn':
        adjustment = 1.15
    else:
        adjustment = 1.05
    
    # Semi-relevant logic
    stability = classify_crop_stability(plot['yield_history'])
    bonus = 2 if 'STABLE' in stability else 0
    
    return base_yield * adjustment + bonus + size_factor

# Main calculation with key nesting and interdependencies
def calculate_optimal_yield(parcel):
    total_weighted_yield = 0
    total_size = sum(p['size'] for p in parcel['plots'])
    
    for plot in parcel['plots']:
        raw_productivity = calculate_plot_productivity(plot)
        # Normalize by size
        normalized_yield = raw_productivity * (plot['size'] / total_size)
        total_weighted_yield += normalized_yield
    
    # Final adjustments using conditional expression
    modifier = 1.1 if parcel['soil_quality'] in ['clay', 'loam'] else 0.9
    final_modifier = modifier if parcel['avg_rainfall'] > 40 else 0.8
    
    # Critical answer computation
    result = total_weighted_yield * final_modifier
    
    # Red herring: unrelated string processing
    metadata_tag = f"YIELD-{parcel['soil_quality'].upper()}-{len(parcel['plots'])}".split('-')
    secondary_flag = any(tag.isdigit() for tag in metadata_tag)
    
    return result

# Execution point of interest
final_yield = calculate_optimal_yield(land_parcel)

# Print result as required
print(f"Result: {final_yield}")