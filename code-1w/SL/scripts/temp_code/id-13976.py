def process_sensor_data(raw_values, threshold=0.75):
    # Irrelevant transformation: frequency normalization
    normalized = [x * 0.98 for x in raw_values if x > 0.1]
    
    # Decoy metric: smoothed signal (not used in final result)
    smoothed = []
    for i in range(1, len(normalized) - 1):
        smoothed.append((normalized[i-1] + normalized[i] + normalized[i+1]) / 3)
    
    # Relevant: extract anomalous indices above threshold
    anomaly_indices = [i for i, x in enumerate(raw_values) if x > threshold]
    
    # Distractor: complex but unused Fourier-like approximation
    fourier_proxy = 0.0
    for i, val in enumerate(raw_values):
        fourier_proxy += val * (1 - abs(i - len(raw_values)//2) / len(raw_values))
    
    # Dead code path: simulation of fallback system (never triggered)
    backup_mode = False
    if len(anomaly_indices) == 0 and sum(raw_values) < 2.0:
        backup_mode = True
        surrogate_data = [x ** 0.5 for x in raw_values]

    # Conditional expression: determine confidence level
    confidence = 'high' if len(anomaly_indices) > 2 else 'low'
    
    # Generate metadata with enumerate and zip (partially relevant)
    indexed_raw = list(enumerate(raw_values))
    shifts = [raw_values[i] - raw_values[i-1] for i in range(1, len(raw_values))]
    shift_pairs = list(zip(indexed_raw[1:], shifts))
    
    # Enrich metrics with irrelevant and relevant features
    enriched_metrics = {}
    for idx, val in enumerate(raw_values):
        enriched_metrics[idx] = {
            'value': val,
            'is_anomalous': idx in anomaly_indices,
            'delta': (val - raw_values[idx-1]) if idx > 0 else 0,
            'weight': 1.5 if val > threshold else 0.8,
            'tag': f"A{idx}" if val > threshold else f"B{idx}"
        }
    
    # Unused recursive helper (decoy function)
    def integrate_recursively(data, pos=0):
        if pos >= len(data):
            return 0
        return data[pos] + 0.9 * integrate_recursively(data, pos + 1)
    
    # Real processing begins: analyze readings based on structure
    def analyze_readings(metrics_dict):
        total_weighted = 0.0
        active_count = 0
        
        # Nested logic with multiple conditions
        for k, v in metrics_dict.items():
            if v['is_anomalous']:
                contribution = v['value'] * v['weight']
                if v['delta'] > 0:
                    contribution *= 1.2
                elif v['delta'] < 0:
                    contribution *= 0.85
                total_weighted += contribution
                active_count += 1
        
        # Secondary adjustment based on pattern
        if active_count > 0:
            base_avg = sum(v['value'] for v in metrics_dict.values()) / len(metrics_dict)
            spike_ratio = total_weighted / (base_avg * active_count)
            if spike_ratio > 1.5:
                total_weighted *= 1.1
        
        # Final computation path
        adjustment_factor = 0.95
        for i in range(len(raw_values)):
            if i in anomaly_indices and raw_values[i] > threshold + 0.1:
                adjustment_factor += 0.02
        
        return int(total_weighted * adjustment_factor)
    
    # Key assignment point
    final_diagnostic = analyze_readings(enriched_metrics)
    
    # Red herring: logging unrelated statistics
    stats_summary = {
        'max_normalized': max(normalized) if normalized else 0,
        'smoothed_length': len(smoothed),
        'fourier_proxy': fourier_proxy,
        'confidence_level': confidence
    }
    
    # Output the correct result as required
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execute with realistic sensor input
data_stream = [0.2, 0.85, 0.3, 0.92, 0.78, 1.05, 0.41, 0.68]
result = process_sensor_data(data_stream)