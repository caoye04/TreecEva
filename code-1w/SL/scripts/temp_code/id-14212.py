def evaluate_performance(output, risk_profile):
    base_score = 0
    penalty = 0
    bonus = 0

    # Irrelevant distraction: unused function call simulation
    debug_mode = False
    log_entries = []
    if debug_mode:
        log_entries.append('Debug: Starting evaluation')

    # Core logic begins
    if output > 80:
        base_score += 40
    elif output > 60:
        base_score += 25
    else:
        base_score += 10

    # Set operations for risk classification
    high_risk_flags = {1, 3, 4, 7}
    medium_risk_flags = {2, 5, 6}
    critical_risk_flags = {9}

    detected_risks = risk_profile.intersection(high_risk_flags)
    potential_risks = risk_profile.difference(critical_risk_flags)

    # Risk-based penalty calculation (only intersection with high_risk matters)
    if len(detected_risks) >= 2:
        penalty += 15
    elif len(detected_risks) == 1:
        penalty += 5

    # Fake complexity: unused path
    compliance_check = True
    audit_trail = []
    for flag in potential_risks:
        if flag in medium_risk_flags:
            audit_trail.append(f"Review needed for flag {flag}")
    # End of unused block

    # Bonus logic based on output efficiency
    efficiency_ratio = output / (len(risk_profile) + 1)
    if efficiency_ratio > 20:
        bonus += 10

    final_score = base_score - penalty + bonus

    # Distraction: irrelevant tracking variables
    summary_report = {
        "output_level": output,
        "risk_count": len(risk_profile),
        "adjustments_applied": penalty + bonus
    }

    return final_score

# Simulated data input
productivity = 85
risk_indicators = {1, 2, 5}
redundant_flags = {8, 9}  # Not used directly
combined_set = risk_indicators.union(redundant_flags)  # Slight misdirection

# Key execution point
final_score = evaluate_performance(productivity, risk_indicators)

# Output result as required
print(f"Target result: {final_score}")