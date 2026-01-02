def evaluate_performance(metrics, weights):
    # Normalize metrics using min-max scaling (irrelevant for final result but adds cognitive load)
    normalized = [(m - min(metrics)) / (max(metrics) - min(metrics) + 1e-8) for m in metrics]

    # Apply weights with lambda function (core logic)
    weighted_sum = sum(map(lambda x, w: x * w, metrics, weights))

    # Auxiliary computation - creates distraction
    squared_devs = [(x - sum(metrics)/len(metrics))**2 for x in metrics]
    variance_proxy = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    # Simulate confidence adjustment (not actually used)
    confidence_factor = 1.0
    if all(m > 0.5 for m in normalized):
        confidence_factor = 1.1
    elif any(m < 0.1 for m in normalized):
        confidence_factor = 0.9

    # Core decision logic with enumerate and zip
    adjustment = 0
    for i, (metric, weight) in enumerate(zip(metrics, weights)):
        if i % 2 == 0 and metric > 0.7:
            adjustment += weight * 0.05
        elif i % 2 == 1 and metric < 0.3:
            adjustment -= weight * 0.02

    # Final score calculation - this is the key line
    final_score = weighted_sum + adjustment

    # Dead code path - never executed due to fixed inputs
    if False:
        final_score = max(0.0, min(1.0, final_score))

    return final_score

# Input data
metrics = [0.85, 0.62, 0.91, 0.45, 0.73]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Unused helper variables - distractors
baseline_scores = [0.7, 0.65, 0.8, 0.5, 0.75]
drift_correction = sum(abs(a - b) for a, b in zip(metrics, baseline_scores))

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Output result
print(f"Result: {final_score}")