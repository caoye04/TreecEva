def calculate_final_score(ranks, multiplier):
    base_points = [100, 80, 60, 40, 20]
    rank_map = {i+1: base_points[i] for i in range(len(base_points))}
    
    # Irrelevant pre-processing: Normalize ranks (not used later)
    normalized_ranks = [r / max(ranks) for r in ranks]
    temp_weights = list(map(lambda x: x ** 0.5, normalized_ranks))

    # Core logic: Compute raw score from top 3 ranked entries
    filtered_ranks = [r for r in ranks if r <= 5]
    sorted_ranks = sorted(filtered_ranks)[:3]
    raw_score = sum(rank_map[r] for r in sorted_ranks)

    # Distractor: unused conditional branch
    adjustment = 0
    if len(sorted_ranks) > 3:
        adjustment = -10
    elif min(sorted_ranks) == 1:
        adjustment = 5  # This executes but doesn't affect final path

    # Bonus logic with distractor variables
    streak_bonus = 0
    for i in range(1, len(sorted_ranks)):
        if sorted_ranks[i] == sorted_ranks[i-1] + 1:
            streak_bonus += 10

    # Secondary distraction: set operations with no impact
    all_possible = set(range(1, 6))
    missing_ranks = all_possible - set(ranks)
    penalty_factor = len(missing_ranks) * 0.5  # Computed but unused

    # Final computation chain
    intermediate = raw_score + streak_bonus
    applied_bonus = intermediate * multiplier
    final_score = int(applied_bonus + adjustment)

    return final_score

# Main execution
rankings = [1, 3, 4, 2, 6, 1]
bonus_multiplier = 1.1

# Dead code: function that simulates load but does nothing
def preload_cache():
    cache = {x: x*2 for x in range(100)}
    return None

preload_cache()  # No effect

initial_flag = True
if initial_flag:
    temp_result = sum([x**2 for x in rankings])  # Unused accumulation

final_score = calculate_final_score(rankings, bonus_multiplier)
print(f"Result: {final_score}")