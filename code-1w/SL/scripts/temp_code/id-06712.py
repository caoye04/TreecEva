def main():
    # Simulate time-series sensor readings for system load
    raw_readings = [120, 135, 128, 142, 150, 148, 160, 175, 180, 178, 170, 165]

    # Irrelevant transformation: normalize to percentage (not used in final logic)
    max_reading = max(raw_readings)
    normalized = [x / max_reading for x in raw_readings]
    avg_normalized = sum(normalized) / len(normalized)

    # Slice only the critical period for analysis
    critical_window = raw_readings[3:9]

    # Track cumulative stress with a lambda-based accumulator
    accumulate_stress = lambda data, base: [base := base + x for x in data]
    stress_levels = accumulate_stress(critical_window, 0)

    # Misleading intermediate calculation: peak-to-average ratio (unused)
    peak_to_avg_ratio = max(critical_window) / (sum(critical_window) / len(critical_window))

    # Boolean filtering: detect over-threshold events
    threshold_limit = 140
    threshold_func = lambda x: x > threshold_limit
    overflow_events = list(filter(threshold_func, critical_window))

    # Count sequences with rising trend (consecutive increases)
    rising_trends = 0
    for i in range(1, len(critical_window)):
        if critical_window[i] > critical_window[i-1]:
            rising_trends += 1

    # Distractor: simulate unrelated temperature drift (dead computation)
    temp_drift = 0.0
    for step in range(5):
        temp_drift += 0.1 * step
        if temp_drift > 1.0:
            temp_drift = 1.0
            break

    # Core logic: find maximum sustained capacity in window
    running_average = sum(critical_window) / len(critical_window)
    peak_capacity = max(stress_levels)  # This accumulates raw sum, so last element is total sum

    # Final analysis uses filter and lambda but doesn't alter peak_capacity
    def analyze_trends(log, condition):
        high_load = list(filter(condition, log))
        duration = len(high_load)
        intensity = sum(high_load) if duration > 0 else 0
        return {'duration': duration, 'intensity': intensity}

    final_analysis = analyze_trends(capacity_log=critical_window, threshold_func=threshold_func)

    # Output target result
    print(f"Result: {peak_capacity}")

if __name__ == "__main__":
    main()