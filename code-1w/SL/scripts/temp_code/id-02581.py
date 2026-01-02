def calculate_harvest_efficiency(fields, settings):
    base_multiplier = settings['efficiency_factor']
    penalty_rate = settings['weather_penalty']
    boost_threshold = settings['min_size_boost']
    
    # Irrelevant preprocessing: normalize field IDs (not used in result)
    normalized_ids = [f"F{idx:03d}" for idx in range(len(fields))]
    temp_log = {fid: 0 for fid in normalized_ids}
    
    total_yield = 0
    efficiency_corrections = []
    
    for i, field in enumerate(fields):
        size = field['area']
        soil_quality = field['soil_score']
        planted_crop = field['crop_type']
        
        # Initial yield estimation
        raw_yield = size * soil_quality * base_multiplier
        
        # Apply crop-specific adjustment (distraction: not all are used)
        if planted_crop == 'wheat':
            raw_yield *= 1.1
        elif planted_crop == 'corn':
            raw_yield *= 0.95
        elif planted_crop == 'soy':
            raw_yield *= 1.05
        
        # Conditional boost for large fields
        if size > boost_threshold:
            raw_yield += 50
        
        # Simulate weather degradation
        adjusted_yield = raw_yield * (1 - penalty_rate)
        
        # Track corrections for unused analytics
        efficiency_corrections.append(abs(adjusted_yield - raw_yield))
        
        # Only every second field is actually counted due to zoning regulations
        if i % 2 == 0:
            total_yield += adjusted_yield
        
        # Dead code branch: never executed but looks relevant
        if False:
            backup_correction = sum(efficiency_corrections) / len(efficiency_corrections)
            total_yield += backup_correction

    # Final adjustment based on aggregate thresholds
    correction_factor = 1.0
    if len(efficiency_corrections) > 3:
        correction_factor = 0.98
    
    intermediate_result = total_yield * correction_factor
    
    # Distractor: complex slicing and set logic with no impact
    sample_yields = efficiency_corrections[1:-1] if len(efficiency_corrections) > 2 else []
    unique_corrections = list(set(sample_yields))
    if len(unique_corrections) > 1:
        unique_corrections.sort(reverse=True)
        peak_variance = unique_corrections[0] - unique_corrections[-1]
        # Unused variable
        stability_index = (1 - (peak_variance / max(unique_corrections))) if peak_variance > 0 else 1

    final_yield = int(intermediate_result)  # Key assignment point
    
    # Additional red herring: update log with irrelevant mappings
    for j, val in enumerate(unique_corrections):
        temp_log[normalized_ids[j]] = val * 0.01

    return final_yield

# Configuration and input data
config = {
    'efficiency_factor': 2.5,
    'weather_penalty': 0.12,
    'min_size_boost': 40
}

field_data = [
    {'area': 50, 'soil_score': 8, 'crop_type': 'wheat'},
    {'area': 30, 'soil_score': 6, 'crop_type': 'corn'},
    {'area': 60, 'soil_score': 9, 'crop_type': 'soy'},
    {'area': 45, 'soil_score': 7, 'crop_type': 'wheat'},
    {'area': 70, 'soil_score': 8, 'crop_type': 'corn'}
]

# Execute
final_yield = calculate_harvest_efficiency(field_data, config)
print(f"Result: {final_yield}")