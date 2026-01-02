def analyze_network_load():
    # Simulate network node performance under variable load
    base_bandwidth = 42.5
    packet_loss_ratio = 0.03
    jitter_samples = [12, 15, 10, 20, 25, 18, 14]
    avg_jitter = sum(jitter_samples) / len(jitter_samples)

    # Configuration map for different traffic types
    traffic_profile = {
        'video': {'weight': 3.2, 'priority': 1},
        'voice': {'weight': 1.8, 'priority': 2},
        'data': {'weight': 0.9, 'priority': 3}
    }

    # Irrelevant historical metrics (distractor)
    historical_max = 9820
    deprecated_flag = True
    if deprecated_flag:
        legacy_score = historical_max * 0.76

    # Main computation variables
    flow_rate = base_bandwidth * (1 - packet_loss_ratio)
    duration = 120  # seconds
    calibration_factor = 1.08

    # Secondary buffer calculations (partially relevant)
    dynamic_load = traffic_profile['video']['weight'] + traffic_profile['voice']['weight']
    stability_offset = 5 if dynamic_load > 4.0 else 2

    # Surge buffer depends on jitter and stability
    surge_buffer = avg_jitter * stability_offset

    # Key assignment: peak capacity calculation
    capacity = flow_rate * duration + surge_buffer

    # Dead code path (red herring)
    if calibration_factor > 1.1:
        capacity *= 0.95
    elif calibration_factor < 1.05:
        adjustment_log = {'reduction_applied': False}

    # Tracking intermediate state (irrelevant to final result)
    stats_snapshot = {
        'timestamp': 1678886400,
        'node_id': 'NWK-7A',
        'temp_diagnostic': legacy_score if 'legacy_score' in locals() else 0
    }

    # Final result variable
    peak_capacity = int(capacity)

    # Output required format
    print(f"Target result: {peak_capacity}")
    
    return peak_capacity

result = analyze_network_load()