def calculate_final_score(data, weight_map):
    base_scores = []
    adjustments = []
    temp_sum = 0

    for i, (rank, score) in enumerate(data):
        if rank <= 3:
            base_modifier = 1.5
        elif rank <= 6:
            base_modifier = 1.2
        else:
            base_modifier = 0.8

        # Irrelevant accumulation (distractor)
        temp_sum += i * score

        adjusted = score * base_modifier
        base_scores.append(adjusted)

        # Dead computation - adjustment not used later
        if adjusted > 50:
            adjustments.append(adjusted * 0.1)
        else:
            adjustments.append(adjusted * 0.05)

    # Secondary loop with zip - relevant for weighting
    weighted_total = 0
    for val, (key, w) in zip(base_scores, sorted(weight_map.items())):
        weighted_total += val * w

    # Misleading normalization (not applied to final result)
    normalized = weighted_total / max(weighted_total, 1) if weighted_total != 0 else 0

    # Final score calculation - only this matters
    final_score = int(weighted_total // len(base_scores))

    # Extraneous state tracking
    log_entry = f"Processed {len(base_scores)} entries with avg {weighted_total / len(base_scores):.2f}"

    return final_score

# Input data: (rank, initial_score)
rank_data = [(1, 45), (4, 60), (7, 30), (2, 50)]
weights = {'A': 0.4, 'B': 0.3, 'C': 0.2, 'D': 0.1}

# Call function and store result
final_score = calculate_final_score(rank_data, weights)
print(f"Result: {final_score}")