def compute_performance():
    # Sensor readings over time (simulated)
    sensor_readings = [23.5, 19.8, 45.2, 37.1, 29.3, 41.0, 33.7]

    # Irrelevant auxiliary data (minimal distraction)
    device_id = "SNSR-7A"
    calibration_offset = 0.15

    # Compute rolling averages over windows of 3
    averages = []
    for i in range(len(sensor_readings) - 2):
        avg = sum(sensor_readings[i:i+3]) / 3
        averages.append(round(avg, 2))

    # Scaling factor based on system gain
    scaling_factor = 1.2

    # Key computation step
    final_score = max(averages[1:4]) * scaling_factor

    # Output result
    print(f"Result: {final_score}")

compute_performance()