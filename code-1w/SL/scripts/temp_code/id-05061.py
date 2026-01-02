def analyze_efficiency(metrics):
    adjusted = [m * 1.2 for m in metrics if m > 5]
    return sum(adjusted) / len(adjusted) if adjusted else 0


def compute_stress_level(workload, threshold=8):
    stress = 0
    for i, load in enumerate(workload):
        if load > threshold:
            stress += (load - threshold) * 1.5
    return stress


def evaluate_performance(output, risk):
    baseline = 100
    penalty = 0
    
    # Complex conditional adjustments
    if any(x < 3 for x in output):
        penalty += 15
    
    avg_output = sum(output) / len(output)
    if avg_output > 7:
        baseline += 30
    else:
        baseline -= 10

    # Distractor: Irrelevant computation with zip
    temp_data = list(zip(output, [x * 0.1 for x in output]))
    temp_sum = sum(a * b for a, b in temp_data)  # Not used later

    # Risk-based adjustment
    risk_factor = 0
    for r in risk:
        if r > 4:
            risk_factor += r * 2
    
    final_risk_adjustment = max(risk_factor, 20)
    
    # Another distractor: unused state tracking
    status_log = {}
    for i, val in enumerate(output):
        status_log[f'entry_{i}'] = 'processed' if val > 4 else 'flagged'

    # Final score computation
    baseline -= penalty
    baseline -= final_risk_adjustment // 3
    
    return int(baseline)

# Main execution
productivity = [8, 6, 9, 7, 5]
risk_assessment = [3, 5, 6, 4]

interim = analyze_efficiency(productivity)
wip_stress = compute_stress_level(productivity, threshold=7)

# Key statement
final_score = evaluate_performance(productivity, risk_assessment)

print(f"Result: {final_score}")