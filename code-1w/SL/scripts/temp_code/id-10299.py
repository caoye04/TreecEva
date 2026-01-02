def analyze_system_performance():
    # Simulate sensor readings (temperature, pressure, voltage)
    sensor_data = [
        {'temp': 75.3, 'pressure': 45.1, 'voltage': 3.3},
        {'temp': 82.7, 'pressure': 47.8, 'voltage': 3.1},
        {'temp': 68.9, 'pressure': 44.2, 'voltage': 3.4},
        {'temp': 91.2, 'pressure': 49.5, 'voltage': 2.9}
    ]

    # Thresholds for normal operation
    temp_threshold = 80.0
    pressure_threshold = 48.0
    voltage_threshold = 3.0

    # Derived metrics
    temperature_anomalies = 0
    high_pressure_count = 0
    total_voltage = 0.0
    stability_index = 0.0
    transient_load = 0  # Irrelevant metric (distractor)
    calibration_offset = 1.05  # Unused calibration (dead code)

    # Lambda to compute efficiency penalty
    efficiency_penalty = lambda t, p: 0.1 if t > temp_threshold or p > pressure_threshold else 0.0

    # Accumulators for relevant calculations
    efficiency_deductions = 0.0
    valid_readings = 0
    cumulative_stress = 0  # Semi-relevant, used in intermediate calc only

    stress_factor = 0.0
    for reading in sensor_data:
        temp = reading['temp']
        pressure = reading['pressure']
        voltage = reading['voltage']

        # Anomaly detection
        if temp > temp_threshold:
            temperature_anomalies += 1
        if pressure > pressure_threshold:
            high_pressure_count += 1
            cumulative_stress += pressure * 0.1  # Used only internally

        # Track valid power levels
        if voltage >= voltage_threshold:
            total_voltage += voltage
            valid_readings += 1

        # Apply dynamic penalty using lambda
        efficiency_deductions += efficiency_penalty(temp, pressure)

    # Compute average voltage only from stable systems
    avg_voltage = total_voltage / valid_readings if valid_readings > 0 else 0.0

    # Simulated load balancing (irrelevant computation)
    for i in range(3):
        transient_load += (i + 1) * 5  # Dead logic, not used later

    # Final efficiency model
    base_efficiency = 100.0
    anomaly_penalty = temperature_anomalies * 2.5 + high_pressure_count * 3.0
    voltage_bonus = (avg_voltage - 3.0) * 5 if avg_voltage > 3.0 else 0.0

    # Core formula
    efficiency_score = base_efficiency - anomaly_penalty - efficiency_deductions + voltage_bonus

    # Final data structure
    final_metrics = []
    final_metrics.append(efficiency_score)
    final_metrics.append(stability_index)  # Append unused value

    print(f"Result: {efficiency_score}")

analyze_system_performance()