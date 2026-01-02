def process_leaderboard(entries):
    # Irrelevant preprocessing: normalize names (not used in final logic)
    normalized_names = [name.strip().title() for name, _ in entries]
    scores = [score for _, score in entries]

    # Distractor: frequency analysis of score digits (unused)
    digit_count = {}
    for score in scores:
        for digit in str(abs(score)):
            digit_count[int(digit)] = digit_count.get(int(digit), 0) + 1

    # Actual relevant logic: rank by score with tie-breaking index
    ranked = sorted([(score, idx) for idx, score in enumerate(scores)], reverse=True)
    rank_map = {idx: rank for rank, (score, idx) in enumerate(ranked)}

    # Bonus calculation based on rank distribution (semi-relevant)
    bonus_base = {}
    for idx, (score, _) in enumerate(ranked):
        position = idx + 1
        if position <= 3:
            bonus_base[position] = score * 0.1
        elif position <= 6:
            bonus_base[position] = score * 0.05
        else:
            bonus_base[position] = score * 0.02

    # Dead code path: never executed due to structure (misleading)
    temp_result = None
    if len(entries) > 100:
        temp_result = sum(bonus_base.values()) / len(bonus_base)

    # Build rank data with adjusted bonuses and original indices
    rank_data = {}
    for i, (score, orig_idx) in enumerate(ranked):
        rank = i + 1
        adjustment_factor = 1 + (0.01 * (10 - min(rank, 10)))  # Diminishing returns
        rank_data[orig_idx] = {
            'base': score,
            'rank': rank,
            'adjusted_bonus': bonus_base.get(rank, 0) * adjustment_factor
        }

    return rank_data


def calculate_final_score(rank_data, weights):
    total_weighted = 0.0
    total_weight = 0.0

    # Use dictionary operations and conditional expressions
    for info in rank_data.values():
        base_val = info['base']
        bonus_val = info['adjusted_bonus']
        rank_weight = weights.get(info['rank'], 1.0)

        # Slicing-like behavior using conditionals (idiomatic Python)
        contribution = (base_val * 0.7 + bonus_val * 1.5) * rank_weight

        # Early termination if absurd values (never triggered here)
        if base_val < -9999:
            return -1

        total_weighted += contribution
        total_weight += rank_weight

    # Final aggregation
    return int(total_weighted / total_weight) if total_weight > 0 else 0


# Main execution
player_entries = [
    ("Alice", 88), ("Bob", 94), ("Charlie", 76), ("Diana", 94),
    ("Eve", 81), ("Frank", 94), ("Grace", 88), ("Henry", 76)
]

# Bonus weights by rank (top performers get higher influence)
bonus_weights = {1: 1.3, 2: 1.3, 3: 1.2, 4: 1.1, 5: 1.0, 6: 0.9, 7: 0.8, 8: 0.7}

# Process leaderboard to extract structured rank data
rank_data = process_leaderboard(player_entries)

# Calculate final composite score
final_score = calculate_final_score(rank_data, bonus_weights)

# Output result
print(f"Result: {final_score}")