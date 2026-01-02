import itertools

def sensor_network_analysis():
    # Simulated raw sensor readings (temperature in millidegrees)
    raw_readings = [23450, 25670, 22890, 24100, 26780, 21090, 27800, 19800]
    
    # Irrelevant environmental metadata
    env_metadata = {
        'humidity': [45, 50, 52, 48, 60, 65, 70, 40],
        'pressure': [1013, 1015, 1012, 1010, 1008, 1005, 1003, 1018],
        'wind_speed': [3.2, 4.1, 2.8, 5.0, 6.3, 2.1, 7.0, 1.8]
    }
    
    # Decoy processing function (never called)
    def analyze_humidity(data):
        return sum(x * 0.1 for x in data if x > 50)
    
    # Calibration parameters (some are red herrings)
    base_offset = 127
    gain_factor = 1.02
    noise_threshold = 20000
    decay_rate = 0.98
    calibration_factor = (base_offset * gain_factor) / 1.5
    
    # Misleading intermediate transformation
    adjusted_by_pressure = [temp - (press - 1000) for temp, press in zip(raw_readings, env_metadata['pressure'])]
    
    # Real signal filtering: remove outliers below threshold
    filtered_data = list(filter(lambda x: x > noise_threshold, raw_readings))
    
    # Dead code path - never executed due to condition
    if len(raw_readings) < 5:
        fallback_value = sum(raw_readings) // len(raw_readings)
        filtered_data.append(fallback_value)
    
    # Apply decay simulation over multiple iterations (distractor)
    temp_state = raw_readings.copy()
    for i in range(3):
        temp_state = [int(x * decay_rate) for x in temp_state]
    final_state_snapshot = temp_state  # Unused later
    
    # Real processing begins here
    def process_readings(data, calib):
        # Compute rolling difference using itertools
        paired = list(itertools.pairwise(data))
        diffs = [abs(b - a) for a, b in paired]
        
        # Add calibration offset to median difference
        sorted_diffs = sorted(diffs)
        mid_idx = len(sorted_diffs) // 2
        median_diff = (sorted_diffs[mid_idx] + sorted_diffs[~mid_idx]) // 2
        
        # Apply non-linear correction
        corrected_median = int(median_diff * 1.25)
        
        # Use lambda for dynamic thresholding
        threshold_func = lambda x: x > (corrected_median * 0.8)
        high_variation_count = sum(1 for d in diffs if threshold_func(d))
        
        # Combine with calibration factor through bit manipulation
        calibrated_component = int(calib) & 0xFF  # Take lower 8 bits
        variation_component = high_variation_count << 4
        
        # Final diagnostic code: XOR combination
        result = calibrated_component ^ variation_component ^ 0xAA
        
        # Dead branch based on impossible condition
        if sum(diffs) < 0:
            result = result * 2  # Never reached
            
        return result
    
    # Secondary decoy function using dictionary operations
    def generate_diagnostics_log(data_dict):
        log_entries = []
        for k, v in data_dict.items():
            entry = f"{k}:{len(v)}" if len(v) % 2 == 0 else f"{k}:N/A"
            log_entries.append(entry)
        return '|'.join(log_entries)
    
    # Generate unused log
    _ = generate_diagnostics_log(env_metadata)
    
    # Key execution point
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

# Execute function
sensor_network_analysis()