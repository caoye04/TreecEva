def evaluate_performance(metrics, thresholds):
    # Normalize metrics using min-max scaling (irrelevant for final result but adds cognitive load)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics)) if max(metrics) != min(metrics) else 0 for m in metrics]
    
    # Compute weighted sum of metrics above threshold (core logic)
    weights = [1.2, 0.8, 1.5, 0.5, 1.0]
    active_indices = [i for i in range(len(metrics)) if metrics[i] > thresholds[i]]
    
    # Distractor: calculate inverse_weights but not used in final computation
    inverse_weights = [1.0 / w for w in weights if w != 0]
    temp_sum = sum(inverse_weights[:3]) * 0.1  # Dead-end calculation

    # Secondary distractor: sorting normalized values but unused
    sorted_norm = sorted(normalized, reverse=True)
    median_normalized = sorted_norm[len(sorted_norm)//2]  # Not used

    # Core logic: sum of weighted active metrics
    weighted_active = sum(metrics[i] * weights[i] for i in active_indices)
    
    # Apply non-linear bonus if more than 2 metrics exceed thresholds
    bonus = 10.5 if len(active_indices) > 2 else 0

    # Tertiary distractor: simulate decay over hypothetical iterations
    decay_accumulator = 0
    for k in range(1, 4):
        decay_accumulator += bonus / (k * 1.5)  # Computation with no impact

    # Final score calculation – only weighted_active and bonus matter
    final_score = int(weighted_active + bonus)

    # Additional red herring: modify final_score in a way that doesn't persist
    _ = [final_score + 10 for _ in range(2)]  # List comprehension with no assignment

    return final_score

# Input data
metrics = [78, 85, 90, 60, 88]
thresholds = [75, 80, 85, 65, 87]

# Key execution point
final_score = evaluate_performance(metrics, thresholds)
print(f"Target result: {final_score}")