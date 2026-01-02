def analyze_efficiency(metrics):
    adjusted_metrics = [m * 1.1 for m in metrics if m > 5]
    avg_metric = sum(adjusted_metrics) / len(adjusted_metrics) if adjusted_metrics else 0
    return avg_metric * 0.9

# Simulate employee performance data
task_completion = [8, 7, 6, 9, 5, 4, 10]
error_rate = [2, 3, 1, 4, 2, 5, 1]

# Irrelevant distraction: environmental factors (not used in final logic)
ambient_temperature = [22, 23, 21, 24, 22, 20, 23]
humidity_levels = [45, 47, 44, 48, 46, 43, 49]

efficiency_score = analyze_efficiency(task_completion)

# Compute productivity with slicing and conditional expression
recent_tasks = task_completion[-4:]
base_productivity = sum(recent_tasks) / len(recent_tasks)
bonus_applied = True if base_productivity >= 7 else False
productivity = base_productivity * (1.2 if bonus_applied else 1.0)

# Risk factor based on error trends
high_error_days = len([e for e in error_rate if e >= 4])
risk_factor = high_error_days / len(error_rate)

# Distractor computation: unused team averages
team_avg_completion = sum(task_completion) / len(task_completion)
team_avg_errors = sum(error_rate) / len(error_rate)

# Core evaluation logic
def evaluate_performance(prod, risk):
    if risk < 0.3:
        performance_level = 'low_risk'
    elif risk < 0.6:
        performance_level = 'moderate_risk'
    else:
        performance_level = 'high_risk'
    
    # Apply conditional scaling
    adjustment = 1.1 if performance_level == 'low_risk' else (0.95 if performance_level == 'moderate_risk' else 0.8)
    raw_score = prod * adjustment
    
    # Additional irrelevant internal calculation
    volatility = abs(max(task_completion) - min(task_completion))
    stability_bonus = 5 if volatility <= 4 else 0  # Not actually added to score
    
    # Final scoring without the bonus (distractor)
    final_raw = raw_score * 10
    return int(final_raw)

# Critical statement
final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")