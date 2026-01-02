import math

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    error_flags = {1: 'OK', 2: 'STABLE', 3: 'CALIBRATED'}
    calibration_offset = 0.87

    # Irrelevant signal smoothing (dead path)
    smoothed = []
    for i in range(len(raw_readings)):
        if i == 0:
            smoothed.append(raw_readings[i])
        else:
            smoothed.append((raw_readings[i] + raw_readings[i-1]) * 0.5)

    # Actual filtering based on prime thresholds
    valid_bounds = set(range(5, 45))
    threshold_set = {x for x in raw_readings if x > 10}

    # Misleading transformation chain
    temp_analysis = {}
    cumulative = 0
    for idx, val in enumerate(raw_readings):
        cumulative += val
        temp_analysis[idx] = math.log(val) if val > 1 else 0
    
    # Fake anomaly detection (distractor)
    anomalies = []
    for k, v in temp_analysis.items():
        if v > 2.5 and k % 2 == 0:
            anomalies.append(k)

    # Real data pipeline
    filtered_data = [x for x in raw_readings if x in valid_bounds]

    # Secondary irrelevant filter (red herring)
    quality_check = [x for x in filtered_data if x % 3 != 0]
    consistency_metric = sum([1 for x in quality_check if x in threshold_set])

    # Core analysis function (uses set operations)
    def analyze_readings(data, thresholds):
        data_set = set(data)
        intersect = data_set.intersection(thresholds)
        exclusive_high = data_set.difference(thresholds)

        # Complex derived metrics
        base_score = sum(intersect) * 0.7
        penalty = len(exclusive_high) * 1.3
        
        # Nested conditional logic with decoy branches
        adjustment = 0
        if len(intersect) > 5:
            adjustment += 10
            if sum(data) % 2 == 0:
                adjustment += 5
            else:
                adjustment -= 3  # Dead path due to data properties
        elif len(data) > 8:
            adjustment += 7
        
        # Final computation with distractor variables
        dummy_weight = math.sin(math.pi / 6)  # Always 0.5, but looks complex
        noise_floor = 0.02 * len(raw_readings)  # Unused constant
        
        result = base_score - penalty + adjustment
        return int(round(result))

    # Execute main logic
    final_diagnostic = analyze_readings(filtered_data, threshold_set)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Unused telemetry dump (distractor)
    telemetry = {
        'version': '2.1.0',
        'nodes': len(raw_readings),
        'flags': error_flags,
        'offset': calibration_offset,
        'consistency': consistency_metric
    }
    
    return final_diagnostic

# Run simulation
collect_diagnostics()