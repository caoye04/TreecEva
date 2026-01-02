from itertools import combinations

# Simulate ranking-based scoring with noise filtering and weighted aggregation
def compute_final_score(ranks, w):
    normalized = [max(0.0, min(10.0, float(11 - r)))) for r in ranks]
    scaled = [n * factor for n, factor in zip(normalized, w)]
    
    # Irrelevant distractor: pairwise rank differences (not used)
    pair_diffs = []
    for i in range(len(ranks)):
        for j in range(i+1, len(ranks)):
            pair_diffs.append(abs(ranks[i] - ranks[j]))
    
    # Semi-relevant: count top performers
    top_count = sum(1 for s in scaled if s > 7.0)
    adjustment = 0.5 if top_count >= 3 else 0.2
    
    # Core logic: average of scaled scores with adjustment
    base_avg = sum(scaled) / len(scaled)
    bonus = adjustment * len([x for x in ranks if x <= 3])
    return base_avg + bonus

# Dataset: competition rankings and importance weights
rankings = [1, 4, 2, 6, 3, 8]
weights = [1.2, 0.8, 1.5, 0.5, 1.0, 0.7]

# Distractor variables
reversed_ranks = rankings[::-1]
sum_pairs = list(combinations(rankings, 2))
mean_rank = sum(rankings) / len(rankings)
rank_strings = [str(r) for r in rankings]
joined_ranks = ''.join(rank_strings)

# Noise calculation (dead code path)
count_inversions = 0
for i in range(len(reversed_ranks)):
    for j in range(i+1, len(reversed_ranks)):
        if reversed_ranks[i] < reversed_ranks[j]:
            count_inversions += 1

# Key execution point
temp_result = compute_final_score(rankings, weights)
final_score = round(temp_result, 4)

print(f"Result: {final_score}")