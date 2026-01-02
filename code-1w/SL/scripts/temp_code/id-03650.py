from collections import defaultdict

def calculate_final_score(performances):
    score_map = defaultdict(int)
    for rank in performances:
        score_map[rank] += 1
    
    sorted_ranks = sorted(score_map.keys(), reverse=True)
    bonus_applied = False
    total_points = 0
    
    for idx, rank in enumerate(sorted_ranks):
        base_points = score_map[rank] * rank
        extra = 5 if not bonus_applied and rank >= 3 else 0
        total_points += base_points + extra
        bonus_applied = bonus_applied or (extra > 0)
    
    adjustment = -2 if len(sorted_ranks) > 4 else 0
    total_points += adjustment
    
    return total_points

# Simulated input: competition rankings from event logs
rankings = [1, 3, 2, 3, 4, 1, 5]
ignored_filter = [x for x in rankings if x > 1]  # Distractor: not used in main logic

final_score = calculate_final_score(rankings)
Result: final_score