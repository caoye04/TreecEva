def sensor_fusion_calibration(readings):
    baseline_offset = 17
    temp_cache = []
    diagnostic_log = []
    
    for reading in readings:
        raw_value = reading['value']
        sensor_type = reading['type']
        timestamp = reading['ts']
        
        # Irrelevant temperature compensation (dead path)
        if sensor_type == 'TMP':
            compensated = raw_value + baseline_offset
            temp_cache.append(compensated)
            continue
        
        # Real processing starts here (hidden among distractions)
        normalized = raw_value / 100.0
        quality_flag = 1 if normalized > 0.5 else 0
        
        # Misleading intermediate calculation (red herring)
        dummy_score = (normalized ** 2) * 0.9 + 10
        
        # Actual signal used later
        if normalized < 0.3:
            diagnostic_log.append(1)
        elif normalized > 0.7:
            diagnostic_log.append(2)
        else:
            diagnostic_log.append(0)
    
    # Decoy function call with no side effects
    def analyze_trend(log):
        return sum(log) / len(log) if log else 0
    
    trend_index = analyze_trend(temp_cache)  # Uses wrong data
    
    # Key logic buried in conditional expression
    primary_count = sum(1 for x in diagnostic_log if x == 2)
    secondary_count = sum(1 for x in diagnostic_log if x == 1)
    adjustment_factor = 0.85 if primary_count > secondary_count else 1.15
    
    # Critical aggregation with min/max and conditional logic
    aggregated = sum(diagnostic_log) * adjustment_factor
    
    # Final transformation using average pattern
    average_diagnostic = aggregated / len(diagnostic_log) if diagnostic_log else 0
    
    # Red herring: unused complex structure
    metadata_summary = {
        'version': '2.1',
        'calibration_mode': 'full',
        'checksum': (baseline_offset * 37) % 256
    }
    
    # Final answer computed via indirect route
    emergency_override = False
    override_threshold = 1.5 if emergency_override else 3.0
    final_diagnostic = average_diagnostic if average_diagnostic <= override_threshold else override_threshold
    
    # Print required at end
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data (deterministic)
data_stream = [
    {'value': 120, 'type': 'TMP', 'ts': 1001},
    {'value': 85, 'type': 'PRX', 'ts': 1002},
    {'value': 20, 'type': 'PRX', 'ts': 1003},
    {'value': 90, 'type': 'PRX', 'ts': 1004},
    {'value': 65, 'type': 'PRX', 'ts': 1005},
    {'value': 15, 'type': 'PRX', 'ts': 1006},
    {'value': 95, 'type': 'PRX', 'ts': 1007}
]

# Entry point
final_diagnostic = sensor_fusion_calibration(data_stream)