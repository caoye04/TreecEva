def calculate_thermal_output(stages):
    base_efficiency = 0.85
    cumulative_heat = 0
    penalty_factor = 0.92
    auxiliary_counter = 0

    # Misleading pre-computation with dead-end variables
    nominal_loads = [stage['input'] * 1.05 for stage in stages]
    adjusted_outputs = []
    temp_log = {}

    for i, stage in enumerate(stages):
        phase_id = stage['phase']
        input_energy = stage['input']
        duration = stage['time']

        # Real computation branch
        raw_output = input_energy * base_efficiency
        if phase_id > 2:
            raw_output *= 1.15  # Boost for advanced phases

        # Distractor: tracking unused metrics
        efficiency_drop = (base_efficiency - 0.02 * (i % 3)) if i % 4 == 0 else base_efficiency
        dummy_score = raw_output * efficiency_drop
        auxiliary_counter += 1

        # Actual heat accumulation
        heat_contribution = raw_output * duration * 0.78
        cumulative_heat += heat_contribution

        # Use of zip and string method in a semi-relevant context
        status_flag = f"PHASE_{phase_id}".lower()
        if 'early' in status_flag or 'late' in status_flag:
            pass  # Dead logic path

        adjusted_outputs.append((i, heat_contribution))

    # Lambda-based filtering that doesn't affect final result
    valid_stages = list(filter(lambda x: x[1] > 50, adjusted_outputs))
    debug_sum = sum([x[1] for x in valid_stages])  # Unused debugging sum

    # Final calculation using dictionary lookup for obfuscation
    config_map = {'final_multiplier': 1.08}
    thermal_capacity = cumulative_heat * config_map['final_multiplier']

    return thermal_capacity

# Input data setup
process_stages = [
    {'phase': 1, 'input': 120, 'time': 3},
    {'phase': 2, 'input': 140, 'time': 4},
    {'phase': 3, 'input': 160, 'time': 5},
    {'phase': 4, 'input': 180, 'time': 6}
]

# Triggering the key statement
thermal_capacity = calculate_thermal_output(process_stages)

# Print result as required
print(f"Result: {thermal_capacity}")