def analyze_metrics(raw_data):
    # Preprocess sensor readings
    cleaned = [x for x in raw_data if x > 0]
    baseline = sum(cleaned) / len(cleaned)
    
    # Compute derived metrics
    squared_devs = [(x - baseline) ** 2 for x in cleaned]
    variance = sum(squared_devs) / len(squared_devs)
    stdev = variance ** 0.5

    # Threshold filtering (distractor computation)
    outlier_count = 0
    temp_sum = 0
    for val in cleaned:
        if abs(val - baseline) > 2 * stdev:
            outlier_count += 1
        temp_sum += val * 0.1  # Irrelevant accumulation

    # Generate metric set using set operations
    high_perf = {x for x in cleaned if x >= baseline + stdev}
    low_perf = {x for x in cleaned if x <= baseline - stdev}
    metric_set = high_perf - low_perf  # Meaningful difference

    # Auxiliary debugging trace (dead code path)
    debug_snapshot = None
    if False:  # Simulated condition, never executed
        debug_snapshot = {
            'raw_len': len(raw_data),
            'outliers': outlier_count,
            'temp_avg': temp_sum / len(cleaned)
        }

    # Core evaluation logic
    def evaluate_performance(metrics):
        if not metrics:
            return 0
        primary_score = sum(metrics) / len(metrics)
        
        # Secondary adjustment based on distribution
        sorted_vals = sorted(metrics)
        median_val = sorted_vals[len(sorted_vals) // 2]
        adjustment = abs(primary_score - median_val) * 0.1
        
        # Final scoring with artificial complexity
        score_pool = set()
        for v in sorted_vals:
            score_pool.add(int(v))
        pool_influence = len(score_pool) * 0.05
        
        final_score = primary_score - adjustment + pool_influence
        return int(final_score)  # Discrete result

    # Execute evaluation
    intermediate_flag = len(high_perf) > len(low_perf)  # Unused flag
    scaling_factor = 1.0
    for _ in range(2):
        scaling_factor *= 0.95  # Decay with no impact

    final_score = evaluate_performance(metric_set)
    print(f"Result: {final_score}")

# Simulated input data from system telemetry
data_stream = [85, 90, 78, 92, 88, 76, 95, 87, 83, 91, 77, 89]
analyze_metrics(data_stream)