import itertools

def sensor_diagnostic():
    # Simulated sensor readings (some faulty)
    raw_readings = [102, 105, -999, 108, 103, -999, 110, 107, 104]
    
    # Calibration data from multiple sources (only one is valid)
    calibrations = [
        {'source': 'A', 'value': 0.98, 'status': 'inactive'},
        {'source': 'B', 'value': 1.02, 'status': 'active'},
        {'source': 'C', 'value': 0.95, 'status': 'inactive'}
    ]
    
    # Extract active calibration factor
    active_cal = [c['value'] for c in calibrations if c['status'] == 'active']
    calibration_factor = active_cal[0] if active_cal else 1.0
    
    # Irrelevant: historical averages (not used in final calculation)
    historical_avg = [101.2, 103.5, 102.8, 104.1, 103.0]
    trend_analysis = sum(historical_avg) / len(historical_avg)
    deviation_score = abs(trend_analysis - 103) * 100

    # Filter out invalid readings (-999 = sensor error)
    filtered_data = [r for r in raw_readings if r != -999]
    
    # Distractor: secondary filter that does nothing (dead code path)
    if len(filtered_data) > 10:
        filtered_data = [r for r in filtered_data if r > 100]

    # Add noise simulation (never used)
    noise_profile = list(itertools.accumulate([0.1, -0.2, 0.3, -0.1, 0.05], lambda x, y: x + y))
    enhanced_readings = [r + noise_profile[i % len(noise_profile)] for i, r in enumerate(filtered_data)]  # unused

    # Compute rolling average (distractor)
    window_size = 3
    rolling_averages = [sum(filtered_data[i:i+window_size]) / window_size 
                        for i in range(len(filtered_data) - window_size + 1)]
    stability_index = sum(1 for x in rolling_averages if abs(x - 105) < 2)

    # Unused transformation using zip and enumerate (red herring)
    timestamps = list(range(len(filtered_data)))
    paired_data = list(zip(timestamps, filtered_data))
    indexed_offsets = {i: t * 0.01 for i, t in enumerate(timestamps)}  # not used

    # Real processing function (depends only on filtered_data and calibration_factor)
    def process_readings(data, cal):
        base_avg = sum(data) / len(data)
        calibrated_avg = base_avg * cal
        
        # Additional logic to increase nesting depth
        if calibrated_avg > 100:
            adjustment = 0
            for i, val in enumerate(data):
                if i % 2 == 0:
                    adjustment += 0.1
                else:
                    adjustment -= 0.05
            
            # Complex adjustment (actually negligible)
            final_adj = adjustment / len(data)
            calibrated_avg += final_adj
        
        # Apply non-linear correction (minimal effect)
        correction = (calibrated_avg - 100) ** 2 / 10000
        return round(calibrated_avg + correction, 6)
    
    # Misleading diagnostic flag (irrelevant)
    system_flag = 'OK' if len(filtered_data) >= 5 else 'ERROR'
    diagnostic_log = f'System {system_flag}: Processed {len(filtered_data)} readings'
    
    # Key computation
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Dead code: alternative algorithm never reached
    def deprecated_analysis(seq):
        return sum(x * 0.9 for x in seq if x > 100) % 777
    
    return final_diagnostic

# Execute
sensor_diagnostic()