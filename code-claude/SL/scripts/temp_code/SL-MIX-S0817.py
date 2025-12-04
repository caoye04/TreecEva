def analyze_elemental_composition(raw_data, threshold=50):
    # Extract elemental signatures from raw data
    elements = {}
    for i, value in enumerate(raw_data):
        element_code = (value & 0xFF00) >> 8
        intensity = value & 0xFF
        if element_code not in elements:
            elements[element_code] = []
        elements[element_code].append(intensity)
    
    # Process radiation levels (not needed for main calculation)
    radiation_levels = [sum(elements.get(code, [0])) for code in range(1, 10)]
    max_radiation = max(radiation_levels) if radiation_levels else 0
    
    # Calculate stability factors (distraction)
    stability = {}
    for code, intensities in elements.items():
        avg = sum(intensities) / len(intensities) if intensities else 0
        stability[code] = avg > threshold
    
    # Determine power levels based on frequency and intensity
    power_levels = {}
    for code, intensities in elements.items():
        # Only specific element codes contribute to power calculation
        if code % 3 == 0 and code <= 15:
            power = len(intensities) * (sum(intensities) / len(intensities) if intensities else 0)
            power_levels[code] = int(power)
    
    # Check for special combinations (distraction)
    special_combos = {(3, 6), (9, 12), (6, 15)}
    present_codes = set(elements.keys())
    combo_bonus = sum(10 for combo in special_combos if all(c in present_codes for c in combo))
    
    # Determine active element based on intensity patterns
    candidate_elements = [code for code in elements if sum(elements[code]) > threshold * 2]
    filtered_elements = [code for code in candidate_elements if code in power_levels]
    
    # Select active element with highest single intensity reading
    active_element = 0
    max_single_reading = 0
    for code in filtered_elements:
        current_max = max(elements[code]) if elements[code] else 0
        if current_max > max_single_reading:
            max_single_reading = current_max
            active_element = code
    
    # Apply environmental modifiers (distraction)
    env_modifiers = {3: 1.5, 6: 0.8, 9: 2.0, 12: 1.2, 15: 0.5}
    
    # Calculate multiplier based on active element properties
    base_multiplier = 1.0
    if active_element in stability and stability[active_element]:
        base_multiplier = 2.0
    elif active_element in stability:
        base_multiplier = 0.75
    
    # Apply final adjustments
    multiplier = base_multiplier * env_modifiers.get(active_element, 1.0)
    
    # This is the statement in question
    final_power = power_levels.get(active_element, 0) * multiplier
    
    # Format output with distracting information
    result_data = {
        "radiation": max_radiation,
        "elements_detected": len(elements),
        "power_output": final_power,
        "stability_index": sum(1 for s in stability.values() if s) / len(stability) if stability else 0
    }
    
    print(f"Result: {int(final_power)}")
    return result_data

# Sample data with encoded element information
raw_data = [0x0612, 0x0645, 0x0678, 0x0690, 0x0612, 0x0623, 0x0645, 0x0690, 0x0612]
result = analyze_elemental_composition(raw_data)