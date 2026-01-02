def compute_threshold_rating():
    raw_values = [12, 15, 8, 23, 16]
    ratings = [val ** 0.5 for val in raw_values]
    base_rating = sum(ratings) / len(ratings)
    
    # Additional processing with enumerate and conditional expression
    adjustments = []
    for i, r in enumerate(ratings):
        adjustment = r * 0.1 if i % 2 == 0 else r * 0.05
        adjustments.append(adjustment)
    
    adjusted_ratings = [ratings[i] + adjustments[i] for i in range(len(ratings))]
    final_rank = max(adjusted_ratings) * (1 + (sum(adjustments) / base_rating))

    # Bitwise operation used to simulate flag check
    control_flag = 0b1010
    modifier = 1 if control_flag & 0b0010 else -1
    final_rank = final_rank * (1 + 0.05 * modifier)

    # Key statement
    threshold_score = final_rank if (final_rank > base_rating) else base_rating * 0.8
    
    # Irrelevant distraction: unused variable
    temp_debug_log = [f"Step {i}: {v}" for i, v in enumerate(raw_values)]

    print(f"Result: {threshold_score}")

compute_threshold_rating()