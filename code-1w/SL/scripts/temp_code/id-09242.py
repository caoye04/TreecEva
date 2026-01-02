def analyze_sensor_data(readings):
    # Irrelevant preprocessing: normalize readings (not used in final calculation)
    normalized = [r / max(readings) for r in readings]
    threshold = 0.5 * sum(normalized)

    # Semi-relevant transformation: apply logarithmic scaling (partially distractor)
    log_scaled = list(map(lambda x: round(x * 100, 2), normalized))

    # Core logic: compute weighted phase shifts based on sensor position
    weights = [1, -2, 3, -1, 2]
    weighted_values = []
    for i, val in enumerate(readings):
        if i % 2 == 0:
            adjusted = val + (val * 0.1)  # Small adjustment for even indices
        else:
            adjusted = val - (val * 0.05)  # Slight reduction for odd indices
        weighted_values.append(adjusted * weights[i % len(weights)])

    # Accumulate phase contributions with modular correction
    total_phase = 0
    for wv in weighted_values:
        total_phase += int(wv) % 7  # Modular arithmetic with accumulation

    # Distractor: unused complex computation involving lambda and filtering
    anomalies = list(filter(lambda x: x > 1.5, normalized))
    anomaly_score = sum(anomalies) * 100 if anomalies else 0  # Not used later

    # Secondary distractor: simulate calibration offset (never applied)
    calibration_map = {i: (i**2 % 97) for i in range(len(readings))}
    dummy_offset = sum(calibration_map.values()) // len(calibration_map)

    # Key function definition embedded to increase nesting and cognitive load
    def calculate_net_flux(data):
        base = sum(data)
        modifier = 1
        if base > 50:
            modifier = 2
        elif base < 30:
            modifier = 0.5
        
        # Real answer depends on accumulated phase mod 100
        flux_component = total_phase % 100
        return int(flux_component * modifier)

    # Execution point of interest
    final_flux = calculate_net_flux(readings)
    return final_flux

# Simulated sensor readings from experimental array
readings_input = [8, 15, 12, 9, 14]

# Execute and print result
result = analyze_sensor_data(readings_input)
print(f"Target result: {result}")