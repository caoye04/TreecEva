def analyze_workflow():
    # Simulate employee task tracking with mixed metrics
    tasks_completed = [8, 12, 5, 17, 9]
    hours_logged = [40, 38, 40, 42, 36]
    error_count = [3, 7, 1, 11, 4]

    # Irrelevant aggregation (distractor)
    total_hours = sum(hours_logged)
    avg_errors_per_task = sum(error_count) / len(tasks_completed)

    # Productivity per employee (tasks/hour), filtered for efficiency
    productivity = list(map(lambda t_h: round(t_h[0] / t_h[1], 3), zip(tasks_completed, hours_logged)))

    # Misleading secondary metric (not used in final logic)
    precision_ratio = [max(0, (t - e*0.8)/t) if t > 0 else 0 for t, e in zip(tasks_completed, error_count)]

    # Threshold-based categorization (unused path - dead code)
    def classify_efficiency(p):
        return 'High' if p >= 0.3 else 'Low'
    categories = [classify_efficiency(p) for p in productivity]

    # Focus on actual error impact via set filtering
    high_error_indices = {i for i, e in enumerate(error_count) if e > 5}
    low_error_productivity = [p for i, p in enumerate(productivity) if i not in high_error_indices]

    # Compute average productivity excluding high-error workers
    base_performance = sum(low_error_productivity) / len(low_error_productivity)

    # Normalize error count using min-max scaling (semi-relevant)
    min_err, max_err = min(error_count), max(error_count)
    normalized_errors = [(e - min_err) / (max_err - min_err + 0.1) for e in error_count]
    avg_normalized_errors = sum(normalized_errors) / len(normalized_errors)

    # Final evaluation function combining productivity and error trends
    def evaluate_performance(prod_list, err_list):
        raw_score = sum(prod_list) * 100
        penalty = sum(e**2 for e in err_list) * 1.5
        bonus = 10 if len([p for p in prod_list if p > 0.25]) >= 3 else 0
        return int(raw_score - penalty + bonus)

    # Key assignment point
    final_score = evaluate_performance(productivity, error_count)
    
    # Redundant transformation (distractor)
    score_bins = {'low': [], 'medium': [], 'high': []}
    for val in productivity:
        if val < 0.2: score_bins['low'].append(val)
        elif val < 0.3: score_bins['medium'].append(val)
        else: score_bins['high'].append(val)

    # Unused helper function (dead code)
    get_median = lambda lst: sorted(lst)[len(lst)//2]
    median_productivity = get_median(productivity)

    print(f"Result: {final_score}")

analyze_workflow()