def process_material_data(data_string):
    # Parse material properties from string
    parts = data_string.split('|')
    material_code = parts[0].strip()
    base_resistance = float(parts[1])
    conductivity = float(parts[2])
    oxidation_level = len(material_code) % 3

    # Irrelevant text analysis (distractor)
    vowels = sum(1 for c in material_code.lower() if c in 'aeiou')
    has_repeating_chars = any(material_code[i] == material_code[i+1] for i in range(len(material_code)-1))

    # Determine phase state based on oxidation and resistance
    if oxidation_level > 0 and base_resistance > 50.0:
        phase_state = 2
    elif oxidation_level == 0:
        phase_state = 1
    else:
        phase_state = 0

    # Secondary computation: stability index (not used in final result)
    stability_index = 0
    for i in range(1, 6):
        if i % 2 == 0:
            stability_index += base_resistance / (i * 10)
        else:
            stability_index -= conductivity / (i * 5)

    # Efficiency factor derived from string patterns and numeric values
    efficiency_factor = len(material_code) * 0.1
    if 'X' in material_code.upper():
        efficiency_factor *= 1.25
    if vowels >= 2:
        efficiency_factor *= 0.9  # Slight penalty

    # Core calculation function embedded
    def calculate_thermal_output(eff, phase):
        base = 100.0
        if phase == 2:
            base *= 1.8
        elif phase == 1:
            base *= 1.4
        else:
            base *= 0.9

        # Apply efficiency with non-linear scaling
        adjusted = base * (eff ** 1.1)

        # Red herring: unused conditional branch
        if adjusted > 200:
            adjusted = 200 - (adjusted - 200) * 0.1

        return adjusted

    # Final assignment - target execution point
    thermal_capacity = calculate_thermal_output(efficiency_factor, phase_state)

    # Dead code path (never reached)
    if False:
        backup_value = base_resistance * conductivity
        thermal_capacity = max(thermal_capacity, backup_value)

    # Print result as required
    print(f"Result: {thermal_capacity}")
    return thermal_capacity

# Execute with input
process_material_data("MXA78|75.5|38.2")