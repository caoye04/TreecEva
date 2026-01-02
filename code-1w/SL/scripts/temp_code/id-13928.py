def evaluate_performance(output, risk):
    base_score = sum(output) // len(output)
    adjustment = 0
    
    # Irrelevant computation: tracking unused efficiency metrics
    peak_efficiency = max(output) * 0.85
    avg_efficiency = sum(x * 0.9 for x in output if x > 10) or 10

    # Real logic begins: apply penalty based on risk exposure
    risk_factor = len(risk.intersection({2, 4, 6, 8}))
    if risk_factor > 2:
        adjustment -= 15
    elif risk_factor == 0:
        adjustment += 10
    else:
        adjustment -= 5

    # Secondary adjustment based on trend (slicing last 3 elements)
    recent_trend = output[-3:]
    if all(x > 12 for x in recent_trend):
        adjustment += 8

    # Distractor: complex but unused calculation involving string conversion
    temp_diag = ''.join([str(x % 5) for x in output[:5]])
    diagnostic_sum = sum(int(d) for d in temp_diag if int(d) % 2 == 0)

    # Another red herring: nested loop that computes but doesn't use anything
    buffer_overflow_sim = 0
    for i in range(2):
        for j in range(3):
            buffer_overflow_sim += (i + 1) * (j - 1) ** 2

    # Final score calculation
    final_score = base_score + adjustment
    return final_score

# Main execution context
productivity = [14, 11, 13, 15, 10, 12]
temp_data = [x ** 2 for x in productivity if x < 12]  # unused later
baseline_check = set(temp_data).difference({121})     # irrelevant

risk_set = {1, 3, 4, 7, 8}

# Additional distraction: unused conditional block
if len(productivity) % 2 == 0:
    shadow_metric = sum(temp_data) / len(temp_data)

final_score = evaluate_performance(productivity, risk_set)
print(f"Result: {final_score}")