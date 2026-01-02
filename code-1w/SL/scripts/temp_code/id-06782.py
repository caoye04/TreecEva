def compute_filtration_metrics(input_volume, pressure_levels):
    # Irrelevant pre-processing: thermal compensation not actually used
    ambient_temp = 23.5
    thermal_compensation = sum([ambient_temp / (i + 1) for i in range(5)])
    calibration_offset = 0.07 * input_volume

    # Core variables
    base_yield = 0
    process_efficiency = 0.0
    adjustment_factor = 0
    total_cycles = len(pressure_levels)
    efficiency_log = []

    # Decoy data structure - never accessed
    class SystemState:
        def __init__(self, code, active):
            self.code = code
            self.active = active

    system_states = [SystemState(f'OP-{i}', True) for i in range(total_cycles)]

    # Real logic buried in distractions
    high_pressure_count = 0
    cumulative_stress = 0

    for idx, p in enumerate(pressure_levels):
        if p > 80:
            high_pressure_count += 1
            cumulative_stress += p % 17

        # Actual yield contribution
        if p < 50:
            base_yield += 12.5
        elif p < 75:
            base_yield += 8.2
        else:
            base_yield += 4.1

        # Efficiency logic with early exit red herring
        temp_eff = 0
        if idx % 4 == 0:
            temp_eff = 0.68
        elif idx % 3 == 0:
            temp_eff = 0.74
        else:
            temp_eff = 0.81

        efficiency_log.append(temp_eff)

        # Only last efficiency matters
        if idx == len(pressure_levels) - 1:
            process_efficiency = temp_eff

    # Dead path: never executed due to logic
    final_pressure = pressure_levels[-1] if pressure_levels else 0
    if final_pressure > 1000:
        safety_override = True
        base_yield *= 0.1  # Unused under normal inputs

    # Distractor: complex-looking but unused bitwise operation
    checksum = 0
    for p in pressure_levels:
        checksum ^= int(p) & 0xFF
        checksum = (checksum << 1) | (checksum >> 7)
    metadata_flag = checksum & 0x0F

    # Adjustment based on stress profile - relevant
    stress_ratio = cumulative_stress / total_cycles if total_cycles else 0
    adjustment_factor = high_pressure_count * 3.7 - stress_ratio * 1.2

    # Key computation point
    filtration_yield = process_efficiency * (base_yield + adjustment_factor)

    # More irrelevant state
    audit_trail = {
        'input_volume': input_volume,
        'levels_processed': total_cycles,
        'calibration_used': False,
        'version': '2.1b'
    }

    # Output the required result
    print(f"Result: {filtration_yield}")
    return filtration_yield

# Simulate execution with realistic parameters
pressure_readings = [45, 67, 82, 58, 41, 90, 73, 66]
volume_in_ml = 250

result = compute_filtration_metrics(volume_in_ml, pressure_readings)