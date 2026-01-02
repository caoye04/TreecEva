import math

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [23.4, 18.9, 20.1, 25.6, 17.8, 22.3, 19.0, 24.1]
    calibration_offsets = [0.1, -0.2, 0.05, 0.3, -0.15, 0.0, 0.2, -0.25]
    
    # Irrelevant preprocessing: normalize to z-score (not used in final path)
    mean_raw = sum(raw_readings) / len(raw_readings)
    variance = sum((x - mean_raw) ** 2 for x in raw_readings) / len(raw_readings)
    std_dev = math.sqrt(variance)
    z_scores = [(x - mean_raw) / std_dev for x in raw_readings]  # Dead end

    # Actual signal correction
    corrected_readings = [raw_readings[i] + calibration_offsets[i] for i in range(len(raw_readings))]

    # Decoy transformation: frequency domain analysis (unused)
    freq_components = []
    for k in range(len(corrected_readings)):
        comp = 0
        for n in range(len(corrected_readings)):
            angle = 2 * math.pi * k * n / len(corrected_readings)
            comp += corrected_readings[n] * (math.cos(angle) - 1j * math.sin(angle))
        freq_components.append(comp)  # Not used

    # Real processing begins: filter anomalies
    baseline = sum(corrected_readings) / len(corrected_readings)
    anomaly_flags = [abs(x - baseline) > 2.0 for x in corrected_readings]
    
    # Secondary validation using moving window (partially relevant)
    valid_segments = []
    for i in range(len(corrected_readings) - 2):
        window = corrected_readings[i:i+3]
        if max(window) - min(window) < 3.5:
            valid_segments.append(True)
        else:
            valid_segments.append(False)
    
    # Build confidence map (only some values are used later)
    confidence_map = {}
    for idx in range(len(corrected_readings)):
        conf = 0.9 if not anomaly_flags[idx] else 0.3
        if idx < len(valid_segments) and valid_segments[idx]:
            conf *= 1.1
        confidence_map[f'sensor_{idx}'] = round(conf, 2)

    # Generate metadata tags (irrelevant)
    tags = []
    for i, val in enumerate(corrected_readings):
        if val > 21:
            tags.append(f'high_{i}')
        elif val < 19:
            tags.append(f'low_{i}')
        else:
            tags.append(f'med_{i}')
    # Tags never used again

    # Destructuring assignment with dummy values
    (primary_risk, secondary_risk, _) = (0.8, 0.6, 'placeholder')
    
    # Create threshold map for analysis (used in final step)
    threshold_map = {
        'warning': baseline + 1.8,
        'critical': baseline + 2.8,
        'hysteresis': 0.5
    }

    # Process data through multiple transformations
    processed_data = []
    temp_accumulator = []
    
    for i, val in enumerate(corrected_readings):
        # Complex conditional with red herring logic
        if anomaly_flags[i]:
            adj_val = val * 0.95
            mode_flag = 'A'
        elif i % 2 == 0:
            adj_val = val * 1.02
            mode_flag = 'B'
        else:
            adj_val = val * 1.01
            mode_flag = 'C'

        # Apply artificial time decay (not actually affecting outcome)
        time_weight = math.exp(-0.05 * i)
        weighted_val = adj_val * time_weight  # Distractor

        # Only this line matters in the loop
        temp_accumulator.append({'value': val, 'mode': mode_flag})
    
    # Finalize processed data using list comprehension
    processed_data = [
        {**item, 'index': idx, 'score': item['value'] * 0.75} 
        for idx, item in enumerate(temp_accumulator)
    ]

    # Dummy machine learning model (never called)
    def predict_failure(data):
        return sum(d['score'] for d in data) / len(data) * 0.9
    
    # Unused recursive function to mislead
    def integrate_series(vals, depth=0):
        if depth >= 3 or len(vals) <= 1:
            return vals[0] if vals else 0
        mid = len(vals) // 2
        left = integrate_series(vals[:mid], depth + 1)
        right = integrate_series(vals[mid:], depth + 1)
        return left * 0.6 + right * 0.4

    # Core analysis logic
    def count_above_threshold(data_list, thresholds):
        warning_level = thresholds['warning']
        critical_level = thresholds['critical']
        
        warning_count = 0
        critical_count = 0
        
        for record in data_list:
            orig_val = record['value']
            if orig_val >= critical_level:
                critical_count += 1
            elif orig_val >= warning_level:
                warning_count += 1

        return warning_count, critical_count

    # Another unused helper to increase noise
    def smooth_data(seq):
        if len(seq) < 3:
            return seq
        smoothed = [seq[0]]
        for i in range(1, len(seq)-1):
            smoothed.append((seq[i-1] + seq[i] + seq[i+1]) / 3)
        smoothed.append(seq[-1])
        return smoothed

    # Actual answer computation path
    def analyze_readings(readings, limits):
        w_count, c_count = count_above_threshold(readings, limits)
        
        # Complex weighting formula with dead variables
        factor_a = 1.2
        factor_b = 0.8
        offset_x = 5  # unused
        padding_y = 12 # unused
        
        # Irrelevant bit manipulation distraction
        magic_key = 0
        for i in range(3):
            magic_key ^= (w_count << i) | (c_count >> i)
        magic_key = magic_key & 0xFF  # Truncate to 8 bits

        # Actual result calculation (depends only on counts)
        base_score = w_count * 10 + c_count * 25
        adjustment = int(baseline)  # Uses earlier computed baseline
        final_score = base_score - adjustment
        
        # Additional decoy logic
        if final_score > 100:
            normalized = final_score / 1.5
        else:
            normalized = final_score * 1.1  # Not used
        
        # This is the true answer variable
        diagnostic_code = final_score + 17
        
        return diagnostic_code

    # Execute main logic
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")

    # Return nothing; only side effect is printing
    return None

# Run simulation
collect_diagnostics()