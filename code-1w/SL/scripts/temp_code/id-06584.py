def evaluate_performance(ranks, metrics):
    # Initialize relevant and irrelevant variables
    total = 0
    penalty = 0
    bonus = 0
    temp_result = 0  # distractor: used in dead code path

    # Core logic begins
    if len(ranks) > 3:
        base_score = sum(ranks)
        modifier = len(ranks.intersection({1, 2, 3}))

        for val in metrics:
            if val % 4 == 0:
                total += val // 2
            elif val % 3 == 0:
                total -= val // 3

        # Additional computation with partial relevance
        adjustment = base_score % 7

        # Key calculation branch
        if modifier >= 2:
            bonus = 17
        else:
            bonus = 5

        # Dead code block (distractor)
        if False:
            temp_result = bonus * adjustment
            temp_result += base_score

        # Final score accumulation
        final_score = total + bonus - adjustment

        return final_score

    else:
        # Unused fallback branch
        return sum(metrics) % 100

# Setup input data
rank_set = {2, 4, 5, 6}
base_metrics = [12, 9, 8, 15, 14]

# Irrelevant pre-computations (distractors)
shadow_value = sum(x ** 2 for x in base_metrics if x < 10)
duplicate_check = len(base_metrics) != len(set(base_metrics))

# Key execution point
final_score = evaluate_performance(rank_set, base_metrics)

# Output result as required
print(f"Target result: {final_score}")