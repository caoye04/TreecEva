def evaluate_performance(metrics, levels):
    base_score = 0
    penalty_adjustment = 0.0
    temp_result = set()
    
    # Irrelevant metric tracking (distractor)
    historical_data = {"peak": 0, "trough": float('inf')}
    for val in levels:
        if val > historical_data["peak"]:
            historical_data["peak"] = val
        if val < historical_data["trough"]:
            historical_data["trough"] = val
    
    # Core logic: count how many metrics are above threshold
    threshold = 75
    valid_count = 0
    for m in metrics:
        if m >= threshold:
            valid_count += 1
            temp_result.add(m)  # Use of set operation (core)

    # Secondary filter: only consider first three qualifying metrics
    limited_set = sorted(temp_result)[:3]
    
    # Bonus calculation based on size (distraction, not used)
    bonus = len(limited_set) * 10 if len(limited_set) == 3 else 0
    
    # Actual scoring logic
    raw_score = sum(limited_set)
    
    # Apply artificial cap (irrelevant path)
    capped_score = min(raw_score, 200)
    if capped_score > 180:
        penalty_adjustment = 5  # Unused variable
    
    # Final computation
    final_score = raw_score - len(metrics)  # Key formula
    return final_score

# Main execution
metric_set = [88, 92, 76, 63, 95]
benchmark_levels = [50, 85, 77, 90, 60, 82]
interim = sorted(benchmark_levels, reverse=True)
baseline = sum(interim[::2]) / len(interim[::2])

# Critical statement
final_score = evaluate_performance(metric_set, benchmark_levels)
print(f"Result: {final_score}")