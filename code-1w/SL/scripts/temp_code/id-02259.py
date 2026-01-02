def analyze_filtration_process(raw_data, threshold=0.5):
    # Simulate sensor readings from a water filtration system
    sensor_readings = [x / 1000 for x in raw_data]

    # Normalize data using z-score (distractor computation)
    mean_val = sum(sensor_readings) / len(sensor_readings)
    variance = sum((x - mean_val) ** 2 for x in sensor_readings) / len(sensor_readings)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_val) / std_dev for x in sensor_readings]  # Not used later

    # Identify critical filters based on pressure differential
    pressure_deltas = []
    for i in range(1, len(sensor_readings)):
        delta = sensor_readings[i] - sensor_readings[i-1]
        pressure_deltas.append(abs(delta))

    # Assign health weights to each filter stage
    health_weights = []
    for val in sensor_readings:
        if val < threshold:
            weight = 1
        elif val < threshold * 2:
            weight = 2
        elif val < threshold * 3:
            weight = 3
        else:
            weight = 4
        health_weights.append(weight)

    # Apply maintenance flag logic (semi-relevant)
    maintenance_needed = [w >= 3 for w in health_weights]
    flagged_stages = sum(maintenance_needed)

    # Compute cumulative stress index (distractor)
    stress_index = 0
    for i, p in enumerate(pressure_deltas):
        stress_index += p * (i + 1)  # Weighted accumulation

    # Filter stages with adequate flow rate
    flow_rates = [x * (1 + 0.1 * w) for x, w in zip(sensor_readings, health_weights)]
    valid_flow_mask = [f > 0.4 for f in flow_rates]

    # Final assessment: weight only those above internal efficiency threshold
    efficiency_flags = [f > 0.45 for f in flow_rates]
    filtered_weights = [w for w, e in zip(health_weights, efficiency_flags) if e]

    # Key statement
    filtration_score = sum(filtered_weights)

    # Dead code path (never executed but looks relevant)
    if False:
        backup_score = sum(health_weights) / len(health_weights)
        log_entry = f"Fallback: {backup_score:.2f}"

    # Print result as required
    print(f"Result: {filtration_score}")

    return filtration_score

# Input data representing raw sensor values in millibars
raw_input = [320, 480, 610, 390, 720, 510, 290]

# Execute function
calculate_result = analyze_filtration_process(raw_input)