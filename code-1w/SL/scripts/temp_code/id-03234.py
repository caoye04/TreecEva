def calculate_performance(data):
    base_multiplier = 1.5
    penalty_factor = 0.9
    bonus_threshold = 85
    adjustment = 0.0

    # Preprocess: extract execution times and normalize scores
    normalized = [score / 100 for score in data if score > 0]
    indices_and_values = list(enumerate(normalized))

    # Misleading computation: irrelevant statistics
    avg_value = sum(normalized) / len(normalized) if normalized else 0
    variance_proxy = sum((x - avg_value) ** 2 for x in normalized) / len(normalized) if normalized else 0

    # Simulate performance tiers using conditional logic and comparisons
    tiered_scores = []
    for i, val in indices_and_values:
        raw_score = val * 100
        if raw_score >= bonus_threshold:
            applied_bonus = base_multiplier * 1.2
        elif raw_score >= 70:
            applied_bonus = base_multiplier
        else:
            applied_bonus = base_multiplier * 0.8
            if i % 3 == 0:
                adjustment -= 0.05  # Minor penalty for position pattern

        final_val = raw_score * applied_bonus
        tiered_scores.append(final_val)

    # Secondary distraction: zipping unrelated metadata
    positions = list(range(len(tiered_scores)))
    metadata_pairs = list(zip(positions, tiered_scores))
    temp_sum = sum(p * v for p, v in metadata_pairs if p % 2 == 1)

    # Actual core logic: aggregate with adjustment
    raw_total = sum(tiered_scores)
    stability_penalty = len([v for v in normalized if v < 0.6]) * 2.5
    consistency_bonus = len([v for v in normalized if v >= 0.9]) * 3.0 if len(normalized) > 4 else 0

    # Final calculation chain
    intermediate_result = raw_total - stability_penalty + consistency_bonus
    adjusted_result = intermediate_result + (adjustment * 100)
    
    # Distractor: unused helper logic
    def smooth(x):
        return x * 0.95 + 5  # Never called
    
    # Key statement
    final_score = int(round(adjusted_result))
    return final_score

# Input data
benchmark_data = [95, 82, 73, 67, 90, 45, 88]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")