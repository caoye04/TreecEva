def analyze_growth_pattern(conditions):
    # Irrelevant ecological analysis (dead code path)
    biomass = 0
    for c in conditions:
        biomass += c * 0.34
    return [x * 1.2 for x in conditions]  # Unused result

def update_sensor_readings(log, offset=0.05):
    # Distractor: sensor calibration with no impact
    adjusted = []
    for i, val in enumerate(log):
        adjusted.append(val + offset * (i % 3))
    return sorted(adjusted, reverse=True)  # Never used

def detect_pest_outbreak(readings):
    # Misleading intermediate: looks important but unused
    threshold = 7.2
    count = 0
    for r in readings:
        if r > threshold:
            count += 1
    alert_level = 'MODERATE' if 2 < count <= 5 else 'LOW'
    return alert_level  # Not used in main logic

def compute_root_depth(soil_layers):
    depth = 0
    factor = 1.0
    for layer in soil_layers:
        if layer['type'] == 'clay':
            factor *= 0.8
        elif layer['type'] == 'sandy':
            factor += 0.1
        depth += layer['thickness'] * factor
    return depth * 0.4  # Red herring calculation

def calculate_harvest_efficiency(fields, infestation):
    total_efficiency = 0.0
    base_modifier = 1.0 - (infestation * 0.08)
    
    for idx, field in enumerate(fields):
        area = field['size']
        quality = field['fertility']
        
        # Real logic begins here
        crop_type_bonus = 1.0
        if field['crop'] == 'wheat':
            crop_type_bonus = 1.15
        elif field['crop'] == 'barley':
            crop_type_bonus = 1.08
            
        # Simulated yield baseline
        raw_yield = area * quality * 0.67
        
        # Apply modifiers
        adjusted_yield = raw_yield * base_modifier * crop_type_bonus
        
        # Special condition using zip and enumerate together
        bonuses = [0.1, 0.05, 0.12, 0.08]
        penalties = [0.03, 0.07, 0.02, 0.04]
        
        for i, (b, p) in enumerate(zip(bonuses, penalties)):
            if idx == i:
                adjusted_yield *= (1 + b - p)

        # Hidden critical adjustment: only odd-indexed fields get climate boost
        if idx % 2 == 1:
            climate_factor = 1.05 + (infestation * 0.01)
            adjusted_yield *= climate_factor

        total_efficiency += adjusted_yield
    
    # Final transformation
    final = total_efficiency * 0.92
    
    # Dead code distractors below
    outlier_check = [x for x in fields if x['fertility'] > 5.0]
    if len(outlier_check) > 2:
        final *= 0.98
    
    return int(final)  # Deterministic integer answer

# Main execution block
if __name__ == '__main__':
    # Input data
    area_data = [
        {'size': 120, 'fertility': 4.2, 'crop': 'wheat'},
        {'size': 95, 'fertility': 4.8, 'crop': 'barley'},
        {'size': 150, 'fertility': 3.9, 'crop': 'wheat'},
        {'size': 88, 'fertility': 4.5, 'crop': 'corn'},
        {'size': 200, 'fertility': 4.1, 'crop': 'wheat'}
    ]
    
    pest_index = 3.4
    
    # Irrelevant pre-processing (distractor)
    growth_conditions = [22, 65, 4.1, 8.3, 1.2]
    soil_profile = [
        {'type': 'loam', 'thickness': 30},
        {'type': 'clay', 'thickness': 15},
        {'type': 'sandy', 'thickness': 10}
    ]
    
    _ = analyze_growth_pattern(growth_conditions)
    _ = update_sensor_readings([7.1, 6.9, 7.3, 7.0, 6.8])
    _ = detect_pest_outbreak([6.5, 7.1, 6.8, 7.4])
    _ = compute_root_depth(soil_profile)
    
    # Key statement
    final_yield = calculate_harvest_efficiency(area_data, pest_index)
    
    print(f"Target result: {final_yield}")