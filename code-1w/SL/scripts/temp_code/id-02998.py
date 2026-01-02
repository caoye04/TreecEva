from collections import Counter

def calculate_final_score(ranks, pen):
    rank_count = Counter(ranks)
    total_ranks = len(ranks)
    most_common_rank = rank_count.most_common(1)[0][1]
    avg_rank = sum(ranks) / total_ranks
    penalty_adjustment = sum(pen.values())
    raw_score = (avg_rank * most_common_rank) - penalty_adjustment
    return int(raw_score + 0.5)

# Input data
rankings = [3, 5, 5, 2, 5, 4, 5, 1]
penalties = {'timeout': 2, 'warning': 1}

# Computation
initial_avg = sum(rankings) / len(rankings)  # distractor: not used in final logic
duplicate_check = set(rankings)  # distractor: just checks uniqueness
final_score = calculate_final_score(rankings, penalties)

print(f"Result: {final_score}")