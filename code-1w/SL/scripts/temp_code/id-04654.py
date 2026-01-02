def evaluate_performance(score, penalty_factor):
    normalized_score = score / 100
    is_excellent = normalized_score >= 0.9
    is_marginal = normalized_score >= 0.5
    base_penalty = 10
    
    if is_excellent:
        bonus = 25 * normalized_score
        final_score = int(100 + bonus)
    else:
        adjustment = 5 if is_marginal else 15
        final_score = int(100 - (penalty_factor * adjustment))
        
    passes_threshold = final_score > 80
    result = final_score if passes_threshold else base_penalty
    return result

# Execution context
current_score = 88
factor = 2
target_result = evaluate_performance(current_score, factor)
print(f"Result: {target_result}")