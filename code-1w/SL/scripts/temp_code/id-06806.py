def analyze_workload_efficiency():
    # Simulate a server workload analyzer with resource allocation
    timestamps = [f'2023-12-01T10:{str(m).zfill(2)}:00' for m in range(0, 60, 5)]
    base_load = 45
    fluctuation_pattern = [1.1, 0.9, 1.25, 0.8, 1.15, 0.95, 1.3, 0.7, 1.05, 1.2, 0.85, 1.1]
    
    # Distractor: irrelevant string processing
    status_messages = ['OK', 'STANDBY', 'ACTIVE', 'OVERLOAD']
    system_status = ', '.join([s.lower() for s in status_messages if len(s) > 3])
    heartbeat = system_status.replace(',', '').split(' ')
    heartbeat_cycle = len(heartbeat) * 2

    # Real computation begins
    usage_tracker = {}
    temp_buffer = []
    scaling_factor = 1.0
    
    for i, ts in enumerate(timestamps):
        cycle_index = i % len(fluctuation_pattern)
        raw_usage = base_load * fluctuation_pattern[cycle_index]
        
        # Conditional expression for dynamic scaling (relevant)
        scaling_factor = 1.1 if raw_usage > 55 else (0.95 if raw_usage < 40 else 1.0)
        adjusted_usage = raw_usage * scaling_factor
        
        # Track usage per hour block (all in same hour here)
        hour_key = ts[:13]  # '2023-12-01T10'
        if hour_key not in usage_tracker:
            usage_tracker[hour_key] = 0.0
        usage_tracker[hour_key] += adjusted_usage / len(timestamps)  # distribute evenly

        # Distractor: collect but never used
        temp_buffer.append((ts, adjusted_usage, pow(adjusted_usage, 0.1)))

    # Secondary distractor loop: processes dummy alerts
    alert_levels = ['LOW', 'MEDIUM', 'HIGH']
    for level in alert_levels:
        trigger_threshold = 40 if level == 'LOW' else (50 if level == 'MEDIUM' else 60)
        # This loop doesn't affect final result
        for k in usage_tracker:
            if usage_tracker[k] > trigger_threshold:
                dummy_alert = f"{level}_ALERT at {k}"

    # Key statement
    peak_capacity = max(usage_tracker.values())

    # Additional red herring: unused derived stats
    avg_capacity = sum(usage_tracker.values()) / len(usage_tracker)
    variance = sum((x - avg_capacity) ** 2 for x in usage_tracker.values()) / len(usage_tracker)
    normalized_peak = peak_capacity / (avg_capacity + 1e-5)

    # Output the required result
    print(f"Result: {peak_capacity}")

analyze_workload_efficiency()