def evaluate_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized_metrics = [round((m - min(metrics)) / (max(metrics) - min(metrics) + 1e-8), 3) for m in metrics]

    # Semi-relevant pre-processing: categorize each metric
    categories = ['high' if m > t else 'low' for m, t in zip(metrics, thresholds)]

    # Distractor: unused computation
    outlier_flags = [abs(m - sum(metrics)/len(metrics)) > 2 for m in metrics]

    # Core logic begins: count transitions in category sequence
    transitions = 0
    for i in range(1, len(categories)):
        if categories[i] != categories[i-1]:
            transitions += 1

    # Secondary logic: compute weighted score with decay
    base_score = sum(m * (0.9 ** i) for i, m in enumerate(metrics))

    # Tertiary logic: adjust score based on transition penalty
    penalty = transitions * 5.2

    # Distractor: dead code path (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print(f"Transitions detected: {transitions}")

    # Key computation
    final_score = base_score - penalty

    # Additional red herring: irrelevant slicing operation
    tail_values = metrics[-3:]  # not used anywhere

    # Another distractor variable
    temp_result = [x for x in metrics if x > sum(thresholds) / len(thresholds)]

    return final_score

# Input data
metrics = [85, 90, 78, 92, 88, 76, 95]
thresholds = [80, 85, 75, 90, 87, 77, 93]

# Execute main logic
final_score = evaluate_performance(metrics, thresholds)

# Output result as required
print(f"Result: {final_score}")