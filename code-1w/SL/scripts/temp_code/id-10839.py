def calculate_final_score(ranks, multiplier):
    # Irrelevant transformation (distractor)
    temp_adjusted = [r * 1.1 for r in ranks if r < 10]
    offset = sum(temp_adjusted) / len(temp_adjusted) if temp_adjusted else 0

    # Semi-relevant preprocessing: filter top performers
    top_performers = {i for i, r in enumerate(ranks) if r <= 3}
    eligible_indices = [i for i in range(len(ranks)) if i % 2 == 0]

    # Core logic: count how many top performers are at even indices
    valid_count = len(top_performers.intersection(set(eligible_indices)))

    # Secondary logic: compute base score using slice of ranks
    segment = ranks[1:6:2]  # every second element from index 1 to 5
    base_score = sum(segment) * 0.5

    # Bonus mechanism based on conditional expression
    bonus = 10 if valid_count >= 2 else 5

    # Misleading complex calculation (not used in final result)
    phantom_score = 0
    for i in range(len(ranks)):
        for j in range(i):
            if ranks[i] < ranks[j]:
                phantom_score += 1

    # Final composition
    adjustment = len(top_performers) > 0 and multiplier or 1.0
    final_score = base_score + bonus * adjustment
    return final_score

# Input data
rankings = [4, 2, 7, 1, 3, 9, 6]
bonus_multiplier = 1.5

# Execution point
final_score = calculate_final_score(rankings, bonus_multiplier)
print(f"Result: {final_score}")