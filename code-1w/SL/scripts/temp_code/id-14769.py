def analyze_sensor_data():
    raw_readings = [14, 28, 35, 42, 56, 63, 70, 84]
    calibration_offsets = [2, -1, 3, 0, -2, 1, 4, -3]
    
    # Apply calibration and filter valid signals
    calibrated_signals = []
    for i in range(len(raw_readings)):
        corrected = raw_readings[i] + calibration_offsets[i]
        if corrected % 7 == 0:
            calibrated_signals.append(corrected)
    
    # Irrelevant transformation (distractor)
    squared_temp = [x**2 for x in raw_readings if x > 50]
    average_square = sum(squared_temp) / len(squared_temp) if squared_temp else 0
    
    # Accumulate only high-confidence readings
    high_confidence_sum = 0
    confidence_count = 0
    threshold = 30
    for val in calibrated_signals:
        if val > threshold:
            high_confidence_sum += val
            confidence_count += 1
    
    # Compute moving average (semi-relevant but not used directly)
    window_avg = []
    for i in range(len(calibrated_signals) - 1):
        window_avg.append((calibrated_signals[i] + calibrated_signals[i+1]) / 2)
    
    # Determine adjustment based on pattern analysis
    trend_flags = []
    for idx, (i, val) in enumerate(zip(range(len(window_avg)), window_avg)):
        trend_flags.append(1 if val > 35 else 0)
    
    adjustment_basis = sum(trend_flags)
    adjustment = adjustment_basis * 0.5 if confidence_count > 0 else 0.0
    
    # Main computation path
    base_sum = sum(calibrated_signals)
    adjusted_sum = base_sum + (adjustment * 10)
    
    # Correction factor based on signal stability
    stability_score = 0
    for i in range(1, len(calibrated_signals)):
        if abs(calibrated_signals[i] - calibrated_signals[i-1]) < 15:
            stability_score += 1
    
    correction_factor = stability_score / len(calibrated_signals) if calibrated_signals else 1.0
    
    # Dead code path (distractor)
    outlier_detection = False
    for val in raw_readings:
        if val > 100:
            outlier_detection = True
            break

    # Key statement
    final_flux = adjusted_sum * correction_factor
    
    print(f"Result: {final_flux}")
    
    return final_flux

result = analyze_sensor_data()