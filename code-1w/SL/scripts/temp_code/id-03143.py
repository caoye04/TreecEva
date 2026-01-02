def system_diagnostic(loads, limit):
    stable_count = 0
    overload_events = []
    transient_spikes = 0
    baseline = sum(loads) / len(loads)
    filtered_loads = [load for load in loads if load > baseline * 0.8]
    
    for i, load in enumerate(filtered_loads):
        if load > limit:
            overload_events.append(i)
            if i > 0 and abs(load - filtered_loads[i-1]) > 15:
                transient_spikes += 1
    
    recovery_points = []
    temp_shadow = 0
    for j in range(len(overload_events)):
        if j < len(overload_events) - 1 and overload_events[j+1] - overload_events[j] > 2:
            recovery_points.append(overload_events[j] + 1)
    
    diagnostic_score = len(overload_events) * 2 - transient_spikes
    
    # Irrelevant health check simulation
    health_flags = set()
    for val in loads:
        if val % 7 == 0:
            health_flags.add('node_sync')
        elif val % 5 == 0:
            health_flags.add('clock_drift')
    dummy_metric = len(health_flags) * 1.5
    
    peak_capacity = max(loads) - baseline
    
    if diagnostic_score > 5:
        peak_capacity *= 1.1
    else:
        peak_capacity += 5
    
    final_analysis = int(peak_capacity + dummy_metric)  # dummy_metric doesn't affect logic but looks relevant
    return final_analysis

# Simulated grid load data over 12h
grid_load = [42, 45, 70, 80, 95, 102, 98, 110, 120, 105, 90, 85]
threshold = 90

# Execute diagnostic
final_analysis = system_diagnostic(grid_load, threshold)
Result: {final_analysis}