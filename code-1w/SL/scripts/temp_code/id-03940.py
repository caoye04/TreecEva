def analyze_workload():
    # Simulate a system monitoring workload across multiple servers
    server_loads = [85, 92, 78, 96, 88, 73, 95]
    maintenance_mode = [False, True, False, False, True, False, False]
    thresholds = {'warning': 75, 'critical': 90}

    # Track actual usage excluding maintenance nodes
    usage_tracker = []
    temp_shadow = []  # Distractor: used in irrelevant computation
    scaling_factor = 1.1

    # Precompute scaled values (partially relevant)
    scaled_loads = list(map(lambda x: x * scaling_factor, server_loads))

    # Initialize auxiliary diagnostics (distractor variables)
    diagnostic_log = []
    anomaly_count = 0
    baseline_reference = sum(server_loads) / len(server_loads)

    for i, load in enumerate(server_loads):
        # Irrelevant health check simulation
        health_score = 100 - abs(load - 85)
        diagnostic_log.append((i, health_score))

        # Shadow tracking with no impact on final result
        if health_score < 60:
            temp_shadow.append(load * 0.9)
            anomaly_count += 1  # Dead code path (never reached due to data)

        # Core logic: only include non-maintenance servers
        if not maintenance_mode[i] and load >= thresholds['warning']:
            adjusted_usage = int(load * (1.0 + 0.02 * (load > thresholds['critical'])))
            usage_tracker.append(adjusted_usage)

        # Early return red herring (never triggered)
        if i == 10:  # Impossible index
            return -1

    # Secondary processing: sorting (semi-relevant, but not used directly)
    sorted_diagnostics = sorted(diagnostic_log, key=lambda x: x[1], reverse=True)

    # Critical statement
    peak_capacity = max(usage_tracker)

    # Final print required for execution visibility
    print(f"Result: {peak_capacity}")

    return peak_capacity

analyze_workload()