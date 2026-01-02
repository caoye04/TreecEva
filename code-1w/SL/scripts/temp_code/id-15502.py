def sensor_diagnostic(raw_readings, calibration_factor=1.05):
    base_threshold = 37.5
    temp_log = []
    valid_readings = []
    outlier_count = 0
    cumulative_sum = 0

    for reading in raw_readings:
        adjusted = reading * calibration_factor
        if 34.0 <= adjusted <= 42.0:
            valid_readings.append(adjusted)
            cumulative_sum += adjusted
        else:
            outlier_count += 1

    avg_reading = cumulative_sum / len(valid_readings) if valid_readings else 0

    # Distractor: Irrelevant health classification
    if avg_reading < 36.5:
        status = 'Hypothermic'
    elif avg_reading > 37.8:
        status = 'Feverish'
    else:
        status = 'Normal'

    # Real processing begins: transform valid readings
    processed_data = [round(r ** 0.5 * 1.1, 3) for r in valid_readings if r > base_threshold]

    # Distractor: unused transformation
    inverted_data = [1 / (r + 0.1) for r in valid_readings]
    normalized = sum(inverted_data) / len(inverted_data) if inverted_data else 0

    # Threshold logic with set operations (required feature)
    base_set = {i for i in range(45, 56)}
    dynamic_offsets = {int(r % 10) for r in raw_readings}
    threshold_set = base_set | dynamic_offsets  # Union: relevant to final result

    secondary_filter = {x for x in threshold_set if x % 3 == 0}  # Dead code path

    def analyze_readings(data, thresholds):
        if not data:
            return -999
        
        # Conditional expression (required feature)
        scaling = 2.5 if len(data) > 3 else 1.8
        
        total_score = 0
        for val in data:
            int_part = int(val * 100) % 100
            # Simulate diagnostic scoring
            contribution = val * scaling
            if int_part in thresholds:
                contribution *= 1.2
            total_score += contribution
            
            # Nested distraction block (unused)
            if contribution > 50:
                backup_ref = [contribution * 0.1 for _ in range(2)]
                for b in backup_ref:
                    b = b ** 0.1  # No effect

        # Complex but deterministic outcome
        adjustment = len(thresholds.intersection({x for x in range(50, 60)}))
        final_adjusted = total_score - (adjustment * 2.1)
        
        # Red herring: irrelevant warning system
        if final_adjusted > 100:
            alert_code = 'DIAG-101'
        else:
            alert_code = 'OK'
            
        return round(final_adjusted, 4)

    # Unused recursive function (distractor)
    def recursive_smooth(data, depth=0):
        if depth >= 2 or len(data) < 2:
            return data
        return recursive_smooth([0.5 * (data[i] + data[i+1]) for i in range(len(data)-1)], depth+1)

    # Key execution point
    final_diagnostic = analyze_readings(processed_data, threshold_set)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

# Input data (simulated sensor readings)
sensor_input = [36.2, 38.1, 39.5, 41.0, 37.3, 42.5, 35.8]

# Execute main function
diagnostic_result = sensor_diagnostic(sensor_input)