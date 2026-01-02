from itertools import combinations

def analyze_workload(tasks, threshold):
    overload_periods = 0
    cumulative_load = 0
    peak_load = 0
    for load in tasks:
        cumulative_load += load
        if load > threshold * 2:
            overload_periods += 1
        if load > peak_load:
            peak_load = load
    efficiency_penalty = 1 if overload_periods > 3 else 0
    return cumulative_load, peak_load, efficiency_penalty

def generate_task_patterns(base_tasks):
    patterns = []
    for r in range(2, 4):
        for combo in combinations(base_tasks, r):
            patterns.append(sum(combo))
    # Some irrelevant aggregation
    total_combinations = sum(1 for _ in combinations(base_tasks, 2)) + sum(1 for _ in combinations(base_tasks, 3))
    avg_pattern = sum(patterns) / len(patterns) if patterns else 0
    return patterns

def evaluate_stress_factors(metrics, history):
    stress_index = 0
    adjustment_factor = 0.0
    for val in metrics:
        if val > 70:
            stress_index += 1
            adjustment_factor += 0.1
    # Dead code path - never executed due to logic above
    if False and stress_index == 0:
        adjustment_factor = -0.5
    historical_average = sum(history) / len(history) if history else 0
    return stress_index, adjustment_factor, historical_average

def calculate_performance_rating():
    # Core task data
    daily_tasks = [12, 15, 10, 23, 18, 16, 20, 14]
    thresholds = 12
    
    # Step 1: Analyze workload characteristics
    total_load, peak, penalty = analyze_workload(daily_tasks, thresholds)
    
    # Irrelevant derived metric (not used in final score)
    average_load = total_load / len(daily_tasks)
    volatility = sum(abs(daily_tasks[i] - daily_tasks[i-1]) for i in range(1, len(daily_tasks)))
    
    # Step 2: Generate combinatorial task interaction patterns
    pattern_list = generate_task_patterns(daily_tasks[:4])  # Only use first 4 days
    complexity_score = len(pattern_list) * 0.5
    
    # Step 3: Evaluate stress indicators
    stress_metrics = [peak, total_load, complexity_score * 10]
    past_ratings = [65, 70, 68, 72, 75]
    stress_level, adj_factor, hist_avg = evaluate_stress_factors(stress_metrics, past_ratings)
    
    # Step 4: Compute preliminary scores
    base_score = 100 - penalty * 10
    load_adjustment = max(0, 30 - (total_load - 100))  # Cap at 30
    
    # Step 5: Apply conditional modifiers
    if peak > 20 and stress_level >= 1:
        load_adjustment *= 0.8  # Penalty for high peak under stress
    
    # Step 6: Combine into performance rating
    performance_raw = base_score + load_adjustment + complexity_score
    
    # Step 7: Final normalization with floor and ceiling
    final_score = max(50, min(100, performance_raw))
    
    # Extra distraction: unused dictionary aggregation
    summary_stats = {
        'total_tasks': total_load,
        'max_daily': peak,
        'volatility': volatility,
        'pattern_count': len(pattern_list),
        'stress_episodes': stress_level
    }
    
    return final_score

# Execution point
final_score = calculate_performance_rating()
print(f"Result: {final_score}")