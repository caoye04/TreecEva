from itertools import combinations

def calculate_final_score(ranks, multiplier):
    base_points = 0
    for pair in combinations(ranks, 2):
        if pair[0] < pair[1]:
            base_points += 1
    
    adjustment = len(ranks) % 4
    base_points -= adjustment
    
    # Irrelevant variable (minimal distraction)
    temp_debug = [x * 2 for x in ranks]
    
    return base_points * multiplier

# Input data
rankings = [3, 1, 4, 2, 5]
bonus_multiplier = 3

final_score = calculate_final_score(rankings, bonus_multiplier)
print(f"Result: {final_score}")