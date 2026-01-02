def calculate_final_score(ranks, penalties):
    base_score = len(ranks)
    adjustment = sum([penalties.get(r, 0) for r in ranks])
    
    # Irrelevant distraction: unused calculation
    temp_factor = base_score * 0.1
    
    filtered_ranks = {r for r in ranks if r > 1}
    bonus = len(filtered_ranks) // 2
    
    return base_score - adjustment + bonus

# Main logic
rank_list = [1, 3, 4, 1, 5]
penalty_map = {3: 2, 4: 1, 5: 3}
rank_set = set(rank_list)

# Another distraction: unused lambda
weight_fn = lambda x: x ** 0.5

final_score = calculate_final_score(rank_set, penalty_map)
print(f"Result: {final_score}")