def sensor_diagnostic():
    raw_readings = [145, 267, 98, 412, 223, 78, 315, 189]
    calibration_offsets = [12, -8, 15, -20, 0, 10, -5, 18]
    status_flags = [True, False, True, True, False, True, True, False]

    # Irrelevant transformation: bit manipulation with no downstream use
    shifted_values = [val >> 2 for val in raw_readings]
    masked_data = [val & 0xFF for val in raw_readings]

    # Actual processing begins
    adjusted_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]
    
    # Distractor: unused helper function
    def smooth_signal(data, factor=0.85):
        smoothed = [data[0]]
        for i in range(1, len(data)):
            smoothed.append(smoothed[-1] * factor + data[i] * (1 - factor))
        return smoothed

    # Another distractor variable
    signal_power = sum([x ** 2 for x in adjusted_readings]) / len(adjusted_readings)

    # Filter valid readings based on status and threshold
    valid_indices = [i for i, flag in enumerate(status_flags) if flag]
    filtered_readings = [adjusted_readings[i] for i in valid_indices]

    # Simulate environmental compensation (only some are used)
    temp_correction = 1.05
    pressure_factor = 0.98
    compensated_readings = [int(x * temp_correction) for x in filtered_readings]

    # Unused dead-end path
    if len(compensated_readings) > 10:
        backup_mode = True
        fallback_score = sum(compensated_readings) // 2
    else:
        backup_mode = False  # This branch executes but isn't critical

    # Key data structures for analysis
    processed_data = {
        'readings': compensated_readings,
        'meta': {'source': 'sensor_array_A', 'version': '2.1'}
    }

    threshold_map = {
        'warning': 250,
        'critical': 350,
        'hysteresis': 25
    }

    # Helper function that is actually used
    def count_exceedances(data_list, warn_limit, crit_limit):
        warn_count = 0
        crit_count = 0
        for val in data_list:
            if val > crit_limit:
                crit_count += 1
            elif val > warn_limit:
                warn_count += 1
        return warn_count, crit_count

    # Main analysis function
    def analyze_readings(data_dict, limits):
        readings = data_dict['readings']
        w, c = limits['warning'], limits['critical']
        warnings, criticals = count_exceedances(readings, w, c)
        
        # Distractor: unused intermediate
        average_reading = sum(readings) / len(readings) if readings else 0
        peak = max(readings) if readings else 0
        
        # Dead code path (never executed due to data size)
        if len(readings) < 3:
            return -999  # emergency fallback

        # Real logic
        base_score = 100
        base_score -= warnings * 15
        base_score -= criticals * 40
        
        # Additional penalty if any reading exceeds critical + hysteresis
        buffer = limits.get('hysteresis', 20)
        if any(r > (c + buffer) for r in readings):
            base_score -= 25
        
        return base_score

    final_diagnostic = analyze_readings(processed_data, threshold_map)
    print(f"Result: {final_diagnostic}")

sensor_diagnostic()