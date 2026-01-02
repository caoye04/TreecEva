def calculate_harvest_efficiency(fields, settings):
    # Precompute threshold using lambda for dynamic filtering
    yield_threshold = lambda x: x > settings['base_yield'] * 1.5

    # Auxiliary tracking variables (some are distractions)
    total_fields = len(fields)
    high_yield_count = 0
    adjusted_yield_sum = 0
    penalty_factor = 0.9 if settings['weather'] == 'dry' else 1.0
    phantom_counter = 0  # Unused variable - red herring

    # Simulate soil quality adjustments (not all used)
    soil_boost = {}
    for field_id, data in fields.items():
        base = data['yield']
        if data['soil_type'] == 'loam':
            soil_boost[field_id] = base * 0.1
        elif data['soil_type'] == 'clay':
            soil_boost[field_id] = -base * 0.05
        else:
            soil_boost[field_id] = 0

    # Core logic: compute adjusted yields with filtering
    valid_fields = []
    for field_id, data in fields.items():
        raw_yield = data['yield']
        adjustment = 0

        # Apply irrigation boost if applicable
        if data['irrigated']:
            adjustment += raw_yield * 0.2

        # Apply pest control penalty if not treated
        if not data['treated']:
            adjustment -= raw_yield * 0.3

        # Adjusted yield after factors
        adj_yield = raw_yield + adjustment

        # Track high-yield fields above dynamic threshold
        if yield_threshold(adj_yield):
            high_yield_count += 1

        # Only include fields that passed minimum size filter
        if data['area_hectares'] >= settings['min_size']:
            adjusted_yield_sum += adj_yield * penalty_factor
            valid_fields.append(adj_yield)

        # Dead code path - misleading computation
        if adj_yield < 0:
            phantom_counter += 1  # Never reached due to data constraints

    # Compute efficiency score
    if valid_fields:
        average_effective_yield = adjusted_yield_sum / len(valid_fields)
        consistency_bonus = 1.0 + (high_yield_count / total_fields) * 0.1
        final_efficiency = average_effective_yield * consistency_bonus
    else:
        final_efficiency = settings['base_yield'] * 0.5

    # Distractor dictionary operations
    stats = {
        'count': total_fields,
        'high_yield_fields': high_yield_count,
        'phantom_triggered': phantom_counter,
        'method': 'adjusted_mean'
    }
    stats.update({'version': '2.1'})  # Irrelevant update

    return int(final_efficiency)  # Final result as integer


# Input data
field_data = {
    'F01': {'yield': 80, 'soil_type': 'loam', 'irrigated': True, 'treated': False, 'area_hectares': 5},
    'F02': {'yield': 60, 'soil_type': 'clay', 'irrigated': False, 'treated': True, 'area_hectares': 4},
    'F03': {'yield': 90, 'soil_type': 'loam', 'irrigated': True, 'treated': True, 'area_hectares': 6},
    'F04': {'yield': 50, 'soil_type': 'sand', 'irrigated': False, 'treated': False, 'area_hectares': 3},
    'F05': {'yield': 75, 'soil_type': 'loam', 'irrigated': True, 'treated': False, 'area_hectares': 5}
}

config = {
    'base_yield': 65,
    'min_size': 4,
    'weather': 'dry'
}

# Execution point
final_yield = calculate_harvest_efficiency(field_data, config)
print(f"Result: {final_yield}")