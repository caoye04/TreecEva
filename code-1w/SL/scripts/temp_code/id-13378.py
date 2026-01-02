def evaluate_performance(output, risk_profile):
    base_efficiency = sum([x * 1.5 for x in output if x > 2])
    penalty = 0
    
    # Tracking irrelevant metrics (distractor)
    peak_moment = -1
    surge_count = 0
    for i, val in enumerate(output):
        if val > 5:
            surge_count += 1
            if surge_count == 1:
                peak_moment = i

    # Unused transformation (dead code path - distractor)
    normalized = []
    max_val = max(output) if output else 1
    for val in output:
        if val > 0:
            normalized.append(round(val / max_val, 3))
        else:
            normalized.append(0)

    # Real logic begins
    efficiency_bonus = 0
    if base_efficiency > 20:
        efficiency_bonus = 10
    elif base_efficiency > 10:
        efficiency_bonus = 5

    # Risk adjustment using set operations
    high_risk_levels = {7, 8, 9, 10}
    risk_intersection = risk_profile & high_risk_levels
    risk_penalty = len(risk_intersection) * 2

    # Conditional branch based on risk tolerance
    risk_tier = "low"
    if len(risk_profile) > 3:
        risk_tier = "medium"
        if len(risk_intersection) > 1:
            risk_tier = "high"

    # Secondary distraction: historical trend simulation (not used)
    trend_projection = []
    for i in range(len(output) - 1):
        delta = output[i+1] - output[i]
        projected_next = output[i+1] + delta * 0.5
n        trend_projection.append(projected_next)

    # Final calculation (key step)
    stability_factor = len(output) - len(risk_profile)
    final_score = int(base_efficiency + efficiency_bonus - risk_penalty + stability_factor)
    
    return final_score

# Main execution context
productivity = [3, 4, 1, 6, 2, 7]
risk_factors = {2, 4, 6, 8}
irrelevant_thresholds = {0, 1, 3, 5, 7}

# Misleading intermediate computation (semi-relevant but not critical)
clean_data = [x for x in productivity if x % 2 == 0]
discount_rate = len(clean_data) * 0.1

# Core assignment with distractors around
baseline = sum(productivity) // len(productivity)
adjusted_baseline = baseline * 2 if baseline < 4 else baseline

# Key statement
final_score = evaluate_performance(productivity, risk_factors)

print(f"Result: {final_score}")