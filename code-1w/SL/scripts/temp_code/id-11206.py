def process_ranking(ranks, weights):
    base_points = 0
    penalty_adjustment = 0
    temp_multiplier = 1.0
    total_shift = 0

    # Irrelevant bit shifting (distractor)
    for i in range(len(weights)):
        total_shift += (weights[i] << 2) >> 1

    # Real logic: scoring based on rank positions and weight mapping
    position_scores = {}
    for idx, player in enumerate(ranks):
        position_scores[player] = max(5 - idx, 0)  # Top 5 get points

    # Extra dictionary processing (semi-relevant)
    weighted_modifiers = {}
    for k, v in weights.items():
        if v > 2:
            weighted_modifiers[k] = v * 0.8
        else:
            weighted_modifiers[k] = v * 1.1

    # Actual score accumulation
    for player, base in position_scores.items():
        if player in weights:
            base_points += base * weights[player]

    # Dummy loop with no effect (dead code path)
    dummy_result = []
    for _ in range(3):
        dummy_result.append([0] * 5)

    # Conditional bonus application (relevant only if threshold met)
    avg_weight = sum(weights.values()) / len(weights)
    if avg_weight >= 3.0:
        bonus_pool = 10
        for player in ranks[:3]:  # Top 3 players
            if player in weighted_modifiers and weighted_modifiers[player] > 2.5:
                bonus_pool -= 2
        penalty_adjustment = bonus_pool  # Only affects final via offset

    # Final computation
    scaling_factor = len(ranks) % 4 or 1
    temp_multiplier = (base_points + penalty_adjustment) / (scaling_factor + 1)

    # Key assignment: this is where the answer is determined
    final_score = int(temp_multiplier + 0.5)  # Round to nearest integer

    return final_score

# Main execution
rankings = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
bonus_weights = {
    'Alice': 4,
    'Bob': 3,
    'Charlie': 2,
    'Diana': 5,
    'Frank': 1  # Not in rankings, irrelevant
}

result = process_ranking(rankings, bonus_weights)
print(f"Target result: {result}")