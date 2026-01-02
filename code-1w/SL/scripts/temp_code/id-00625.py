def evaluate_performance(output, risk_profile):
    base_score = 100
    adjustment = 0
    
    # Irrelevant computation: historical average (not used in final logic)
    historical_avg = sum([95, 87, 92, 88, 90]) / 5
    temp_offset = 5 if historical_avg > 90 else 0  # Distractor
    
    # Lambda for dynamic threshold (used)
    threshold_func = lambda x: x * 0.75
    
    high_threshold = threshold_func(100)
    
    # Set operations: identify risky and safe tasks
    all_tasks = set(range(1, 21))
    risk_set = {3, 6, 9, 12, 15, 18}
    safe_tasks = all_tasks - risk_set
    
    # Simulate partial completion using intersection
    completed_tasks = {2, 4, 6, 7, 10, 11, 14, 15, 19}
    successful_safe = completed_tasks & safe_tasks  # Only safe and completed
    
    productivity = len(successful_safe)
    
    # Core scoring logic
    if productivity > high_threshold:
        adjustment += 15
    elif productivity >= 5:
        adjustment += 5
    else:
        adjustment -= 10
    
    # Risk penalty: count how many risk tasks were completed
    risky_completion = len(completed_tasks & risk_set)
    risk_penalty = risky_completion * 2
    
    # Dead code path (never executed due to constant condition) — red herring
    debug_mode = False
    extra_bonus = 0
    if debug_mode:
        extra_bonus = 100  # Never reached

    # Final score calculation
    intermediate = base_score + adjustment
    final_score = intermediate - risk_penalty
    
    return final_score

# Main execution
productivity = 0  # Will be redefined inside function
risk_set = {3, 6, 9, 12, 15, 18}  # Used in function

# Key statement
final_score = evaluate_performance(productivity, risk_set)
print(f"Result: {final_score}")