def evaluate_performance(output, risk):
    base_score = 100
    adjustment = 0

    # Complex scoring logic with intermediate distractions
    if output > 80:
        adjustment += 15
    elif output > 60:
        adjustment += 8
    else:
        adjustment -= 10

    # Distractor: Irrelevant health check computation
    health_metrics = [0.85, 0.91, 0.76, 0.88]
    avg_health = sum(health_metrics) / len(health_metrics)
    normalized_health = (avg_health - 0.8) * 100  # Not used later

    # Risk evaluation using lambda for dynamic threshold
    risk_penalty = (lambda r: 20 if r > 0.7 else (10 if r > 0.5 else 0))(risk)
    adjustment -= risk_penalty

    # Simulated experience multiplier (constant in this case)
    experience_years = 5
    exp_multiplier = 1.0 + min(experience_years * 0.05, 0.5)

    # Final score calculation
    final_raw = (base_score + adjustment) * exp_multiplier

    # Additional red herring: unused productivity trend analysis
    trends = [(1, 65), (2, 70), (3, 85)]
    growth_rate = sum(t[1] - trends[i-1][1] for i in range(1, len(trends)))  # Computed but unused

    # Apply ceiling cap
    final_score = int(min(final_raw, 120))

    return final_score

# Main execution context
productivity = 74
risk_factor = 0.68

# Unused diagnostic data structure
system_diagnostics = {
    "load": 0.77,
    "uptime": 1420,
    "errors_seen": 3,
    "recovery_count": 1
}

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Print result for inspection
print(f"Result: {final_score}")