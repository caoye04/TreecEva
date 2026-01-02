def calculate_rating(ranks, multiplier):
    base_score = 0
    penalty = 0
    temp_result = []
    
    # Irrelevant pre-processing (distractor)
    for k in sorted(ranks.keys()):
        if ranks[k] > 5:
            temp_result.append(k * 2)  # Unused computation

    # Core logic with dictionary operations and conditionals
    for key, value in ranks.items():
        if value >= 8:
            base_score += value * 1.5
        elif value >= 5:
            base_score += value
        else:
            penalty += 1

    # Misleading intermediate calculation (not used directly)
    avg_rank = sum(ranks.values()) / len(ranks) if ranks else 0
    adjustment = avg_rank * 0.1  # Computed but not impactful

    # Another red herring: sorting that doesn't affect outcome
    sorted_values = sorted(ranks.values(), reverse=True)
    for i, v in enumerate(sorted_values):
        if i % 3 == 0:
            adjustment += v * 0.05  # Minor distraction

    # Actual score computation uses only base_score, penalty, and multiplier
    raw_score = (base_score - penalty * 2) * multiplier
    final_score = int(raw_score + 0.5)  # Round to nearest integer

    return final_score

# Initialize data
rank_map = {
    'alpha': 9,
    'beta': 7,
    'gamma': 10,
    'delta': 4,
    'epsilon': 6
}

bonus_multiplier = 1.2
offset_correction = 3.1415  # Dead variable
threshold_limit = 8  # Unused constant

# Execute main logic
final_score = calculate_rating(rank_map, bonus_multiplier)

print(f"Result: {final_score}")