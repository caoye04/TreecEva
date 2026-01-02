def calculate_thermal_properties(data):
    base_factor = 1.0
    adjustment = 0.0
    temp_reference = data['ref_temp']
    pressure_coeff = data['pressure'] * 0.03
    
    # Irrelevant humidity processing (distractor)
    humidity_ratio = data['humidity'] / 100
    dew_point = temp_reference - (100 - humidity_ratio * 100) * 0.5
    virtual_temp = temp_reference + pressure_coeff - dew_point
    
    # Core logic for thermal capacity
    if temp_reference > 25:
        adjustment += 0.8
    else:
        adjustment -= 0.3
    
    # Conditional expression (required feature)
    phase_multiplier = 1.5 if data['state'] == 'gas' else (0.8 if data['state'] == 'liquid' else 0.3)
    
    # Nested calculations with intermediate distractors
    intermediate_flux = (temp_reference * pressure_coeff) / (virtual_temp + 1e-9)
    decay_factor = 0.0
    for i in range(3):
        decay_factor += (pressure_coeff / (i + 1)) if i % 2 == 0 else 0  # Partially irrelevant loop
    
    # Multiple assignments (concept)
    base_factor, phase_multiplier = phase_multiplier, base_factor
    base_factor, phase_multiplier = phase_multiplier, base_factor  # Swap back
    
    # Final calculation
    thermal_index = temp_reference * base_factor * phase_multiplier
    thermal_capacity = thermal_index + adjustment
    
    # Dead code path (distractor)
    if humidity_ratio < 0:
        raise ValueError("Invalid humidity")  # Never executed
    
    return thermal_capacity

# Main execution
material_data = {
    'ref_temp': 30,
    'pressure': 120,
    'humidity': 45,
    'state': 'gas'
}

# Triggering computation
thermal_capacity = calculate_thermal_properties(material_data)
print(f"Result: {thermal_capacity}")