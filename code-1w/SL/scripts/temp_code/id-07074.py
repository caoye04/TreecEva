def analyze_performance(data, weights):
    weighted_sum = 0
    normalization_factor = sum(weights)
    temp_result = []

    for i, (value, weight) in enumerate(zip(data, weights)):
        adjusted = value * weight / normalization_factor
        temp_result.append(adjusted)
        
    # Distractor: irrelevant computation on transformed data
    squared_magnitudes = [x**2 for x in temp_result]
    mean_square = sum(squared_magnitudes) / len(squared_magnitudes) if squared_magnitudes else 0

    return sum(temp_result)


def calculate_rating(contributions, impact_levels):
    base_score = 0
    bonus_tracker = []
    penalty_flag = False

    contribution_pairs = list(enumerate(zip(contributions, impact_levels)))

    for idx, (contrib, impact) in contribution_pairs:
        raw_contribution = contrib * impact
        
        # Apply tiered multiplier based on modular pattern
        tier_multiplier = (idx % 3) + 1
        scaled_contrib = raw_contribution * tier_multiplier
        
        if scaled_contrib > 50 and not penalty_flag:
            bonus_tracker.append(scaled_contrib * 0.1)
            penalty_flag = True  # Only trigger once

        base_score += scaled_contrib

    # Irrelevant transformation chain (distractor)
    noise_filter = lambda x: x ^ 7 if x > 0 else x | 3
    filtered_bonus = [noise_filter(int(b)) for b in bonus_tracker]
    auxiliary_total = sum(filtered_bonus) // 2 if filtered_bonus else 0

    # Final score depends only on base_score and first bonus (if any)
    final_additive = auxiliary_total * 0.5  # This will be small but non-zero
    result = base_score + (bonus_tracker[0] if bonus_tracker else 0) + final_additive

    return int(result)

# Core input data
contributions = [12, 15, 8, 20, 10]
impact_levels = [3, 4, 2, 5, 3]
weights = [1, 2, 1, 3, 2]

# Dummy call to distract (dead path)
dummy_analysis = analyze_performance([10, 20], [1, 1])

intermediate_metric = sum(contributions) * max(impact_levels) // len(contributions)

# Key execution point
final_score = calculate_rating(contributions, impact_levels)

print(f"Result: {final_score}")