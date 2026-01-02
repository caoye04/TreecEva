def system_diagnostic(loads):
    threshold = 75
    overload_events = 0
    temp_buffer = []
    cumulative_stress = 0
    peak_capacity = 0

    for hour, load in enumerate(loads):
        if load > threshold:
            overload_events += 1
            temp_buffer.append(load * 1.2)
        else:
            temp_buffer.append(load * 0.9)

        stress_factor = (load / (threshold + 1)) ** 2
        cumulative_stress += stress_factor

        if load > peak_capacity:
            peak_capacity = load

    # Simulate secondary diagnostics (distractor logic)
    baseline_avg = sum(loads) / len(loads)
    variation = sum((x - baseline_avg) ** 2 for x in loads)
    stability_score = variation / baseline_avg if baseline_avg else 0

    # Irrelevant data transformation
    normalized = list(map(lambda x: round(x / max(loads), 3), loads))
    high_load_periods = [i for i, x in enumerate(normalized) if x > 0.8]

    # Unused nested structure
    stats_summary = {
        'max': max(loads),
        'min': min(loads),
        'overloads': overload_events,
        'stress_index': round(cumulative_stress, 4)
    }

    # Distractor computation with set operations
    unique_loads = set(loads)
    fluctuation_set = set(abs(loads[i] - loads[i-1]) for i in range(1, len(loads)))
    common_anomalies = unique_loads & fluctuation_set  # Not used

    # Conditional expression affecting a red herring
    contingency_plan = 'A' if len(high_load_periods) > 3 else 'B'
    fallback_mode = True if stability_score > 10 else False

    # Key result assignment (critical point)
    final_analysis = {
        'capacity_peak': peak_capacity,
        'event_count': overload_events
    }

    return final_analysis

# Main execution
grid_loads = [65, 70, 80, 92, 68, 77, 85, 90, 74, 88]
system_status = system_diagnostic(grid_loads)
peak_capacity = system_status['capacity_peak']
Result: {peak_capacity}