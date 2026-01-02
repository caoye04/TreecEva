def evaluate_performance(output, constraints):
    base_efficiency = len(output)
    penalty = 0

    # Distractor: Irrelevant calculation on unused metric
    phantom_metric = sum([x ** 0.5 for x in output if x > 10])
    temp_buffer = [base_efficiency * i for i in range(3)]  # Dead computation

    # Real logic begins: determine constraint violations
    critical_failures = constraints.difference(output)
    minor_issues = output.intersection(constraints)

    # Nested logic with interdependent steps
    if len(critical_failures) > 0:
        for failure in critical_failures:
            if failure % 3 == 0:
                penalty += 5
            elif failure % 2 == 0:
                penalty += 2

    score_adjustment = 0
    for issue in minor_issues:
        if issue > 5:
            score_adjustment += 3
        else:
            score_adjustment += 1

    # Secondary distractor: complex but unused formula
    theoretical_max = base_efficiency * 10 - len(critical_failures) * 7.5
    deprecated_factor = theoretical_max / (1 + penalty) if penalty else 0  # Not used

    # Final score computation
    raw_score = base_efficiency * 10 - penalty * 4 + score_adjustment
    final_score = int(raw_score)

    return final_score

# Simulated dataset
productivity_set = {2, 4, 5, 6, 9, 12}
risk_set = {3, 6, 9, 12, 15}

# Key execution point
final_score = evaluate_performance(productivity_set, risk_set)
print(f"Result: {final_score}")