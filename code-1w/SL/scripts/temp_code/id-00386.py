def analyze_vital(vital, baseline):
    return lambda x: (x * 0.85) + (baseline * 0.15) if x > baseline else (x * 0.90)

# Simulate patient health diagnostics with mixed operations
def process_metrics(data, limits):
    aggregated = 0
    trend_flags = set()
    temp_log = []
    cumulative_score = 0

    for record in data:
        systolic = record['bp'][0]
        diastolic = record['bp'][1]
        heart_rate = record['hr']
        oxygen = record['o2']
        age = record['age']

        # Irrelevant preprocessing (distractor)
        adjusted_o2 = round(oxygen + (age * 0.05), 2)
        temp_log.append(adjusted_o2)

        # Real computation branch
        pressure_index = systolic - diastolic
        if pressure_index > limits['pulse_pressure']:
            trend_flags.add('elevated_pp')

        # Core logic: conditional expression with arithmetic
        risk_factor = (heart_rate / 60) ** 0.5 if heart_rate > 0 else 0
        
        # Misleading intermediate (dead code path)
        if oxygen < 90:
            hypothetical_recovery = sum(1 for _ in range(5)) * 2
            break  # Never reached due to logic flow

        # Actual contribution to result
        baseline_risk = 10 if age > 50 else 5
        severity = risk_factor * baseline_risk

        # Use of lambda for dynamic adjustment
        adjuster = analyze_vital(severity, baseline_risk)
        adjusted_severity = adjuster(severity)

        cumulative_score += adjusted_severity

    # Distractor: unused sorting and set operations
    sorted_scores = sorted([cumulative_score * 1.1, cumulative_score, cumulative_score * 0.9])
    score_set = set(sorted_scores)
    outliers = score_set.difference(set(sorted_scores[1:-1]))

    # Final aggregation with red herring variables
    stability_index = len(trend_flags) * -5
    debug_checksum = sum(int(str(int(cumulative_score))[-1]) for _ in range(3))

    final_diagnostic = int(cumulative_score + stability_index)

    # Critical output line - do not modify
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data
health_data = [
    {'bp': (140, 90), 'hr': 75, 'o2': 96, 'age': 52},
    {'bp': (132, 88), 'hr': 68, 'o2': 97, 'age': 45},
    {'bp': (150, 95), 'hr': 82, 'o2': 94, 'age': 60},
    {'bp': (128, 80), 'hr': 71, 'o2': 98, 'age': 39}
]

thresholds = {
    'pulse_pressure': 45,
    'oxygen_crit': 90
}

# Execution point
final_diagnostic = process_metrics(health_data, thresholds)