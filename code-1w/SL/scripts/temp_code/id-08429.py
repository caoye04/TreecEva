def evaluate_performance(output, risk):
    base_efficiency = 85.0
    adjustment_factor = 0.9
    if output > 70:
        base_efficiency += 10
    else:
        base_efficiency -= 5

    # Irrelevant computation (distractor)
    hypothetical_gain = base_efficiency * 1.5 if risk < 0.5 else base_efficiency * 0.7

    # Real adjustment using lambda (required feature)
    decay_function = lambda x, r: x * (1 - r * 0.15)
    adjusted = decay_function(base_efficiency, risk)

    # Additional logic step with boolean reasoning
    stability_bonus = 7 if output > 60 and risk < 0.4 else 0
    adjusted += stability_bonus

    # More distractors: unused intermediate calculations
    projected_trend = adjusted * 1.2
    fallback_estimate = (adjusted + 80) / 2
    outlier_check = adjusted > 90

    # Final threshold clamp
    if adjusted > 95:
        adjusted = 95
    elif adjusted < 50:
        adjusted = 50

    return round(adjusted, 2)

# Simulated input data
productivity = 78
risk_factor = 0.35

# Dead code path (misleading control flow)
if productivity < 50:
    risk_factor *= 2
elif productivity > 90:
    risk_factor *= 0.8
else:
    pass  # No-op branch for distraction

# Secondary distractor variables
baseline_projection = productivity * 1.1
risk_tolerance = 1.0 if risk_factor < 0.3 else 0.8

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result as required
print(f"Result: {final_score}")