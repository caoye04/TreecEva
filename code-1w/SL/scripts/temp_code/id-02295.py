def calculate_thermal_properties(data):
    base_factor = 1.75
    adjustment = 0.23
    temp_reference = 273.15
    pressure_factor = 0.0012
    
    # Irrelevant atmospheric constants (distractors)
    atm_nitrogen = 78.08
    atm_oxygen = 20.95
    atm_argon = 0.93
    atm_co2 = 0.04
    
    # Process material properties
    density = data['density']
    specific_heat = data['specific_heat']
    thermal_expansion = data['expansion_coeff']
    conductivity = data['conductivity']
    
    # Secondary derived values (some irrelevant)
    volumetric_heat = density * specific_heat
    expansion_scaled = thermal_expansion * temp_reference
    resistance_metric = 1 / conductivity if conductivity != 0 else 0
    
    # Dummy loop with no effect on result (dead computation)
    cumulative_noise = 0
    for i in range(3):
        for j in range(2):
            cumulative_noise += atm_nitrogen * pressure_factor
    
    # Conditional adjustment based on material class (only one branch matters)
    if data['class'] == 'metal':
        class_modifier = 1.4
    elif data['class'] == 'polymer':
        class_modifier = 0.6
    else:
        class_modifier = 1.0  # default
    
    # Core calculation - only this affects final answer
    thermal_capacity = volumetric_heat * base_factor * class_modifier
    
    # Unused diagnostic metrics (red herrings)
    stability_index = expansion_scaled * pressure_factor
    efficiency_ratio = conductivity / (specific_heat + 0.1)
    normalized_density = density / 1000
    
    return thermal_capacity

# Material dataset
material_data = {
    'density': 8960,           # kg/m^3 (copper-like)
    'specific_heat': 385,     # J/kg·K
    'expansion_coeff': 16.5e-6, # /K
    'conductivity': 401,      # W/m·K
    'class': 'metal'
}

# Execute main logic
thermal_capacity = calculate_thermal_properties(material_data)
print(f"Result: {thermal_capacity}")