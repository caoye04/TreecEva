def sensor_network_analysis():
    raw_readings = [14.2, 18.5, 12.1, 23.7, 15.3, 17.8, 9.6, 25.1, 13.4, 16.9]
    calibration_offsets = [0.3, -0.2, 0.5, -0.4, 0.1, -0.3, 0.2, -0.1, 0.4, -0.5]
    location_flags = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']
    
    # Irrelevant transformation: location encoding (distractor)
    location_map = {loc: idx for idx, loc in enumerate(set(location_flags))}
    encoded_locations = [location_map[loc] for loc in location_flags]
    
    # Apply calibration (relevant)
    calibrated_readings = [raw + cal for raw, cal in zip(raw_readings, calibration_offsets)]
    
    # Red herring: temperature classification (not used later)
    def classify_temp(val):
        if val < 15: return 'LOW'
        elif val < 20: return 'NORMAL'
        else: return 'HIGH'
    classifications = [classify_temp(r) for r in calibrated_readings]
    
    # Decoy function: never called
    def analyze_trend(data):
        return sum(1 for i in range(1, len(data)) if data[i] > data[i-1])
    
    # Simulate packet loss: filter out every 3rd reading (relevant)
    valid_indices = [i for i in range(len(calibrated_readings)) if (i + 1) % 3 != 0]
    filtered_data = [calibrated_readings[i] for i in valid_indices]
    
    # Dead code path: defines but doesn't use
    stats_snapshot = {
        'mean': sum(filtered_data) / len(filtered_data),
        'min': min(filtered_data),
        'max': max(filtered_data)
    }
    
    # Bit manipulation decoy (irrelevant)
    checksum = 0
    for val in raw_readings:
        int_val = int(val * 10)
        checksum ^= int_val
        checksum = (checksum << 1) & 0xFFFF
    
    # Lambda for dynamic threshold (actually used)
    base_threshold = 16.5
    threshold_func = lambda x: x > (base_threshold + 0.8 if x < 20 else base_threshold - 1.2)
    
    # Core processing function (contains key logic)
    def process_readings(data, threshold_fn):
        triggered = list(map(threshold_fn, data))
        
        # Enumerate with index-based suppression rule (only even indices count)
        active_alarms = [
            flag for idx, flag in enumerate(triggered)
            if flag and idx % 2 == 0
        ]
        
        # String-based status generation (distractor)
        statuses = ['ALERT' if a else 'OK' for a in triggered]
        status_line = ''.join([s[0] for s in statuses]).lower()
        
        # Unused compression simulation
        compressed = ''.join([
            ch.upper() if idx % 2 == 0 else ch 
            for idx, ch in enumerate(status_line)
        ])
        
        # Final diagnostic: count of suppressed alarms (key result)
        total_triggered = sum(triggered)
        effective_triggered = len(active_alarms)
        suppression_rate = total_triggered - effective_triggered
        
        # Diagnostic weight calculation
        weights = [1.1, 0.9, 1.2][:len(data)]  # Truncated to data length
        weighted_sum = sum(w * val for w, val in zip(weights, data))
        
        # Final result combines multiple elements but only suppression_rate is critical
        return int(suppression_rate * 1000 + weighted_sum * 0.1)

    final_diagnostic = process_readings(filtered_data, threshold_func)
    print(f"Result: {final_diagnostic}")

sensor_network_analysis()