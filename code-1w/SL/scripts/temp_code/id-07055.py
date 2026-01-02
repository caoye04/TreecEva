def analyze_system_metrics():
    # Simulated sensor readings from a distributed monitoring system
    raw_readings = [145, 267, 198, 87, 211, 305, 176, 94]
    
    # Irrelevant calibration constants (distractor)
    calib_factor_a = 0.987
    calib_offset_b = -4.2
    temp_reference = 25.0

    # Normalize readings using min-max scaling (partially relevant)
    min_val, max_val = min(raw_readings), max(raw_readings)
    normalized = [(x - min_val) / (max_val - min_val) for x in raw_readings]

    # Weighted contribution calculation with enumeration (relevant)
    weights = [0.1, 0.2, 0.15, 0.05, 0.25, 0.1, 0.08, 0.02]
    weighted_sum = sum(norm * w for norm, w in zip(normalized, weights))

    # System health baseline with decoy computations
    baseline_threshold = 0.7
    fluctuation_index = (max_val - min_val) / len(raw_readings)
    stability_score = 100 - fluctuation_index  # Unused metric (red herring)

    # Conditional adjustment based on pattern detection
    rising_trend = 0
    for i in range(1, len(raw_readings)):
        if raw_readings[i] > raw_readings[i-1]:
            rising_trend += 1
    
    # Trend bias factor (only used if trend is strong)
    trend_bias = rising_trend * 1.5 if rising_trend > 5 else 0.0  # Dead code path

    # Aggregate pre-diagnostic index
    aggregate_health_index = int((weighted_sum * 1000) + 50)

    # Environmental interference simulation (irrelevant block)
    interference_mask = 0
    for bit in range(8):
        interference_mask |= (1 << bit) if bit % 3 == 0 else 0
    noise_correction = bin(interference_mask).count('1')

    # System configuration profile
    config_flags = {'redundancy': True, 'failover': False, 'debug_mode': True}
    active_modules = sum([config_flags[k] for k in config_flags])

    # Final computation chain
    system_weight = len([x for x in raw_readings if x > 150])  # Count high-load sensors
    
    # Key statement: final diagnostic calculation
    final_diagnostic = aggregate_health_index // system_weight
    
    # Decoy output variables (misleading)
    avg_normalized = sum(normalized) / len(normalized)
    peak_contribution = max(zip(weights, normalized), key=lambda x: x[0]*x[1])

    # Output target result
    print(f"Result: {final_diagnostic}")

analyze_system_metrics()