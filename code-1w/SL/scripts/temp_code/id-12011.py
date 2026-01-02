def calculate_engine_metrics(sensor_data):
    # Parse sensor input: format 'temp:humid:vib:press'
    values = sensor_data.split(':')
    raw_temp = float(values[0])
    humidity = float(values[1])
    vibration = int(values[2])
    base_pressure = float(values[3])

    # Derived temperature with calibration
    calibrated_temp = raw_temp + 273.15
    adjusted_temperature = calibrated_temp * 0.85 if humidity > 60 else calibrated_temp * 0.9

    # Irrelevant noise: signal degradation simulation (not used in final result)
    signal_loss = 0.0
    for i in range(3):
        if vibration > 50:
            signal_loss += 0.01 * (i + 1)

    # Compression cycle analysis
    cycles = [1.2, 0.9, 1.4, 1.1]
    stable_cycle_found = False
    for c in cycles:
        if abs(c - 1.1) < 0.05:
            stable_cycle_found = True
            break

    compression_factor = 2.3 if stable_cycle_found else 1.8

    # Data mapping for error codes (semi-relevant)
    error_map = {0: 'OK', 1: 'CAL_ERR', 2: 'SENS_OFF'}
    system_status = error_map.get(0, 'UNKNOWN')

    # Red herring: unused pressure transformation
    alt_pressure = base_pressure
    for shift in [0.1, -0.05, 0.02]:
        alt_pressure *= (1 + shift)

    # Key state tracking
    offset = 10 if system_status == 'OK' else 20

    # Critical computation point
    final_pressure = adjusted_temperature * compression_factor + offset

    # Dead code path (never reached due to constant condition)
    if len(error_map) > 10:
        final_pressure *= 0.95

    return final_pressure

# Simulated sensor input
sensor_input = "45:68:55:101.3"
result = calculate_engine_metrics(sensor_input)
print(f"Result: {result}")