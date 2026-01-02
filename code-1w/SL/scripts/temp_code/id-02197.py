def process_readings(data, limits):
    cumulative_score = 0
    anomaly_count = 0
    temporal_flags = set()
    
    for i, reading in enumerate(data):
        base_value = reading // 10
        offset = reading % 7
        adjusted = base_value + offset
        
        if adjusted > limits['high']:
            anomaly_count += 1
            temporal_flags.add(i)
        elif adjusted < limits['low']:
            anomaly_count += 1
            temporal_flags.add(i)
        
        rolling_modifier = (adjusted ^ i) & 3
        cumulative_score += adjusted + rolling_modifier

    # Distractor block: irrelevant transformation
    shadow_buffer = [x * 1.5 for x in data if x % 2 == 0]
    normalization_factor = sum(shadow_buffer) / len(shadow_buffer) if shadow_buffer else 1.0
    normalized_total = int(cumulative_score / (normalization_factor + 1e-8))
    
    # Another distractor: dead logic path
    debug_snapshot = None
    if len(temporal_flags) > 100:
        debug_snapshot = { 'flags': temporal_flags, 'score': normalized_total }
    
    # Real computation continues
    slice_window = data[2:-2] if len(data) > 4 else data
    window_impact = sum(slice_window) // len(slice_window) if slice_window else 0
    
    # Final diagnostic combines relevant state
    final_diagnostic = cumulative_score - (anomaly_count * 10) + window_impact
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input setup
sensor_data = [89, 42, 76, 33, 91, 64, 25, 88, 73, 55, 47, 68, 90, 39, 81]
thresholds = { 'high': 12, 'low': 5 }

# Execute
final_diagnostic = process_readings(sensor_data, thresholds)