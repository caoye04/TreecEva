def calculate_final_score(data, limits):
    intermediate_sum = 0
    penalty_adjustment = 0
    bonus_multiplier = 1.0

    # Irrelevant tracking variables (distractors)
    sample_count = len(data)
    outlier_count = 0
    temp_cache = {}

    for key, value in data.items():
        if value < 0:
            outlier_count += 1
            continue

        # Real logic: apply tiered scoring based on thresholds
        threshold_high = limits['high']
        threshold_mid = limits['mid']

        if value >= threshold_high:
            intermediate_sum += 10
        elif value >= threshold_mid:
            intermediate_sum += 5
        else:
            intermediate_sum += 2

        # Dead code path - never executed due to logic above (distractor)
        if value > 1000:
            temp_cache[key] = value ** 0.5

    # Spurious calculation with no effect (distractor)
    avg_sample_value = sum(data.values()) / sample_count if sample_count else 0
    hidden_correction = avg_sample_value * 0.01

    # Bonus only applies if no outliers (not triggered here)
    if outlier_count == 0:
        bonus_multiplier = 1.2

    # Actual core computation
    base_penalty = 3 * (outlier_count > 0)
    final_score = (intermediate_sum - base_penalty) * bonus_multiplier

    return int(final_score)

# Main execution
results = {
    'test_A': 85,
    'test_B': 92,
    'test_C': 45,
    'test_D': 73,
    'test_E': 61,
    'test_F': -5  # outlier
}

thresholds = {
    'high': 90,
    'mid': 60
}

# Red herring function that's defined but not used
def debug_analysis(x): return sum(x.values()) % 7

final_score = calculate_final_score(results, thresholds)
print(f"Result: {final_score}")