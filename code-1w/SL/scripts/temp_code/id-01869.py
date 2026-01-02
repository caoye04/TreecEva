def analyze_sensor_data():
    raw_readings = [23, 45, 67, 12, 89, 34, 56]
    thresholds = { 'low': 30, 'high': 70 }
    
    # Preprocess: filter out-of-bound readings
    filtered_readings = [x for x in raw_readings if thresholds['low'] <= x <= thresholds['high']]
    
    # Compute moving average over window of size 2 (for smoothing)
    smoothed = []
    for i in range(len(filtered_readings) - 1):
        smoothed.append((filtered_readings[i] + filtered_readings[i+1]) / 2)
    
    # Misleading intermediate analysis (not used in final result)
    outlier_count = 0
    for val in raw_readings:
        if val < thresholds['low'] or val > thresholds['high']:
            outlier_count += 1
    temp_adjustment = outlier_count * 1.5  # Dead code path
    
    # Core diagnostic logic
    base_energy = 0
    for val in smoothed:
        base_energy += int(val) ** 2
    
    # Secondary transformation with bit manipulation
    shift_register = 0
    for i, val in enumerate(smoothed):
        shift_register ^= int(val) << (i % 3)
    
    # Auxiliary computation (distractor)
    cumulative_delta = 0.0
    for i in range(1, len(raw_readings)):
        cumulative_delta += abs(raw_readings[i] - raw_readings[i-1])
    stability_index = cumulative_delta / len(raw_readings)  # Not used
    
    # Key variables leading to final answer
    aggregate_score = base_energy // len(smoothed)
    correction_factor = len(filtered_readings) << 2  # Multiply by 4 using bit shift
    mask_value = 0b1111  # Use only lowest 4 bits
    
    # Final diagnostic fusion
    final_diagnostic = aggregate_score + correction_factor & mask_value
    
    print(f"Result: {final_diagnostic}")

analyze_sensor_data()