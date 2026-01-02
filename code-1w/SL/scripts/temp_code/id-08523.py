def calculate_final_score(ranks, multiplier):
    base_points = 0
    penalty_adjustment = 0
    temp_sum = 0
    cumulative_offset = 0

    # Irrelevant tracking variables (distractors)
    max_rank_seen = float('-inf')
    rank_sequence = []
    debug_log = []

    for i, (idx, rank) in enumerate(zip(range(len(ranks)), ranks)):
        if rank <= 0:
            continue  # Invalid rank, skip

        # Real logic: accumulate base points with position weighting
        base_points += (rank * (i + 1)) % 7

        # Semi-relevant: track for potential later use (but not used in final result)
        temp_sum += rank ** 0.5
        rank_sequence.append(rank)

        # Conditional nesting with red herring branch
        if i % 2 == 0:
            penalty_adjustment += 2
            if rank > 5:
                cumulative_offset -= 1
        else:
            penalty_adjustment -= 1
            shadow_variable = idx * 2  # Dead computation

    # Another layer of distraction: unused normalization attempt
    if len(rank_sequence) > 0:
        avg_rank = sum(rank_sequence) / len(rank_sequence)
        normalized_total = avg_rank * 1.5  # Not used

    # Key calculation hidden among noise
    adjustment_factor = (base_points + penalty_adjustment) % 10
    score_boost = 0

    # Simulate conditional bonus logic
    for j in range(3):
        if adjustment_factor > 5:
            score_boost += multiplier * 2
        else:
            score_boost += multiplier // 2

    # Final score depends only on base_points and score_boost
    final_result = base_points + score_boost

    # Misleading variable that looks important but isn't part of answer
    performance_tier = 'A' if final_result > 30 else 'B'

    return final_result


# Main execution
rank_data = [4, 6, 2, 8, -1, 3]
bonus_multiplier = 3
auxiliary_data = [x ** 2 for x in rank_data]  # Unused data structure
offset_tracker = 0

for k in range(len(rank_data)):
    offset_tracker += k * 0.5  # Distractor loop

final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")