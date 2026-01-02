def calculate_final_score(ranks, performances):
    base_score = 0
    bonus_multiplier = 1.0

    # Count how many performers are in top-tier ranks
    elite_count = len(performances.intersection(ranks.keys()))

    # Add base points for each elite performer
    for performer in performances:
        if performer in ranks:
            base_score += ranks[performer]

    # Apply multiplier based on diversity of performance
    if len(performances) >= 3:
        bonus_multiplier += 0.5

    # Irrelevant distraction: unused variable
    temp_offset = -5  

    # Compute final score
    final_score = base_score * bonus_multiplier

    return int(final_score)

# Define ranking and performance data
rank_map = {'alpha': 8, 'beta': 12, 'gamma': 15, 'delta': 6}
performance_set = {'alpha', 'beta', 'gamma', 'omega'}

# Execute main logic
final_score = calculate_final_score(rank_map, performance_set)
print(f"Result: {final_score}")