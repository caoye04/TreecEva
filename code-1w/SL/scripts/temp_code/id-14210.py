def evaluate_performance(output, risk):
    base_score = sum([x * 0.8 for x in output if x > 5])
    penalty = 0
    if any(r > 0.7 for r in risk):
        penalty += 15
    if len(risk) > 3:
        penalty += 5
    adjustment = 1.0
    for i in range(len(output)):
        if i % 2 == 0 and output[i] < 10:
            adjustment *= 0.95
    # Irrelevant tracking variables
    debug_log = []
    temp_buffer = set()
    for val in output:
        temp_buffer.add(val * 2 + 3)
        debug_log.append(f'Processed {val}')
    # Unused complex structure
    historical_weights = {i: 0.9 ** i for i in range(len(output))}
    scaling_factor = len(temp_buffer) / (len(output) + 1e-5)
    effective_score = base_score * adjustment - penalty
    return int(effective_score)

# Simulated team performance metrics
productivity = [6, 8, 4, 9, 7]
risk_factor = [0.5, 0.8, 0.3, 0.9]

# Dead code path - never executed
legacy_mode = False
backup_scores = None
if legacy_mode:
    backup_scores = [evaluate_performance([1,2], [0.1])] * 3

# Key computation
final_score = evaluate_performance(productivity, risk_factor)

# Additional irrelevant calculations
outlier_count = len({x for x in productivity if x < 5})
shadow_score = sum(productivity) * 0.5 - sum(risk_factor) * 10

# Final output
print(f"Result: {final_score}")