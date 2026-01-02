def calculate_thermal_output(phases):
    base_efficiency = 0.87
    cumulative_stress = 0
    thermal_capacity = 0
    stress_factors = [1.1, 0.9, 1.3, 0.8, 1.05]
    efficiency_log = []

    for i, phase in enumerate(phases):
        if i % 2 == 0:
            adjusted_load = phase * base_efficiency
            # Distractor: simulate sensor fluctuation
            sensor_noise = (i + 1) * 0.03
            adjusted_load += sensor_noise if i > 2 else 0
            efficiency_log.append(adjusted_load)
        else:
            # Real computation branch
            transient_load = phase * 1.15
            # Additional distractor variable
            dummy_offset = sum([x * 0.01 for x in range(i)]) if i > 0 else 0
            transient_load -= dummy_offset
            thermal_capacity += transient_load * stress_factors[i % len(stress_factors)]

    # Simulate post-processing calibration (irrelevant to final result)
    calibration_data = [thermal_capacity * 0.98, thermal_capacity * 1.02]
    avg_calibration = sum(calibration_data) / len(calibration_data)
    
    # Key statement
    thermal_capacity = calculate_thermal_output(process_phases)

# Setup input data
process_phases = [23, 45, 67, 89, 12]
baseline_score = sum(process_phases) / len(process_phases)  # Irrelevant metric
auxiliary_matrix = [[i+j for j in range(3)] for i in range(3)]  # Dead code structure

# Entry point
thermal_capacity = 0
target_phase_envelope = [p * 1.05 for p in process_phases]  # Unused preprocessing

thermal_capacity = calculate_thermal_output(process_phases)
print(f'Result: {thermal_capacity}')