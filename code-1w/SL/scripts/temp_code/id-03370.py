def analyze_sensor_network():
    # Simulated sensor readings (temperature in millidegrees)
    raw_readings = [23450, 25670, 22890, 27800, 21000, 24300, 26750, 28100, 20500, 23900]
    
    # System thresholds and calibration offsets
    critical_temp = 27500
    calibration_matrix = [1.02, 0.98, 1.01, 0.99, 1.03]
    baseline_adjustment = 20000
    decay_factor = 0.85

    # Irrelevant auxiliary data (distractor)
    maintenance_logs = ['OK', 'REPLACE_FAN', 'OK', 'CLEAN_SENSOR', 'OK']
    last_recalibration = "2023-10-05"
    device_status = {"sensors": 10, "active": 8, "faulty": 2}

    # Apply baseline correction (real processing step)
    corrected_readings = [r - baseline_adjustment for r in raw_readings]

    # Outlier detection using moving average (mixed relevance)
    window_size = 3
    smoothed = []
    for i in range(len(corrected_readings)):
        if i < window_size:
            window = corrected_readings[:i+1]
        else:
            window = corrected_readings[i-window_size+1:i+1]
        smoothed.append(sum(window) / len(window))

    # Filter readings above threshold (relevant)
    threshold = 5500
    high_readings = [v for v in corrected_readings if v > threshold]
    filtered_data = [x for x in high_readings if x < 7000]  # Narrow valid band

    # Decoy transformation chain (mostly irrelevant)
    transformed_chain = []
    temp_val = 1000
    for _ in range(5):
        temp_val = int(temp_val * decay_factor + 50)
        transformed_chain.append(temp_val)
    final_transform = transformed_chain[-1] if transformed_chain else 0

    # Real processing function (nested logic)
    def process_readings(data, limit):
        if not data:
            return -1
        
        # Bit manipulation for diagnostic signature (relevant)
        aggregate = 0
        for val in data:
            shifted = (val >> 4) & 0xFF
            aggregate ^= shifted
            
        # Conditional expression with slicing (required Python feature)
        category = 'CRITICAL' if any(x > 6500 for x in data) else 'ELEVATED'
        slice_offset = 1 if category == 'CRITICAL' else 0
        segment = data[slice_offset:]
        
        # Secondary computation with modular arithmetic (relevant)
        checksum = 0
        for i, v in enumerate(segment):
            checksum += (v * (i + 1)) % 97
        
        # Final diagnostic combines bit-aggregate and checksum
        diagnostic_code = (aggregate * 1000) + (checksum % 1000)
        
        # Dead code path (distractor)
        if diagnostic_code < 0:
            backup_system = True
            for _ in range(3):
                backup_system = not backup_system
            return -999
            
        return diagnostic_code

    # Unused but plausible function (red herring)
    def compute_stability_index(logs, status):
        uptime_score = status["active"] * 10
        error_count = logs.count('REPLACE_FAN') + logs.count('CLEAN_SENSOR')
        return uptime_score - (error_count * 15)

    # Unused variable (distractor)
    stability_rating = compute_stability_index(maintenance_logs, device_status)

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold)

    # Print result as required
    print(f"Result: {final_diagnostic}")

    # Additional irrelevant operations (misleading intermediate results)
    cumulative_power = 0
    for i in range(len(transformed_chain)):
        cumulative_power += transformed_chain[i] ** 2
    energy_metric = cumulative_power // 1000

    return final_diagnostic

# Execute and capture result
result = analyze_sensor_network()