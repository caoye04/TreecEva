def process_rankings(ranks, multiplier):
    base_points = [10, 8, 6, 4, 2]
    adjusted_ranks = [r % 7 for r in ranks if r > 0]  # modular arithmetic with filtering
    filtered_indices = [i for i in range(len(adjusted_ranks)) if i % 2 == 0]
    
    temp_sum = 0
    penalty = 0
    for idx in filtered_indices:
        if idx < len(base_points):
            temp_sum += base_points[idx] * (adjusted_ranks[idx] // 2)
        penalty += (idx ** 2) % 3  # irrelevant penalty accumulator (distractor)

    outlier_count = sum(1 for x in ranks if x == 99)  # red herring check
    scaling_factor = 1.0
    if len(ranks) > 3:
        scaling_factor = 1.25  # minor boost, not always impactful

    intermediate = temp_sum * scaling_factor
    
    # Simulate conditional bonus using bitwise and logical ops
    has_bonus = (multiplier > 1) and ((len(ranks) & 1) == 1)  # bitwise AND condition
    bonus = intermediate * 0.1 if has_bonus else 0

    final_score = int(intermediate + bonus - penalty)
    
    # Dead code path - never executed due to fixed condition (distractor)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {final_score}')
    
    return final_score

# Main execution
rankings = [5, -3, 12, 4, 99]
bonus_multiplier = 2
counterfeit_data = [x * 2 for x in rankings if x < 0]  # unused list comprehension (distractor)
final_score = process_rankings(rankings, bonus_multiplier)
print(f"Result: {final_score}")