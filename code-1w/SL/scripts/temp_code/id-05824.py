def evaluate_performance(metrics, base):
    # Irrelevant transformation (distractor)
    temp_normalized = [round((m - min(metrics)) / (max(metrics) - min(metrics)) * 100) for m in metrics]
    
    # Actual relevant logic
    high_perf = {m for m in metrics if m > base}
    medium_perf = {m for m in metrics if m == base}
    
    # Misleading cumulative calculation (semi-relevant)
    cumulative_drift = sum(abs(m - base) for m in metrics)
    drift_penalty = cumulative_drift * 0.1

    # Core logic: performance bonus based on set operations
    exceptional_count = len(high_perf - medium_perf)
    stability_bonus = 5 if len(medium_perf) >= 2 else 0

    # Secondary distractor: unused control flow
    if len(temp_normalized) > 10:
        smoothing_factor = 1.5
    else:
        smoothing_factor = 1.0  # Never used

    # Red herring variable
    theoretical_max = len(metrics) * max(metrics)

    # Key computation
    base_score = sum(high_perf) + stability_bonus
    adjustment = len(high_perf.intersection({x for x in metrics if x > base + 5})) * 3
    final_score = int(base_score - drift_penalty + adjustment)
    
    return final_score

# Baseline configuration (real input)
baseline = 68
raw_metrics = [75, 68, 83, 62, 71, 68, 80, 77, 64]

# Unused data structure (distractor)
legacy_data = [(67, 'A'), (70, 'B'), (63, 'C')]
metric_set = set(raw_metrics)

# Execute main logic
current_system_load = sum([x**2 for x in raw_metrics]) // 1000  # Computed but irrelevant
final_score = evaluate_performance(metric_set, baseline)

print(f"Result: {final_score}")