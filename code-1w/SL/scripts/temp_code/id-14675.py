def evaluate_performance(output, risk):
    base_efficiency = sum(output) // len(output)
    safety_margin = 10
    threshold = 5

    # Irrelevant computation: historical average (not used in final logic)
    historical_avg = (sum(range(1, len(output) + 1)) / len(output)) if output else 0

    # Distractor: unused transformation
    adjusted_output = [x * 1.1 for x in output]
    capped_values = [min(x, 20) for x in adjusted_output]

    # Semi-relevant filtering
    high_performers = [x for x in output if x > base_efficiency]

    # Real logic begins: count how many risk factors are mitigated
    mitigation_count = 0
    for val in output:
        temp_set = {val % 3, val % 5, val % 7}
        intersection = temp_set & risk  # set operation
        if len(intersection) >= 2:
            mitigation_count += 1

    # Secondary path: unused conditional branch
    if len(high_performers) > threshold:
        dummy_score = len(high_performers) * safety_margin

    # Actual scoring logic
    raw_score = len(high_performers) * 100
    penalty = len(risk) * 15
    final_score = raw_score - penalty + mitigation_count

    return final_score

# Main execution
productivity = [8, 12, 5, 19, 3, 14]
risk_factors = {2, 3, 5, 7}
deprecated_flag = False
legacy_buffer = [0] * 5

# Key statement
final_score = evaluate_performance(productivity, risk_factors)

print(f"Result: {final_score}")