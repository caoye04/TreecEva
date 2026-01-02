def analyze_system_state():
    # System telemetry data
    base_readings = [0.87, 1.02, 0.93, 1.11, 0.76, 1.24, 0.68]
    thresholds = {"low": 0.85, "high": 1.15}
    
    # Irrelevant historical stats (distractor)
    historical_avg = 0.92
    fluctuation_index = sum(abs(a - b) for a, b in zip(base_readings, base_readings[1:]))
    stability_score = 100 - fluctuation_index * 10

    # Core processing variables
    filtered_readings = [x for x in base_readings if thresholds["low"] <= x <= thresholds["high"]]
    outlier_count = len(base_readings) - len(filtered_readings)
    
    # Simulated node network (mixed structure)
    node_status = {
        'N1': {'active': True, 'priority': 1},
        'N2': {'active': False, 'priority': 3},
        'N3': {'active': True, 'priority': 2},
        'N4': {'active': True, 'priority': 1},
        'N5': {'active': False, 'priority': 2}
    }
    
    # Dead code path - never executed (red herring)
    def legacy_recalibrate(x):
        return (x * 1.05) % 1.3
    
    # Unused transformation (distractor)
    adjusted_readings = list(map(lambda x: x * 1.01 if x < 1.0 else x * 0.99, base_readings))
    
    # Active node processing
    active_nodes = [nid for nid, props in node_status.items() if props['active']]
    priority_sum = sum(node_status[nid]['priority'] for nid in active_nodes)
    
    # Diagnostic computation chain
    baseline_diagnostic = sum(filtered_readings) * 10
    aggregate_score = int(baseline_diagnostic) + outlier_count * 5
    
    # Backup system offset (based on inactive nodes)
    inactive_nodes = set(node_status.keys()) - set(active_nodes)
    backup_offset = len(inactive_nodes) + 1
    
    # Correction factor influenced by conditional logic
    if priority_sum > 3:
        correction_factor = 7
    elif priority_sum == 3:
        correction_factor = 3
    else:
        correction_factor = -2
    
    # Key statement
    final_diagnostic = aggregate_score + correction_factor * (len(active_nodes) - backup_offset)
    
    # Decoy output prints (misleading intermediate values)
    debug_values = {
        'stability_score': round(stability_score, 2),
        'fluctuation_index': round(fluctuation_index, 3),
        'adjusted_mean': round(sum(adjusted_readings)/len(adjusted_readings), 3)
    }
    
    # Redundant set operation (distractor)
    reading_set_a = {round(x, 2) for x in base_readings}
    reading_set_b = {round(x, 2) for x in filtered_readings}
    missing_threshold_crossings = len(reading_set_a - reading_set_b)
    
    return final_diagnostic

result = analyze_system_state()
print(f"Result: {result}")