def calculate_thermal_capacity(state):
    base_factor = 1.87
    adjustment = 0.13
    temp_sum = 0
    pressure_comp = 0
    
    # Irrelevant sensor readings (distractor variables)
    sensor_noise_1 = 0.002 * state['temperature']
    sensor_noise_2 = 0.005 * state['pressure']
    calibration_offset = sensor_noise_1 + sensor_noise_2 - 0.001
    
    for i, (key, value) in enumerate(state.items()):
        if key == 'temperature':
            temp_sum += value * base_factor
        elif key == 'volume':
            temp_sum += value * 0.04
        elif key == 'pressure':
            pressure_comp = value * adjustment

    # Dead computation branch - never reached due to logic above
    if 'density' in state and state['density'] > 100:
        temp_sum *= 1.05

    # Unused intermediate calculation (red herring)
    theoretical_max = (state['temperature'] * state['volume']) / 1000
    efficiency_ratio = theoretical_max / (temp_sum + 1) if temp_sum else 0

    final_capacity = temp_sum + pressure_comp
    return int(final_capacity)

# System state snapshot from geothermal monitoring
reservoir_state = {
    'temperature': 320,
    'volume': 150,
    'pressure': 86,
    'depth': 2400,
    'material_type': 'basalt'
}

# Intermediate diagnostic values (not affecting result)
diagnostic_checksum = sum([len(k) for k in reservoir_state.keys()])
data_timestamp = '2023-11-05T14:30:00Z'

thermal_capacity = 0
thermal_capacity = calculate_thermal_capacity(reservoir_state)
print(f"Result: {thermal_capacity}")