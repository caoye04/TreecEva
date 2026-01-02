def analyze_performance(metrics, thresholds):
    # Irrelevant pre-processing (distractor)
    normalized = [m / max(metrics) for m in metrics]
    filtered = [m for m in normalized if m > 0.1]
    
    # Core logic: compute weighted score
    weights = [0.2, 0.3, 0.5]
    weighted_sum = sum(m * w for m, w in zip(metrics[:3], weights))
    
    # Secondary computation (partially relevant)
    avg_metric = sum(metrics) / len(metrics)
    deviation = sum(abs(m - avg_metric) for m in metrics)
    stability_score = 100 - deviation
    
    # Red herring: unused function call idea
    def adjust_for_noise(val): return val * 0.98  # never called
    
    # Control flow with misleading branch
    if len(thresholds) > 5:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.0  # this always runs
    
    # Key calculation hidden among distractions
    base_score = weighted_sum * 10
    penalty = 0
    for t in thresholds:
        if t < 50:
            penalty += 5
    final_score = base_score - penalty
    
    # Another distraction: complex but unused list comprehension
    derived_insights = [
        (i, metrics[i] ** 0.5) for i in range(len(metrics))
        if metrics[i] % 2 == 0
    ]
    
    # Critical assignment point
    efficiency_score = int(final_score * adjustment_factor)
    
    # Dead code path (never reached)
    if False:
        efficiency_score *= -1
    
    return efficiency_score

# Simulate execution
metrics_data = [85, 72, 91, 64, 55]
threshold_limits = [88, 70, 95, 40, 60, 58]

result = analyze_performance(metrics_data, threshold_limits)
efficiency_score = result
print(f"Target result: {efficiency_score}")