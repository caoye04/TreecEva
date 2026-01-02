def calculate_thermal_output(stages):
    base_efficiency = 0.85
    decay_factor = 0.92
    peak_load = 1200
    thermal_capacity = 0
    efficiency_log = []

    for stage in stages:
        duration = stage.get('duration', 1)
        temperature = stage.get('temp', 300)
        pressure = stage.get('pressure', 1.0)
        mode = stage.get('mode', 'normal')

        # Irrelevant computation (distractor)
        auxiliary_power = duration * 17 % 103
        if auxiliary_power > 50:
            auxiliary_power -= 23

        # Core calculation branch
        if mode == 'boost':
            raw_output = temperature * duration * 1.4
        elif mode == 'eco':
            raw_output = temperature * duration * 0.7
        else:
            raw_output = temperature * duration

        adjusted_output = raw_output * base_efficiency

        # Simulate efficiency decay over stages
        base_efficiency *= decay_factor

        # Accumulate only during high-pressure phases
        if pressure >= 1.5:
            thermal_capacity += adjusted_output

        # Dead code path (misleading)
        if temperature < 250:
            safety_margin = 1.1
        else:
            pass  # Placeholder, no effect

        efficiency_log.append(base_efficiency)

    # Final adjustment based on number of logged efficiencies
    correction_factor = len(efficiency_log) if len(efficiency_log) > 3 else 1.0
    thermal_capacity /= correction_factor

    return int(thermal_capacity)

# Simulation data
process_stages = [
    {'duration': 5, 'temp': 400, 'pressure': 1.6, 'mode': 'normal'},
    {'duration': 3, 'temp': 500, 'pressure': 1.8, 'mode': 'boost'},
    {'duration': 4, 'temp': 350, 'pressure': 1.2, 'mode': 'eco'},
    {'duration': 6, 'temp': 550, 'pressure': 2.0, 'mode': 'boost'},
    {'duration': 2, 'temp': 300, 'pressure': 0.9, 'mode': 'normal'}
]

aux_data = [x['temp'] * 0.01 for x in process_stages]  # Unused variable

thermal_capacity = 0
thermal_capacity = calculate_thermal_output(process_stages)
print(f"Result: {thermal_capacity}")