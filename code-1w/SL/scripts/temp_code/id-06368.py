from itertools import groupby

def calculate_final_score(ranks, weights):
    # Group consecutive ranks to count frequency
    grouped = [(k, len(list(g))) for k, g in groupby(sorted(ranks))]
    
    # Calculate base score as sum of rank frequencies multiplied by their rank
    base_score = sum(rank * count for rank, count in grouped)
    
    # Apply bonus weights based on rank position
    weighted_bonus = 0
    for i, (rank, count) in enumerate(grouped):
        if rank in weights:
            weighted_bonus += weights[rank] * (i + 1)  # position-based multiplier
    
    # Irrelevant distraction: unused variable
    temp_debug_log = f'Processed {len(grouped)} groups'
    
    final_score = base_score + weighted_bonus
    return final_score

# Input data
rank_data = [3, 1, 2, 2, 3, 1, 1, 3]
bonus_weights = {1: 2, 3: 1}

final_score = calculate_final_score(rank_data, bonus_weights)
print(f"Result: {final_score}")