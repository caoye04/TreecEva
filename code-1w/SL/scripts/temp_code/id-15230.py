def analyze_employee_performance():
    base_metrics = [87, 92, 78, 90, 85, 93, 88]
    adjustment_factors = [0.95, 1.02, 0.98, 1.05, 0.90, 1.01, 0.99]
    perf_log = [base * factor for base, factor in zip(base_metrics, adjustment_factors)]

    # Irrelevant string processing (distractor)
    status_labels = ['A', 'B', 'C', 'D']
    graded_status = {s: s.lower() + '_pass' for s in status_labels}
    formatted_status = [label.upper().replace('_PASS', '') for label in graded_status.values()]

    # Threshold logic with set operations
    high_performer_threshold = 89.5
    exclusion_zone = {round(x, 1) for x in perf_log if x < 80}
    threshold_set = {x for x in perf_log if x >= high_performer_threshold}

    # Dead code path (not executed but adds cognitive load)
    legacy_scaling = False
    scaling_factor = 0
    if legacy_scaling and scaling_factor > 0:
        perf_log = [x / scaling_factor for x in perf_log]

    # Conditional expression with case conversion (irrelevant to final result)
    mode_flag = 'ADAPTIVE'
    processing_mode = 'strict' if mode_flag.lower() == 'adaptive'.upper() else 'relaxed'

    # Core computation
    def process_performance_data(log, thresholds):
        raw_total = sum(thresholds)
        count = len(thresholds)
        average_boost = raw_total / count if count > 0 else 0

        # Secondary adjustments (some values used, others not)
        peak_bonus = max(log) * 0.05
        floor_penalty = min(log) * 0.02
        adjusted_avg = average_boost + peak_bonus - floor_penalty

        # Final transformation
        normalized = round(adjusted_avg, 2)
        return int(normalized)

    final_score = process_performance_data(perf_log, threshold_set)
    
    # Additional irrelevant computations
    outlier_count = len([x for x in perf_log if x > 100])
    stability_index = sum(1 for i in range(1, len(perf_log)) if perf_log[i] >= perf_log[i-1])

    print(f"Result: {final_score}")

analyze_employee_performance()