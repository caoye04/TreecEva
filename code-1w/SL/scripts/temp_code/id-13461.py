def evaluate_performance(metrics, weights):
    # Normalize metrics using lambda for dynamic scaling
    normalized = list(map(lambda x: x / max(metrics) if max(metrics) != 0 else 0, metrics))

    # Irrelevant computation: track volatility (not used in final result)
    volatility = 0
    for i in range(1, len(normalized)):
        volatility += abs(normalized[i] - normalized[i-1])

    # Weighted aggregation with conditional boost
    base_score = sum(n * w for n, w in zip(normalized, weights))

    # Conditional performance bonus (depends on pattern in metrics)
    bonus = 0.0
    if all(metrics[i] <= metrics[i+1] for i in range(len(metrics)-1)):
        bonus = 10.0  # Monotonic increase bonus

    # Distractor: complex but unused transformation
    transformed = [round((x ** 0.5) * 10, 2) for x in normalized if x > 0.2]
    temp_result = sum(transformed) / len(transformed) if transformed else 0

    # Final adjustment based on threshold crossing
    threshold_crosses = sum(1 for m in metrics if m > 50)
    adjustment = 5 if threshold_crosses >= 2 else 0

    # Final score calculation
    final_score = base_score * 100 + bonus + adjustment
    return final_score

# Input data
metrics = [45, 60, 75, 80]
weights = [0.1, 0.2, 0.3, 0.4]

# Execution point
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")