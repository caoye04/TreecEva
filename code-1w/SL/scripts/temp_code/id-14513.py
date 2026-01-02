def evaluate_performance(metrics, exceptions):
    base = sum(metrics)
    penalty = len([x for x in metrics if x < 70])
    adjustment = 0
    
    # Irrelevant computation: tracking unused trend
    trend = [metrics[i+1] - metrics[i] for i in range(len(metrics)-1)]
    avg_trend = sum(trend) / len(trend) if trend else 0
    
    # Distractor: complex lambda that isn't used in final logic
    outlier_detector = lambda val, thresh: abs(val - base / len(metrics)) > thresh
    detected_outliers = [outlier_detector(x, 15) for x in metrics]
    
    # Real logic begins
    stability_bonus = 10 if all(x >= 65 for x in metrics) else 0
    
    # Set operations to filter risk-adjusted metrics
    risky_indices = {i for i, val in enumerate(metrics) if val < 60}
    filtered_metrics = [val for i, val in enumerate(metrics) if i not in risky_indices]
    
    if filtered_metrics:
        performance_mean = sum(filtered_metrics) / len(filtered_metrics)
    else:
        performance_mean = 0
    
    # Secondary distractor: unused transformation
    transformed_data = list(map(lambda x: x * 1.1 if x > 80 else x * 0.9, metrics))
    mean_transformed = sum(transformed_data) / len(transformed_data)
    
    # Core calculation
    raw_score = performance_mean + stability_bonus
    
    # Final adjustment using set intersection (modular arithmetic)
    cycle_days = {1, 3, 5, 7, 9, 11}
    exception_days = {x % 12 for x in exceptions}
    conflict_count = len(cycle_days.intersection(exception_days))
    
    final_score = int(raw_score - (penalty * 5) - (conflict_count * 3))
    return final_score

# Main execution
productivity = [85, 72, 68, 90, 76, 81]
risk_logs = [102, 205, 301]  # Unused variable (distractor)
dummy_calc = [x ** 0.5 for x in productivity if x % 2 == 0]  # Dead code path side-effect

# Key statement
final_score = evaluate_performance(productivity, risk_logs)
print(f"Result: {final_score}")