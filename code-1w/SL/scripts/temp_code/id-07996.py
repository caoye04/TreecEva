def evaluate_performance(metrics, flags):
    base = sum(metrics)
    adjustment = 0
    
    # Irrelevant transformation on flags (distractor)
    temp_flags = set([f ^ 3 for f in flags])
    unused_flag_value = sum(temp_flags) * 0.1  # Not used later
    
    if len(flags) > 2:
        adjustment += 10
    else:
        adjustment -= 5
    
    # Another red herring: complex-looking but unused computation
    shadow_metrics = [m ** 2 for m in metrics if m > 4]
    cumulative_shadow = 0
    for val in shadow_metrics:
        cumulative_shadow += val - 2
    
    # Real logic begins: filter meaningful contributions
    relevant_contributions = [m for m in metrics if m >= 5]
    contribution_bonus = len(relevant_contributions) * 3
    
    # Use set intersection to determine risk penalty
    high_risk_codes = {1, 3, 7, 9}
    risk_intersection = flags & high_risk_codes
    risk_penalty = len(risk_intersection) * 2
    
    # Nested logic with dependency on multiple factors
    if base > 20:
        if adjustment > 0:
            base += 5
        else:
            base -= 3
    else:
        base += 2
    
    final_score = base + contribution_bonus - risk_penalty
    
    # Dead code path (never executed due to fixed input, but looks active)
    if False and unused_flag_value > 100:
        final_score *= 1.1
    
    return final_score

# Main execution context
productivity = [6, 7, 3, 8]
risk_indicators = {2, 3, 5, 7}

# Unused but plausible-looking preprocessing
normalized_productivity = [p / max(productivity) * 10 for p in productivity]
scaled_sum = sum(normalized_productivity)

# Key statement
final_score = evaluate_performance(productivity, risk_indicators)

print(f"Target result: {final_score}")