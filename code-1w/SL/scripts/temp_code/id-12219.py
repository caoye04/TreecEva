def evaluate_performance(weights, results):
    # Normalize results using min-max scaling (irrelevant for final logic but adds computation)
    min_val, max_val = min(results), max(results)
    normalized = [(x - min_val) / (max_val - min_val + 1e-9) for x in results]

    # Apply weighted sum using lambda for dynamic weighting (key operation)
    weighted_sum = sum(map(lambda w, r: w * r, weights, results))

    # Secondary metric: count how many exceed threshold (distractor computation)
    threshold_count = sum(1 for r in results if r > 0.7)
    adjustment_factor = 0.9 if threshold_count >= 2 else 1.1  # unused later

    # Simulate confidence calibration (dead code path - never executed)
    confidence = None
    if False:
        confidence = sum(r ** 2 for r in normalized) / len(normalized)

    # Core logic: apply fixed bonus based on pattern match (actual determinant)
    pattern_match = all(abs(results[i] - results[i+1]) < 0.3 for i in range(len(results)-1))
    bonus = 15 if pattern_match else 0

    # Final score computed here — this is the key statement
    final_score = weighted_sum * 100 + bonus

    # Extra distraction: update with unused dictionary mapping
    status_map = {'low': 1, 'medium': 2, 'high': 3}
    level = 'medium' if final_score < 200 else 'high'

    return final_score

# Input data
metric_weights = [0.4, 0.3, 0.2, 0.1]
raw_results = [0.8, 0.6, 0.55, 0.75]

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_results)
print(f"Target result: {final_score}")