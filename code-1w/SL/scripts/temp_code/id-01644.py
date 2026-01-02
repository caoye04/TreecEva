from collections import defaultdict

# Simulate system performance evaluation across multiple metrics
def main():
    raw_inputs = [12, 15, 22, 8, 33, 19]
    adjustment_factor = 0.85
    baseline = sum(raw_inputs) / len(raw_inputs)

    # Irrelevant preprocessing (distractor)
    temp_data = [x * adjustment_factor for x in raw_inputs]
    normalized = [round((x - min(temp_data)) / (max(temp_data) - min(temp_data)) * 100) for x in temp_data]

    # Key metric calculations
    metrics = defaultdict(float)
    metrics['throughput'] = sum(x for x in raw_inputs if x > baseline)
    metrics['efficiency'] = len([x for x in raw_inputs if x % 2 == 0])
    metrics['stability'] = abs(raw_inputs[0] - raw_inputs[-1])

    # Bonus logic with conditional weighting
    bonus_weights = {}
    bonus_weights['throughput'] = 1.2 if metrics['throughput'] > 50 else 0.9
    bonus_weights['efficiency'] = 1.1 if metrics['efficiency'] >= 3 else 0.85
    bonus_weights['stability'] = 0.95 if metrics['stability'] < 20 else 0.7

    # Secondary distractor: unused alternative scoring
    alt_scores = []
    for val in raw_inputs:
        if val > baseline:
            penalty = 0.1 * (val - baseline)
            adjusted_val = val - penalty
n        else:
            adjusted_val = val + 1.5
        alt_scores.append(adjusted_val)

    # Unused function (dead code path - distractor)
    def deprecated_normalization(data):
        total = sum(data)
        return [d / total for d in data]

    # Core calculation
    base_score = sum(metrics.values())
    multiplier = 1.0
    for key in metrics.keys():
        if key in bonus_weights:
            multiplier *= bonus_weights[key]

    final_score = base_score * multiplier
    
    # Additional irrelevant transformation
    ceiling_limit = 100
    capped_score = min(final_score, ceiling_limit)
    buffer_zone = 5

    # Output result
    print(f"Result: {final_score}")

main()