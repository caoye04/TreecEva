def calculate_system_capacity():
    base_load = 987
    temperature_offset = 3
    peak_multiplier = 1.2
    
    # Adjust base load based on environmental temperature
    adjusted_base = base_load + (temperature_offset * 15)
    
    # Simulate minor sensor calibration (irrelevant to final result)
    calibration_reference = "CAL-7A"
    version_tag = calibration_reference.lower().replace('-', '_')
    metadata_flag = len(version_tag) > 5
    
    # Efficiency determined by hardware generation
    hardware_generation = 7
    if hardware_generation >= 5:
        efficiency_factor = 2
    else:
        efficiency_factor = 3
    
    # Final capacity calculation using integer division
    final_capacity = adjusted_base // efficiency_factor
    
    # Logging output (does not affect computation)
    print(f"System report: {calibration_reference}")
    
    return final_capacity

result = calculate_system_capacity()
print("Result: " + str(result))