def calculate_thermal_properties(data):
    base_factor = 1.0
    adjustment = 0.0
    thermal_capacity = 0.0
    legacy_scale = 0.98  # outdated parameter, not used in current logic
    temp_buffer = []

    for index, (material, props) in enumerate(zip(data['names'], data['properties'])):
        conductivity = props['conductivity']
        density = props['density']
        specific_heat = props['specific_heat']

        # Irrelevant intermediate calculation (distractor)
        hypothetical_yield = conductivity * density * 0.02
        temp_buffer.append(hypothetical_yield)

        # Actual relevant computation
        base_factor *= (index + 1) / len(data['names']) if index % 2 == 0 else 1.0

        if conductivity > 200:
            adjustment += 0.1
        elif density > 8000:
            adjustment -= 0.05

        # Core formula
        material_contribution = conductivity * specific_heat * (1 + adjustment)
        thermal_capacity += material_contribution

        # Early exit based on condition (not triggered in this case)
        if index >= 4:
            break

    # Final adjustment using base_factor (only affects result slightly)
    thermal_capacity *= (base_factor + 1)

    # Dead code path (never executed with current input)
    if legacy_scale > 1.0:
        thermal_capacity *= legacy_scale

    return thermal_capacity


# Input data
material_data = {
    'names': ['Copper', 'Aluminum', 'Steel', 'Lead', 'Silver'],
    'properties': [
        {'conductivity': 398, 'density': 8960, 'specific_heat': 0.385},
        {'conductivity': 237, 'density': 2700, 'specific_heat': 0.897},
        {'conductivity': 50, 'density': 7850, 'specific_heat': 0.449},
        {'conductivity': 35, 'density': 11340, 'specific_heat': 0.129},
        {'conductivity': 429, 'density': 10490, 'specific_heat': 0.235}
    ]
}

# Additional irrelevant tracking
processing_log = []
for i, name in enumerate(material_data['names']):
    processing_log.append(f'Processed {name} at stage {i}')

thermal_capacity = calculate_thermal_properties(material_data)
print(f'Result: {thermal_capacity}')