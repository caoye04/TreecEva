def sensor_diagnostic_system():
    raw_signals = [145, 267, 180, 99, 210, 305, 112, 88, 177]
    calibration_factor = 0.93
    sample_window = 3
    baseline_offset = 100
    temp_buffer = []
    filtered_data = []
    
    # Irrelevant pre-processing: signal smoothing with unused method
    for i in range(len(raw_signals)):
        smoothed = sum(raw_signals[max(0, i-2):i+1]) / (i+1 if i < 2 else 3)
        temp_buffer.append(round(smoothed * calibration_factor))
    
    # Actual relevant processing: apply baseline correction and detect peaks
    corrected_values = [x - baseline_offset for x in raw_signals]
    peak_indices = [i for i, v in enumerate(corrected_values) if v > 100]
    
    # Simulate data packet formatting (distractor)
    packets = []
    for idx in peak_indices:
        packet = f"PKT|{idx:02d}|{raw_signals[idx]}|CHK"
        packet = packet.replace("PKT", "LOG")  # Unused transformation
        parity_check = packet.count('1') % 2  # Dead code
        packets.append(packet)
    
    # Distractor: frequency analysis on string digits (irrelevant)
    digit_freq = {}
    for p in packets:
        for c in p:
            if c.isdigit():
                digit_freq[c] = digit_freq.get(c, 0) + 1
    sorted_digits = sorted(digit_freq.keys())
    entropy_proxy = len(sorted_digits)  # Not used in final logic

    # Real data path: process readings into diagnostic bands
    processed_data = []
    for val in corrected_values:
        if val < 50:
            processed_data.append('LOW')
        elif val < 150:
            processed_data.append('MID')
        else:
            processed_data.append('HIGH')
    
    # Set operations: determine active categories (using required feature)
    activity_set = set(processed_data)
    expected_set = {'LOW', 'MID', 'HIGH'}
    missing_observations = expected_set - activity_set  # Distractor
    
    # Define thresholds using string-based keys (required string method usage)
    threshold_map = {
        'HIGH'.lower().strip(): 2,
        'MID'.lower().strip(): 4,
        'LOW'.lower().strip(): 1
    }
    
    # Diagnostic engine function (nested inside to increase nesting)
    def analyze_readings(levels, config):
        count_summary = {}
        for level in levels:
            count_summary[level] = count_summary.get(level, 0) + 1
        
        # Apply threshold logic
        score = 0
        for k, v in count_summary.items():
            key = k.lower().strip()
            if key in config:
                if v >= config[key]:
                    score += v * 10
                else:
                    score -= 5
        
        # Bit manipulation red herring
        encoded_score = score ^ 255  # Unused transformation
        normalized = abs(encoded_score) % 100  # Misleading intermediate
        
        # Final decision logic
        if 'HIGH' in count_summary and count_summary['HIGH'] >= config['high']:
            return score + 20
        elif 'MID' in count_summary and count_summary['MID'] >= config['mid']:
            return score + 10
        else:
            return score
    
    # Unused recursive function (dead code path)
    def recursive_energy(acc, depth):
        if depth == 0:
            return acc
        return recursive_energy(acc + (acc % 10), depth - 1)
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

sensor_diagnostic_system()