def calculate_final_score(ranks, adjusters):
    base_points = 0
    bonus_multiplier = 1.0
    
    # Convert ranks to initial points using dictionary mapping
    rank_to_points = {1: 100, 2: 80, 3: 60, 4: 40, 5: 20}
    for rank in ranks:
        if rank in rank_to_points:
            base_points += rank_to_points[rank]
    
    # Apply performance adjustments using set intersection to find valid bonuses
    valid_bonuses = {"A", "B", "C"}
    eligible_adjusters = set(adjusters) & valid_bonuses
    
    for adj in eligible_adjusters:
        if adj == "A":
            bonus_multiplier *= 1.2
        elif adj == "B":
            bonus_multiplier *= 1.15
        elif adj == "C":
            base_points += 10
    
    # Final score with truncated integer arithmetic
    final_score = int(base_points * bonus_multiplier)
    return final_score

# Input data
rankings = [1, 3, 1, 4]
performance_adjusters = ["A", "X", "B", "Z"]  # Only A and B are valid

# Compute result
target_result = calculate_final_score(rankings, performance_adjusters)
print(f"Result: {target_result}")