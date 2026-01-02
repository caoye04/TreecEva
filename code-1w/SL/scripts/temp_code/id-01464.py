def evaluate_performance(metrics, limits):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_result = 0

    # Irrelevant precomputation (distractor)
    for i in range(3):
        temp_result += i * 2

    # Real logic begins: assess each metric against threshold
    for key, value in metrics.items():
        threshold = limits.get(key, 0)

        if value > threshold:
            base_score += 10
            if key == 'latency' and value < threshold + 5:
                bonus_tracker.append(3)
            elif key == 'throughput':
                base_score += 5  # Extra reward for high throughput
        else:
            penalty_adjustment -= 2

    # Dead code path - never executed due to fixed keys, but looks relevant
    if 'redundant_flag' in metrics:
        base_score += 100

    # Unused helper computation (misleading)
    avg_bonus = sum(bonus_tracker) / len(bonus_tracker) if bonus_tracker else 0

    # Final adjustment using only base_score and penalty_adjustment
    final = base_score + penalty_adjustment + len(bonus_tracker)

    return final

# Simulation data
system_metrics = {
    'latency': 12,
    'throughput': 47,
    'error_rate': 0.03
}

thresholds = {
    'latency': 15,
    'throughput': 40,
    'error_rate': 0.05
}

# Extraneous variable initialization (distraction)
initial_assessment = 0
audit_log = []
for k in system_metrics:
    audit_log.append(f"{k}_checked")

# Key execution point
final_score = evaluate_performance(system_metrics, thresholds)

# Output result as required
print(f"Result: {final_score}")