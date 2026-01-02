import itertools

def preprocess_readings(sensor_array):
    # Irrelevant preprocessing function (dead code path)
    return [x * 1.05 for x in sensor_array if x > 20]

def validate_checksum(data):
    # Misleading validation function (not actually used in critical path)
    checksum = 0
    for d in data:
        checksum ^= d
    return checksum == 0

def calculate_thermal_properties(fluids):
    base_temp = 273.15
    total_weight = 0.0
    effective_heat = 0.0
    entropy_offset = 0.0

    # Distractor variables
    deprecated_flag = False
    legacy_mode = True
    buffer_cache = [0] * 10
    temp_snapshot = []

    for entry in fluids:
        mass = entry['mass']
        temperature_c = entry['temp_c']
        phase_state = entry['phase']

        # Real logic begins: convert to Kelvin and compute contribution
        temp_k = temperature_c + base_temp
        heat_contribution = mass * temp_k * 0.24  # Specific heat approx

        # Distractor: irrelevant phase-based logic with unused branches
        if phase_state == 'solid':
            adjusted_heat = heat_contribution * 0.9
        elif phase_state == 'liquid':
            adjusted_heat = heat_contribution
        elif phase_state == 'gas':
            adjusted_heat = heat_contribution * 1.1
            entropy_offset += mass * 0.05
        else:
            adjusted_heat = heat_contribution

        effective_heat += adjusted_heat
        total_weight += mass

        # Red herring: collecting data not used in final result
        temp_snapshot.append(temp_k)

    # Real computation step
    thermal_index = effective_heat / total_weight if total_weight > 0 else 0

    # Complex distractor block: fake normalization using itertools
    normalization_factors = [1.0, 0.95, 0.98, 1.02, 1.05]
    factor_cycle = itertools.cycle(normalization_factors)
    normalized_values = []
    for i, val in enumerate([effective_heat, total_weight, entropy_offset]):
        normalized_values.append(val * next(factor_cycle))
    # This normalized_values is never used again

    # More decoy logic
    if len(fluids) > 3:
        outlier = max(temp_snapshot) - min(temp_snapshot)
        avg_temp = sum(temp_snapshot) / len(temp_snapshot)
        variance = sum((t - avg_temp) ** 2 for t in temp_snapshot)
        # Unused statistical values

    # Final relevant transformation
    thermal_capacity = round(thermal_index * 1.08, 4)  # Apply system gain

    # Dead assignment: overwritten comment
    # thermal_capacity = 0  # [DEPRECATED] do not uncomment

    return thermal_capacity

# Main execution
if __name__ == '__main__':
    # Simulated sensor data from thermal array
    fluid_data = [
        {'mass': 2.5, 'temp_c': 25.0, 'phase': 'liquid'},
        {'mass': 1.8, 'temp_c': 100.0, 'phase': 'gas'},
        {'mass': 3.2, 'temp_c': -5.0, 'phase': 'solid'},
        {'mass': 0.9, 'temp_c': 75.0, 'phase': 'gas'}
    ]

    # Distractor initialization
    calibration_sequence = [0.1, 0.2, 0.4, 0.8, 1.6]
    system_status = 'ACTIVE'
    debug_mode = False
    audit_log = []

    # Key statement
    thermal_capacity = calculate_thermal_properties(fluid_data)

    # Additional red herring computations
    cumulative_delta = 0
    for i in range(len(calibration_sequence)):
        cumulative_delta += calibration_sequence[i] * 0.1
        audit_log.append(f'Step {i}: {cumulative_delta}')

    # Only this print statement matters
    print(f'Result: {thermal_capacity}')