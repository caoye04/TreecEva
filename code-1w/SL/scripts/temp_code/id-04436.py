def compute_temperature():
    sensor_readings = {65, 70, 72, 68, 71}
    calibration_offset = 5
    base_temp = sum(sensor_readings) / len(sensor_readings)

    outlier_threshold = 70
    high_readings = {t for t in sensor_readings if t > outlier_threshold}
    low_readings = {t for t in sensor_readings if t <= outlier_threshold}

    adjusted_temp = base_temp - calibration_offset if len(high_readings) > len(low_readings) else base_temp + calibration_offset

    stability_margin = 3
    is_stable = max(sensor_readings) - min(sensor_readings) < stability_margin

    final_temperature = adjusted_temp if is_stable else base_temp * 1.5

    # Irrelevant tracking variable (minimal distraction)
    reading_count = len(sensor_readings)

    print(f"Result: {final_temperature}")

compute_temperature()