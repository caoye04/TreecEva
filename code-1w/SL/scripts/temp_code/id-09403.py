def evaluate_performance(output, risk):
    base_score = 100
    adjustment = 0

    # Complex productivity scoring with distractors
    if output > 80:
        adjustment += 15
    elif output > 60:
        adjustment += 8
    else:
        adjustment -= 10

    # Distractor: Irrelevant string processing (simulating log analysis)
    log_entry = "ERROR: Minor timeout in module X"
    error_count = len(list(filter(lambda x: x.isupper(), log_entry)))
    warning_flag = 'WARNING' in log_entry or 'ERROR' in log_entry
    normalized_flags = sum(1 for c in log_entry if c in ['!', '?']) * 2

    # Risk-based penalty using dictionary mapping
    risk_map = {'low': 0.1, 'medium': 0.25, 'high': 0.5}
    risk_multiplier = risk_map.get(risk, 0.15)

    volatility_index = 0
    for i in range(3):
        volatility_index += (output * risk_multiplier) // (i + 1)  # Some misleading accumulation

    # Real impact: volatility affects score only if risk is high
    if risk == 'high':
        adjustment -= int(volatility_index * 0.1)

    # More distraction: unused helper computation
    def calculate_efficiency(a, b):
        return (a * 0.7) + (b * 0.3)

    efficiency = calculate_efficiency(output, base_score)  # Computed but not used

    # Final score calculation (key statement)
    final_score = base_score + adjustment - int(risk_multiplier * 10)

    return final_score

# Main execution flow
productivity = 72
risk_level = 'medium'
risk_factor = risk_level

interim_result = productivity * 1.1  # Red herring operation
placeholder_list = [1, 2, 3, 4]
expanded_data = [x * interim_result for x in placeholder_list]  # Dead-end computation

final_score = evaluate_performance(productivity, risk_factor)
print(f"Target result: {final_score}")