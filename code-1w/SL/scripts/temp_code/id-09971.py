def calculate_harvest_efficiency(fields, irrigation):
    base_multiplier = 1.2
    penalty_rate = 0.05
    boost_factor = 0.1
    dummy_counter = 0
    total_area = sum([f['area'] for f in fields])
    avg_moisture = sum(irrigation) / len(irrigation) if irrigation else 0

    # Misleading computation - not directly used
    theoretical_max = total_area * 1500 * (1 + boost_factor)
    efficiency_map = {}
    
    for i, field in enumerate(fields):
        area = field['area']
        crop_type = field['crop']
        base_yield = area * 800
        
        # Simulate moisture impact
        moisture_effect = min(1.0, max(0.6, avg_moisture * 0.02))
        
        # Crop-specific modifiers (some are distractions)
        if crop_type == 'wheat':
            modifier = 1.0
            dummy_counter += 1
        elif crop_type == 'corn':
            modifier = 1.1
            penalty_rate += 0.01  # Red herring update
        elif crop_type == 'soy':
            modifier = 0.95
            base_multiplier *= 0.99  # Distracting adjustment
        else:
            modifier = 1.0

        adjusted_yield = base_yield * modifier * moisture_effect * base_multiplier
        efficiency_map[i] = adjusted_yield / area
    
    # Secondary loop for stability check (partially relevant)
    stable_fields = 0
    for val in efficiency_map.values():
        if 700 <= val <= 950:
            stable_fields += 1

    # Final efficiency score with normalization
    raw_total = sum(efficiency_map.values())
    stability_bonus = 1 + (stable_fields / len(fields)) * 0.05
    
    # Actual answer computation
    final_yield = int(raw_total * stability_bonus)
    
    # Dead code - irrelevant to result
    outlier_count = len([v for v in irrigation if v < 30 or v > 90])
    if outlier_count > 2:
        theoretical_max *= 0.9

    return final_yield

# Input data
field_data = [
    {'area': 10, 'crop': 'wheat'},
    {'area': 15, 'crop': 'corn'},
    {'area': 12, 'crop': 'soy'},
    {'area': 8, 'crop': 'wheat'}
]

irrigation_levels = [45, 60, 55, 70, 50]

# Execute and print result
dummy_counter = 0
for _ in irrigation_levels:
    dummy_counter += 1  # Irrelevant counting

final_yield = calculate_harvest_efficiency(field_data, irrigation_levels)
print(f"Result: {final_yield}")