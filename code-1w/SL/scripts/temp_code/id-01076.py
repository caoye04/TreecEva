def evaluate_performance(output, risk_profile):
    base_efficiency = sum(output) // len(output)
    safety_margin = 100 - max(risk_profile)
    
    # Distractor: Irrelevant computation on latency
    latency_log = [0.5 * x + 2 for x in output]
    avg_latency = sum(latency_log) / len(latency_log)
    normalized_latency = avg_latency / (base_efficiency + 1)

    # Real logic begins
    compliance_check = len(risk_profile & {1, 3, 5, 7})  # Only odd risks matter
    adjustment_factor = 0
    if compliance_check == 0:
        adjustment_factor = 20
    elif compliance_check < 3:
        adjustment_factor = 10
    else:
        adjustment_factor = 0

    # Secondary distractor: Unused function definition
    def predict_future_trend(data):
        return [d * 1.1 for d in data]  # Never called

    # Accumulation with conditional boost
    performance_bonus = 0
    for val in output:
        if val > base_efficiency:
            performance_bonus += 5

    # Core formula
    score = base_efficiency + safety_margin + adjustment_factor + performance_bonus
    
    # Another red herring: complex but unused set operation
    stale_risks = risk_profile - {x for x in range(1, 10) if x % 2 == 1}
    critical_stale_count = len(stale_risks)

    return score

# Main execution
productivity = [12, 15, 10, 18, 14]
risk_levels = [2, 4, 6, 8]
risk_set = set(risk_levels)

interim_metric = len(productivity) * 3  # unused beyond here
temp_flag = False
if interim_metric > 10:
    temp_flag = True

final_score = evaluate_performance(productivity, risk_set)
print(f"Result: {final_score}")