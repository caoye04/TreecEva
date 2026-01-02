def calculate_optimal_yield(data, thresholds):
    total_yield = 0
    adjustment_factor = 1.25
    decay_rate = 0.9
    temp_buffer = []
    
    # Preprocess: filter valid zones using dictionary keys
    valid_zones = {k: v for k, v in data.items() if len(k) >= 3 and k.startswith('zone')}
    
    # Misleading computation: buffer accumulation with no impact
    for key in data:
        if 'temp' in key:
            temp_buffer.append(len(key) * 0.5)
    buffered_sum = sum(temp_buffer) / (len(temp_buffer) + 1)

    # Core logic: compute yield based on threshold mapping
    for zone, values in valid_zones.items():
        base_score = sum(values)
        zone_id = zone.split('_')[1]
        
        # Set-based overlap to determine quality tier
        expected_range = set(range(80, 120))
        observed_set = set(values)
        overlap_count = len(observed_set & expected_range)
        
        # String analysis for zone classification
        modifier = 1.0
        if zone_id.isdigit() and int(zone_id) % 2 == 0:
            modifier *= 1.1
        if 'legacy' in zone:
            modifier *= 0.85
        
        # Threshold lookup
        zone_type = 'default'
        if int(zone_id) < 10:
            zone_type = 'alpha'
        elif int(zone_id) < 20:
            zone_type = 'beta'
        
        thresh = thresholds.get(zone_type, 100)
        
        # Accumulate adjusted yield
        if base_score > thresh * len(values):
            total_yield += base_score * modifier * adjustment_factor
        else:
            total_yield += base_score * decay_rate

    # Red herring: unused min/max/average chain
    all_values = [v for sublist in data.values() for v in sublist]
    peak = max(all_values)
    trough = min(all_values)
    avg_val = sum(all_values) / len(all_values)
    stability_metric = (peak - trough) / avg_val if avg_val else 0

    # Final adjustment
    final_yield = int(total_yield - buffered_sum)  # buffered_sum has negligible effect
    return final_yield

# Input data structure
harvest_data = {
    'zone_5': [85, 92, 96, 78],
    'zone_12': [110, 115, 105, 120],
    'zone_19': [65, 70, 68, 72],
    'zone_21': [95, 90, 93, 97],
    'temp_zone_x': [50, 55],
    'legacy_zone_4': [88, 81, 85, 89]
}

threshold_map = {
    'alpha': 88,
    'beta': 105,
    'gamma': 95
}

# Key execution point
final_yield = calculate_optimal_yield(harvest_data, threshold_map)
print(f"Result: {final_yield}")