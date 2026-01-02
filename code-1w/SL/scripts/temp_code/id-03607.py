def analyze_system_performance(loads, thresholds):
    peak_load = max(loads)
    base_threshold = thresholds['critical']
    temp_adjustment = sum([x * 0.1 for x in loads if x > base_threshold])  # Distractor: not used later

    convergence = sum(loads) / len(loads)
    fluctuation = max(loads) - min(loads)

    # Misleading computation path (dead end)
    if fluctuation > 50:
        emergency_mode = True
        fallback_value = 999  # Never used
    else:
        emergency_mode = False

    # Semi-relevant state tracking
    status_flags = {}
    status_flags['high_load'] = peak_load > base_threshold
    status_flags['stable'] = fluctuation < 30

    # Conditional expression with actual relevance
    stability_factor = 1.5 if status_flags['stable'] else 0.7

    # Dummy dictionary operation (distraction)
    metadata_log = {'timestamp': 12345, 'version': '2.1.0', 'debug': False}
    metadata_log['processed'] = True

    # Irrelevant loop (distractor)
    cumulative_noise = 0
    for i in range(3):
        cumulative_noise += i ** 3  # Unused value

    # Key function call embedded in logic
    def calculate_rating(avg, factor):
        raw_score = avg * factor
        penalty = 0.2 * fluctuation if not status_flags['high_load'] else 0.0
        return int(raw_score - penalty)

    final_score = calculate_rating(convergence, stability_factor)
    
    # Print required to expose result
    print(f"Result: {final_score}")

# Input data
workload_readings = [88, 92, 85, 96, 89]
threshold_settings = {'warning': 80, 'critical': 90}

# Execute
analyze_system_performance(workload_readings, threshold_settings)