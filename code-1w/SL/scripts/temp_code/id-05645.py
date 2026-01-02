def evaluate_performance(output, risk):
    base_score = len(output) * 3
    penalty = 0

    # Irrelevant string processing (distractor)
    status_messages = ["OK", "WARNING", "ERROR"]
    log_entry = "System: Process ".lower() + "completed".upper()
    temp_flag = "DEBUG" in log_entry

    if len(risk) > 4:
        penalty += 15
    else:
        penalty += 5

    # Misleading intermediate calculations
    efficiency_ratio = (base_score / (len(risk) + 1)) if risk else 0
    debug_trace = [base_score >> i for i in range(3)]  # Bit shifting distraction

    # Core logic hidden among noise
    adjustment = 0
    if 'high' in output and 'critical' not in risk:
        adjustment += 22
    elif 'low' in output:
        adjustment -= 10
    else:
        adjustment += 8

    # Actual score computation
    raw_score = base_score - penalty + adjustment

    # Conditional expression used meaningfully
    multiplier = 1.5 if 'high' in output and len(risk.intersection({'critical', 'moderate'})) == 0 else 1.0
    final_score = int(raw_score * multiplier)

    # Dead code path (never reached due to structure)
    if False:
        fallback = set(range(10))
        final_score = sum(fallback) % 7

    return final_score

# Simulate workflow states
productivity = ['high', 'stable', 'responsive']
risk_factors = {'minor', 'delay', 'overhead', 'bottleneck'}
unused_buffer = [0] * 12  # Allocated but unused

# Key execution point
final_score = evaluate_performance(productivity, risk_factors)
print(f"Result: {final_score}")