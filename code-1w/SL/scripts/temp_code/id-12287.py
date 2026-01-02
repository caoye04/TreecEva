def analyze_performance(metrics):
    # Irrelevant transformation
    temp_data = {k: v ** 0.5 for k, v in metrics.items() if v > 5}
    adjusted = {}
    for key, value in metrics.items():
        if value >= 8:
            adjusted[key] = value * 1.2
        elif value >= 5:
            adjusted[key] = value * 1.1
        else:
            adjusted[key] = value * 0.9
    
    # Distractor: unused computation
    outlier_count = sum(1 for x in adjusted.values() if x > 10)
    normalized = {k: min(v, 10) for k, v in adjusted.items()}
    
    return normalized

# Simulate intermediate processing
def apply_weighting(data, weights):
    weighted = {}
    for k, v in data.items():
        weight = weights.get(k, 1.0)
        weighted[k] = v * weight
    return weighted

# Core scoring logic
def calculate_final_score(results, multiplier):
    base = sum(results.values())
    count = len([v for v in results.values() if v >= 7])
    
    # Bonus logic with distractor variables
    streak = 0
    max_streak = 0
    for val in results.values():
        if val >= 7:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    
    # Real bonus calculation
    performance_bonus = 5 * (count // 3)
    streak_bonus = 3 * (max_streak // 2)
    total_bonus = performance_bonus + streak_bonus
    
    # Unused but plausible distraction
    penalty = 0
    for val in results.values():
        if val < 5:
            penalty += 2
    
    final = base + total_bonus * multiplier
    return int(final)

# Main execution
if __name__ == '__main__':
    # Input data
    raw_metrics = {'task1': 9, 'task2': 7, 'task3': 4, 'task4': 8, 'task5': 6}
    
    # Step 1: Analyze performance
    processed = analyze_performance(raw_metrics)
    
    # Step 2: Define weights (some irrelevant keys)
    importance_weights = {'task1': 1.1, 'task2': 0.9, 'task4': 1.2, 'task5': 1.0, 'taskX': 0.5}
    scored = apply_weighting(processed, importance_weights)
    
    # Step 3: Prepare final results
    filtered_results = {k: v for k, v in scored.items() if k in ['task1', 'task2', 'task4']}
    
    # Add a missing task artificially
    if 'task3' not in filtered_results:
        filtered_results['task3'] = 3.5  # Not used due to filter above

    bonus_multiplier = 1.5
    final_score = calculate_final_score(filtered_results, bonus_multiplier)
    
    # Print result
    print(f"Result: {final_score}")