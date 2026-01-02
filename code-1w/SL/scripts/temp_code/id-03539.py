import math

# Irrelevant helper function (decoy)
def normalize_string(s):
    return s.upper().strip().replace(' ', '_')

# Unused transformation map (red herring)
transformation_map = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'X': 99, 'Y': 100, 'Z': 101
}

# Simulated land parcel metadata (some fields are irrelevant)
land_parcel_data = [
    {'id': 'P001', 'area': 120, 'soil_quality': 'rich', 'elevation': 150, 'irrigated': True, 'crop_type': 'wheat'},
    {'id': 'P002', 'area': 85, 'soil_quality': 'poor', 'elevation': 320, 'irrigated': False, 'crop_type': 'corn'},
    {'id': 'P003', 'area': 200, 'soil_quality': 'medium', 'elevation': 180, 'irrigated': True, 'crop_type': 'barley'},
    {'id': 'P004', 'area': 90, 'soil_quality': 'rich', 'elevation': 140, 'irrigated': True, 'crop_type': 'wheat'}
]

# Decoy statistical accumulator (never used in final calculation)
decoys = {
    'total_surveys': 12,
    'avg_rainfall_mm': 78.5,
    'invalid_flag_count': 0
}

# Mapping for soil quality to base yield factor (used)
quality_factor = lambda q: { 'poor': 0.5, 'medium': 0.75, 'rich': 1.2 }[q]

# Redundant string-based flag system (distractor)
status_flags = ['valid', 'verified', 'processed']
flag_state = {f: True for f in status_flags}
flag_state['deprecated'] = False

# Auxiliary function that looks important but is unused
def compute_tax_liability(parcel_list):
    total_value = 0
    for p in parcel_list:
        base = p['area'] * 10
        if p['soil_quality'] == 'rich':
            base *= 1.5
        total_value += base
    return total_value * 0.02

# Function that appears in intermediate steps but is not part of final logic
def estimate_water_usage(parcel_list):
    total_water = 0
    for p in parcel_list:
        if p['irrigated']:
            total_water += p['area'] * 300
    return total_water

# Core calculation function with embedded distractions
def calculate_harvest_efficiency(parcel_data):
    cumulative_score = 0
    adjustment_log = []
    
    # Irrelevant pre-scan (looks like validation)
    valid_ids = [p['id'] for p in parcel_data if 'P' in p['id'] and len(p['id']) == 4]
    if len(valid_ids) != len(parcel_data):
        raise ValueError("All parcel IDs must follow P### format")
    
    # Real processing begins
    for idx, parcel in enumerate(parcel_data):
        area = parcel['area']
        base_yield = area * 100  # Base per-hectare assumption
        
        # Quality adjustment
        qf = quality_factor(parcel['soil_quality'])
        adjusted_yield = base_yield * qf
        
        # Irrigation boost (only if irrigated)
        if parcel['irrigated']:
            adjusted_yield *= 1.3
        
        # Elevation penalty if above threshold (real logic)
        if parcel['elevation'] > 200:
            adjusted_yield *= 0.8
        elif parcel['elevation'] < 100:
            adjusted_yield *= 0.95
        
        # Crop-specific modifier (only affects barley)
        crop_mod = 1.0
        if parcel['crop_type'] == 'barley':
            crop_mod = 1.1
        elif parcel['crop_type'] == 'corn':
            # This block is never reached due to data
            crop_mod = 0.85
        adjusted_yield *= crop_mod
        
        # Conditional logging (distractor)
        log_entry = f"Parcel {parcel['id']}: {adjusted_yield:.2f}"
        adjustment_log.append(log_entry)
        
        # Accumulate only the numeric yield
        cumulative_score += adjusted_yield
    
    # Summation and normalization step (key result)
    total_area = sum(p['area'] for p in parcel_data)
    final_efficiency_ratio = cumulative_score / total_area if total_area else 0
    
    # Case conversion on dummy text (irrelevant string operation)
    debug_tag = "Harvest_Normalized"
    normalized_tag = debug_tag.lower().replace('_', '-')
    
    # Dictionary accumulation that does nothing
    stats_snapshot = {
        'run_tag': normalized_tag,
        'parcel_count': len(parcel_data),
        'peak_yield': max([cumulative_score / len(parcel_data), 0])
    }
    
    # Final yield is efficiency ratio multiplied by fixed constant
    final_yield = int(final_efficiency_ratio * 1000)  # Scale and discretize
    
    # DEAD CODE PATH (never executed)
    if False:
        fallback = 0
        for item in stats_snapshot.values():
            if isinstance(item, (int, float)):
                fallback += item
        final_yield = fallback
    
    return final_yield

# Execution entry point
baseline_reference = sum(d['area'] for d in land_parcel_data if d['soil_quality'] == 'rich')
efficiency_trend = [calculate_harvest_efficiency(land_parcel_data) for _ in range(1)]  # Single eval
final_yield = efficiency_trend[0]

# Output result
print(f"Result: {final_yield}")