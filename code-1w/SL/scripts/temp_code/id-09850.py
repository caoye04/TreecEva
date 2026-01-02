def calculate_harvest_efficiency(zones, stress_levels):
    base_multiplier = 1.25
    efficiency_slots = [0] * len(zones)
    temp_offset = 0
    
    for i, (zone_id, area) in enumerate(zones.items()):
        if area < 10:
            efficiency_slots[i] = 0.5
            continue
        
        # Irrelevant temperature adjustment (not used in final calculation)
        temp_adjustment = (i + 1) * 0.05
        temp_offset += temp_adjustment
        
        stress_index = stress_levels.get(zone_id, 1)
        raw_efficiency = area * base_multiplier
        
        # Distractor: unused intermediate
        hypothetical_yield = raw_efficiency * 1.3
        
        if stress_index > 1.5:
            efficiency_slots[i] = raw_efficiency * 0.6
        elif stress_index > 1:
            efficiency_slots[i] = raw_efficiency * 0.8
        else:
            efficiency_slots[i] = raw_efficiency * 1.0
    
    # Use of zip and conditional expression
    adjusted_values = [val if val > 6 else val * 1.1 for val in efficiency_slots]
    total_contribution = sum(adjusted_values)
    
    # Dead code path - never executed due to data
    sentinel_flag = False
    if sentinel_flag:
        total_contribution *= 0.9  # This is never reached
    
    return int(total_contribution)

# Main execution
area_config = {'A1': 12, 'B2': 15, 'C3': 8, 'D4': 20}
stress_factors = {'A1': 1.2, 'B2': 0.9, 'D4': 1.8}  # C3 missing => default 1

intermediate_debug = [x * 0.5 for x in [10, 20, 30]]  # Unused list

final_yield = calculate_harvest_efficiency(area_config, stress_factors)
print(f"Result: {final_yield}")