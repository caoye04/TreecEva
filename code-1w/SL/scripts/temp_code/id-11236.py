def calculate_final_score(data):
    base_points = 10
    bonus_multiplier = 1.5
    rank_bonus = {1: 20, 2: 15, 3: 10}
    participation_award = 5

    total_entries = len(data)
    valid_ranks = [val for val in data.values() if isinstance(val, int) and val > 0]

    avg_rank = sum(valid_ranks) / len(valid_ranks) if valid_ranks else 3

    base_award = base_points + (rank_bonus.get(min(valid_ranks), 0) if valid_ranks else 0)

    adjustment = 0
    if avg_rank <= 1.5:
        adjustment = 10
    elif avg_rank <= 2.5:
        adjustment = 5

    final_score = (base_award + participation_award + adjustment) * bonus_multiplier
    return final_score

rank_data = {'player_A': 1, 'player_B': 2, 'player_C': 1, 'status': 'active'}
final_score = calculate_final_score(rank_data)
print(f"Result: {final_score}")