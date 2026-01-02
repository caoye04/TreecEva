def calculate_final_score(ranks):
    # Filter top performers with rank <= 3
    top_performers = [rank for rank in ranks if rank <= 3]
    bonus_points = len(top_performers) * 10
    
    # Calculate base score as sum of all ranks
    base_score = sum(ranks)
    
    # Apply penalty for lowest rank
    lowest_rank = max(ranks)
    penalty = lowest_rank * 2
    
    # Compute final score
    final_score = base_score - penalty + bonus_points
    return final_score

# Simulated competition rankings
rankings = [1, 4, 2, 5, 3, 6]

# Irrelevant distraction: unused variable (minimal interference)
dummy_value = sorted(rankings, reverse=True)

final_score = calculate_final_score(rankings)
print(f"Result: {final_score}")