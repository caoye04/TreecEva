def calculate_final_score(ranks, bonuses):
    base_points = 0
    multiplier = 1
    temp_result = []  # distractor variable

    for rank in ranks:
        if rank <= 3:
            base_points += 10
        elif rank <= 7:
            base_points += 5
        else:
            base_points += 1

    for i, (key, value) in enumerate(zip(bonuses.keys(), bonuses.values())):
        if i % 2 == 0:
            multiplier *= value

    final_score = base_points * multiplier
    return final_score

# Ranking data from competition rounds
rank_data = [1, 4, 8, 2, 6]
bonus_map = {'round1': 2, 'round2': 3, 'round3': 4}

# Irrelevant tracking variable (mild distraction)
processing_status = "completed"

final_score = calculate_final_score(rank_data, bonus_map)
print(f"Result: {final_score}")