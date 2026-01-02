def sensor_calibration():
    base_signal = 23.5
    offset = -7.2
    gain = 1.8

    # Initial calibration adjustment
    calibrated_signal = (base_signal + offset) * gain

    # Environmental compensation factor
    temperature_factor = 0.95
    humidity_compensation = 1.02

    adjusted_energy = calibrated_signal * temperature_factor * humidity_compensation

    # Define dynamic correction using lambda
    final_adjustment = lambda x: x * 0.98 + 5.4 if x > 30 else x * 1.05 - 2.1

    energy_threshold = final_adjustment(adjusted_energy)

    # Irrelevant telemetry log (minimal distraction)
    telemetry_log = {'status': 'ok', 'ignored_value': 999}

    return energy_threshold

result = sensor_calibration()
print(f"Result: {result}")