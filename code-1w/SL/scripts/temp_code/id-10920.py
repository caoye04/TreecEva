def sensor_network_analysis():
    # Simulated environmental sensor readings (temperature in millidegrees)
    raw_readings = [23450, 25670, 19890, 30120, 27650, 21000, 26780, 24500]

    # Calibration offset due to hardware drift (irrelevant for final result)
    calibration_map = {'sensor_a': 120, 'sensor_b': 87, 'sensor_c': 156}
    adjusted_offsets = {k: v * 0.85 for k, v in calibration_map.items()}

    # Auxiliary function – never called, red herring
    def legacy_filter(data, limit):
        return [x for x in data if x > limit * 1.1]

    # Historical baseline stats (distractor variables)
    historical_avg = sum([22000, 24500, 23000, 26000]) // 4
    variance_buffer = (historical_avg * 0.05) // 1

    # Active filter logic
    valid_range = lambda x: 20000 <= x <= 28000
    filtered_data = list(filter(valid_range, raw_readings))

    # Bit manipulation for checksum (misleading intermediate)
    checksum = 0
    for val in raw_readings:
        checksum ^= (val >> 4) & 0xFF
    checksum = (checksum + len(raw_readings)) % 1000

    # Unused recursive helper – dead code path
    def recursive_compress(seq):
        if len(seq) <= 1:
            return seq[0] if seq else 0
        return recursive_compress([seq[i] + seq[i+1] for i in range(0, len(seq)-1, 2)])

    # String-based metadata processing (irrelevant but plausible)
    node_ids = ['N1', 'N2', 'N3', 'N4', 'N5']
    id_concat = ''.join(node_ids).upper().replace('N', 'X')
    id_summation_key = sum([ord(c) for c in id_concat[:5]]) % 500

    # Core transformation pipeline
    scaling_factor = 0.01  # convert millidegrees to degrees
    scaled_data = [x * scaling_factor for x in filtered_data]

    # Threshold function using closure (key functional element)
    base_threshold = 24.0
    threshold_func = lambda x: x >= (base_threshold + (len(filtered_data) - 2) * 0.5)

    # Real processing function (uses lambda and string method indirectly via filter name)
    def process_readings(data_list, condition):
        # Simulate diagnostic mode
        mode_flag = 'DIAG'.lower().strip()
        high_stress = list(filter(condition, data_list))
        low_stress = [x for x in data_list if not condition(x)]
        
        # Complex aggregation with multiple steps
        stress_score = sum([x * 1.2 for x in high_stress])
        normal_score = sum([x * 0.8 for x in low_stress])
        
        # Final diagnostic calculation
        adjustment = len(high_stress) - len(low_stress)
        raw_diagnostic = stress_score - normal_score + (adjustment * 100)
        
        # Additional red herring: unused transform
        inverted = [round((1000 / x) * 10) / 10 for x in data_list if x > 0]
        
        return int(round(raw_diagnostic))

    # Key execution point
    final_diagnostic = process_readings(scaled_data, threshold_func)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

    # Unused cleanup
    del calibration_map, adjusted_offsets

sensor_network_analysis()