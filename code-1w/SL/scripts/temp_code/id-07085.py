def analyze_sensor_network():
    # Simulated IoT sensor data processing with diagnostic logic
    raw_readings = [145, 128, 203, 99, 176, 112, 189, 134, 167, 105]
    calibration_offset = 17
    sample_weights = [0.88, 0.91, 0.85, 0.93, 0.87, 0.90, 0.84, 0.92, 0.89, 0.86]
    
    # Irrelevant baseline stats (distractor)
    avg_reading = sum(raw_readings) / len(raw_readings)
    variance_proxy = sum((x - avg_reading) ** 2 for x in raw_readings)
    peak_noise_floor = max(raw_readings) * 0.1
    
    # Thresholds for anomaly detection (used later)
    threshold_map = {
        'critical': 180,
        'warning': 150,
        'nominal': 120
    }
    
    # Decoy function - never called (dead code path)
    def compute_entropy(values):
        from math import log
        total = sum(values)
        probabilities = [v/total for v in values if v > 0]
        return -sum(p * log(p) for p in probabilities)
    
    # Apply calibration and filter valid range (relevant)
    calibrated = [r + calibration_offset for r in raw_readings]
    valid_range_mask = [130 <= val <= 210 for val in calibrated]
    
    # Conditional expression to flag high-risk sensors
    risk_flags = ['high' if x > threshold_map['critical'] else 'medium' if x > threshold_map['warning'] else 'low' for x in calibrated]
    
    # Filter out-of-range readings using string-encoded status (mixed paradigm)
    status_codes = ['VALID' if m else 'OUTLIER' for m in valid_range_mask]
    filtered_data = [calibrated[i] for i in range(len(calibrated)) if status_codes[i] == 'VALID']
    
    # Spurious dictionary transformation (irrelevant)
    metadata_index = {f'sensor_{i}': {'status': st, 'weight': sample_weights[i]} 
                     for i, st in enumerate(status_codes)}
    
    # Unused intermediate aggregation (red herring)
    weighted_sum = sum(filtered_data[i] * sample_weights[i] for i in range(len(filtered_data)))
    normalization_factor = sum(sample_weights[i] for i in range(len(filtered_data)))
    
    # Real processing begins: categorize and count anomalies
    def process_readings(data, limits):
        categories = {'critical': 0, 'warning': 0, 'nominal': 0}
        for val in data:
            if val > limits['critical']:
                categories['critical'] += 1
            elif val > limits['warning']:
                categories['warning'] += 1
            else:
                categories['nominal'] += 1
        
        # Diagnostic score based on category distribution
        base_score = categories['critical'] * 50 + categories['warning'] * 20 + categories['nominal'] * 5
        adjustment = len(data) % 7  # Modular arithmetic twist
        final_score = base_score - adjustment
        
        # More distraction: unused string formatting
        report_template = "Diagnostic Report: {level} priority - Score {score:.1f}"
        urgency_level = "HIGH" if final_score > 100 else "MODERATE"
        
        return final_score  # This is the real answer source
    
    # Secondary decoy function (never used)
    def generate_diagnostic_chain():
        chain = []
        for i in range(8):
            chain.append((i, i**3 % 11))
        return dict(chain)
    
    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")

# Execute main logic
analyze_sensor_network()