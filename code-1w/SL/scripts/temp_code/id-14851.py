def calculate_final_score(data, weights):
    # Preprocess: Normalize and filter valid entries
    normalized = {}
    total_weight = sum(weights.values())
    temp_values = []
    scaling_factor = 1.0 / (total_weight if total_weight > 0 else 1)

    for key, value in data.items():
        if value < 0:
            continue  # Skip invalid negative ranks
        adjusted = value * scaling_factor
        normalized[key] = round(adjusted, 4)
        temp_values.append(adjusted)

    # Irrelevant distraction: sort but don't use sorted list directly
    sorted_vals = sorted(temp_values, reverse=True)
    mid_point = len(sorted_vals) // 2
    median_trend = (sorted_vals[mid_point] + sorted_vals[-mid_point-1]) / 2 if mid_point > 0 else 0

    # Real computation begins: weighted harmonic mean with bonus logic
    weighted_inv_sum = 0.0
    weight_sum = 0.0
    for k, v in normalized.items():
        w = weights.get(k, 0)
        if v > 0 and w > 0:
            weighted_inv_sum += w / v
            weight_sum += w

    # Handle edge case
    harmonic_component = weight_sum / weighted_inv_sum if weighted_inv_sum > 0 else 0

    # Bonus adjustment based on conditional expression
    penalty_factor = 0.9 if len(normalized) < 3 else 1.0
    final_bonus = sum([weights[k] * 0.1 for k in normalized if k.startswith('tier')])

    # Final score calculation
    base_score = harmonic_component * penalty_factor
    final_score = base_score + final_bonus

    # Dead code path - never executed under current logic
    if False and 'debug' in data:
        print(f'Debug mode active: {data["debug"]}')

    return round(final_score, 4)

# Main execution context
rank_data = {
    'tier_A': 12,
    'tier_B': 8,
    'tier_C': 15,
    'tier_D': -1,  # Invalid, will be filtered
    'meta_X': 5
}
bonus_weights = {
    'tier_A': 3,
    'tier_B': 4,
    'tier_C': 2,
    'tier_D': 1,
    'meta_X': 0
}

# Intermediate irrelevant calculations
aggregate_sum = sum(rank_data.values())
dropped_count = len([v for v in rank_data.values() if v < 0])
mean_shift = aggregate_sum / (len(rank_data) - dropped_count) if dropped_count < len(rank_data) else 0

# Key statement
final_score = calculate_final_score(rank_data, bonus_weights)

# Output result
print(f'Result: {final_score}')