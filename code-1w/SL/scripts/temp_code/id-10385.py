def calculate_final_score(ranks, extra):
    base_points = 0
    rank_multiplier = {1: 10, 2: 8, 3: 6}
    for rank, player in enumerate(ranks, start=1):
        if rank in rank_multiplier:
            base_points += rank_multiplier[rank]
    
    # Additional logic using set operations
    valid_bonuses = {p for p in extra if p in ranks}
    bonus_points = len(valid_bonuses) * 5
    
    # Use of zip to pair data
    adjustments = [abs(i - v) for i, v in zip(range(len(ranks)), [3,1,4])]
    penalty = sum(adjustments)
    
    temp_result = base_points + bonus_points  # Irrelevant intermediate
    unused_var = [x**2 for x in range(3)]      # Slight distractor (low interference)
    
    final_score = temp_result - penalty
    return final_score

# Input data
player_rankings = ['Alice', 'Bob', 'Charlie']
performance_bonuses = ['Bob', 'Eve', 'Alice']

result = calculate_final_score(player_rankings, performance_bonuses)
print(f"Target result: {result}")