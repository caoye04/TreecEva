def analyze_workload():
    base_load = 42
    scaling_factor = 1.5
    offset_correction = 7
    
    # Simulated system usage over time (in arbitrary units)
    raw_readings = [30, 45, 50, 55, 60, 58, 62, 70, 68, 75, 73, 80, 85, 90, 88]
    adjusted_readings = [int(x * scaling_factor) + offset_correction for x in raw_readings]
    
    # Historical anomaly buffer (irrelevant to final result)
    anomaly_flags = []
    for val in adjusted_readings:
        if val > 100:
            anomaly_flags.append(True)
        else:
            anomaly_flags.append(False)
    
    # Track rolling utilization (core logic)
    window_size = 5
    usage_traces = []
    for i in range(len(adjusted_readings)):
        if i >= 2:  # Start collecting after warm-up period
            segment = adjusted_readings[i - 2:i + 1]
            avg_load = sum(segment) / len(segment)
            usage_traces.append(int(avg_load))
    
    # Add decoy computation: long-term trend (not used in answer)
    cumulative_drift = 0
    for j in range(1, len(usage_traces)):
        cumulative_drift += usage_traces[j] - usage_traces[j-1]
    long_term_trend = cumulative_drift / (len(usage_traces) - 1) if len(usage_traces) > 1 else 0
    
    # Compute peak observed capacity in recent window
    if len(usage_traces) >= window_size:
        peak_capacity = max(usage_traces[-window_size:])
    else:
        peak_capacity = max(usage_traces) if usage_traces else 0
    
    # Print final target result
    print(f"Target result: {peak_capacity}")

analyze_workload()