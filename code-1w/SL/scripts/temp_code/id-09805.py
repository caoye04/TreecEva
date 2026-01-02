def calculate_thermal_response(temps, phase):
    base_factor = 1.0 if phase == 'solid' else (2.5 if phase == 'liquid' else 4.0)
    adjustment = 0.0
    temp_sum = sum(temps)
    temp_len = len(temps)
    temp_avg = temp_sum / temp_len if temp_len > 0 else 0

    # Distractor block: pressure simulation (not used in final result)
    initial_pressure = 101.3
    pressure_trend = [initial_pressure * (1 + i * 0.05) for i in range(len(temps))]
    stabilized_pressure = pressure_trend[-1] if pressure_trend else 0
    derived_compression = stabilized_pressure ** 0.5  # Unused

    # Real computation path
    fluctuation_score = 0
    for i in range(1, len(temps)):
        diff = abs(temps[i] - temps[i-1])
        fluctuation_score += diff * 0.1

    efficiency_ratio = 0.95 - (fluctuation_score * 0.01)
    efficiency_ratio = max(efficiency_ratio, 0.6)

    # Simulated calibration offset (semi-relevant but overridden)
    calibration_hint = temp_avg * 0.02
    if temp_avg > 500:
        calibration_hint *= 1.5  # Dead code branch due to input

    # Conditional expression (required feature)
    peak_load = max(temps) > 800 else False
    surge_multiplier = 1.3 if peak_load else 1.0

    # Final calculation
    raw_capacity = temp_avg * base_factor * surge_multiplier
    thermal_capacity = raw_capacity * efficiency_ratio

    # Irrelevant post-calculation
    decay_rate = 0.01 * thermal_capacity  # Not used
    projected_cooling = [thermal_capacity * (0.9 ** i) for i in range(5)]  # Dead data

    return thermal_capacity

# Input setup
material_phase = 'solid'
temp_profile = [200, 210, 190, 220, 215, 195, 205]

# Key execution point
thermal_capacity = calculate_thermal_response(temp_profile, material_phase)

print(f"Result: {thermal_capacity}")