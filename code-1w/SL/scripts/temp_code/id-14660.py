def evaluate_performance(metrics, weights):
    base_score = 0
    penalty_adjustment = 0
    bonus_tracker = []
    temp_offset = 0

    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        normalized = metric / (i + 1) if i % 2 == 0 else metric * 0.9
        contribution = normalized * weight

        if contribution > 15:
            penalty_adjustment -= 3
            bonus_tracker.append(contribution * 0.1)

        base_score += int(contribution)

        # Distractor: irrelevant accumulation
        temp_offset += (i * weight) % 3

    # Dead computation path (no effect on result)
    outlier_count = sum(1 for v in metrics if v > 20)
    if outlier_count > 2:
        temp_offset *= -1

    # Secondary loop with semi-relevant logic
    scaling_factor = 1.0
    for idx, val in enumerate(weights):
        scaling_factor *= (val % 2 + 1)
        if idx == len(weights) // 2:
            scaling_factor = round(scaling_factor, 1)
            break  # early exit

    final_score = base_score + penalty_adjustment

    # Additional red herring variables
    debug_info = {'offset': temp_offset, 'factor': scaling_factor, 'bonus_sum': sum(bonus_tracker)}
    
    return final_score

# Input data
metrics = [25, 18, 12, 30, 8]
weights = [2, 4, 3, 5, 1]

# Key execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")