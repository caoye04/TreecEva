def analyze_workload(tasks, threshold):
    heavy_load_count = 0
    total_complexity = 0
    peak_complexity = 0
    complexity_history = []

    for task in tasks:
        base_load = task.get('base', 1)
        priority_factor = task.get('priority', 1)
        environment_multiplier = task.get('env', 1.0)

        # Irrelevant intermediate computation (distractor)
        adjusted_env = environment_multiplier * 0.95 + 0.05
        temp_debug_value = base_load * adjusted_env

        raw_complexity = base_load * priority_factor
        total_complexity += raw_complexity

        if raw_complexity > peak_complexity:
            peak_complexity = raw_complexity

        if raw_complexity > threshold:
            heavy_load_count += 1

        complexity_history.append(raw_complexity)

    average_complexity = total_complexity / len(tasks) if tasks else 0
    return {
        'total': total_complexity,
        'average': average_complexity,
        'peak': peak_complexity,
        'over_threshold': heavy_load_count,
        'history': complexity_history
    }


def evaluate_efficiency(metrics):
    efficiency_score = 0
    degradation_penalty = 0
    
    # Simulate historical trend analysis (partially unused)
    historical_trend = [metrics['average'] * 0.9, metrics['average'], metrics['average'] * 1.1]
    improvement_rate = historical_trend[2] - historical_trend[0]

    if metrics['peak'] > 25:
        degradation_penalty += 15
    if metrics['over_threshold'] >= 3:
        degradation_penalty += 10

    # Core scoring logic
    efficiency_score = max(100 - metrics['total'] * 0.5, 0)
    efficiency_score -= degradation_penalty

    # Dead code path (distractor)
    if efficiency_score < 0:
        efficiency_score = max(efficiency_score, -5)  # Never reached due to previous max()

    return efficiency_score


def calculate_performance_rating():
    # Real data used in computation
    task_list = [
        {'base': 5, 'priority': 3, 'env': 1.1},
        {'base': 8, 'priority': 4, 'env': 0.9},
        {'base': 6, 'priority': 5, 'env': 1.2},
        {'base': 4, 'priority': 2, 'env': 1.0},
        {'base': 7, 'priority': 3, 'env': 1.3}
    ]

    # Unused dummy data (distractor)
    dummy_tasks = [
        {'base': 20, 'priority': 1, 'env': 0.5},
        {'base': 1, 'priority': 10, 'env': 2.0}
    ]

    workload_metrics = analyze_workload(task_list, threshold=18)
    efficiency = evaluate_efficiency(workload_metrics)

    # Secondary evaluation with conditional expression
    risk_factor = 'high' if workload_metrics['peak'] > 30 else 'medium' if workload_metrics['peak'] > 20 else 'low'
    risk_adjustment = -10 if risk_factor == 'high' else (-5 if risk_factor == 'medium' else 0)

    # Final score calculation
    initial_score = efficiency * 1.1
    final_score = initial_score + risk_adjustment

    # Spurious variable with no impact (distractor)
    normalized_final = round(final_score / 100.0, 3)
    status_flag = 'OPTIMAL' if normalized_final > 0.8 else 'SUBOPTIMAL'

    # Critical output
    print(f"Result: {final_score}")
    return final_score

# Entry point
result = calculate_performance_rating()