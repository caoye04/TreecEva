def evaluate_performance(metrics, thresholds):
    # Initialize tracking variables
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = 0

    # Irrelevant pre-processing (distractor)
    for key in metrics:
        if 'temp' in key:
            temp_result += metrics[key] * 0.1

    # Core evaluation logic
    stability = metrics.get('stability', 0)
    responsiveness = metrics.get('responsiveness', 0)
    efficiency = metrics.get('efficiency', 0)

    # Distractor: unused computation
    hypothetical_index = (stability * 0.3 + efficiency * 0.7) / (responsiveness + 1e-5)

    # Threshold-based scoring with conditional expressions
    base_score += 20 if stability > thresholds['stability'] else -5
    base_score += 15 if responsiveness >= thresholds['responsiveness'] else 0
    base_score += 25 if efficiency > thresholds['efficiency'] else -10

    # Bonus conditions with list accumulation (semi-relevant)
    if stability > 80 and efficiency > 75:
        bonus_tracker.append(12)
    if responsiveness > 90:
        bonus_tracker.append(8)

    # Penalty logic with nested conditionals
    if stability < 60:
        if efficiency < 50:
            penalty_adjustment -= 15
        else:
            penalty_adjustment -= 5

    # Dictionary-driven dynamic adjustment (actual relevant logic)
    severity_map = {'low': 0, 'medium': -8, 'high': -20}
    risk_level = 'low'
    if stability < 50 or efficiency < 40:
        risk_level = 'high'
    elif stability < 70 or efficiency < 60:
        risk_level = 'medium'

    penalty_adjustment += severity_map[risk_level]

    # Final score computation
    final_component = sum(bonus_tracker) + base_score + penalty_adjustment

    # Dead code path (distractor)
    if temp_result > 100:
        final_component *= 1.1  # Never reached due to input constraints

    return int(final_component)

# Main execution context
metrics_data = {
    'stability': 85,
    'responsiveness': 92,
    'efficiency': 78,
    'temp_diagnostic_1': 45,
    'temp_diagnostic_2': 67
}

thresholds_config = {
    'stability': 70,
    'responsiveness': 85,
    'efficiency': 70
}

# Key statement
final_score = evaluate_performance(metrics_data, thresholds_config)

print(f"Target result: {final_score}")