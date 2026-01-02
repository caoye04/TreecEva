from itertools import combinations

def evaluate_performance(metrics):
    base_score = sum(metrics) * 0.8
    bonus = 0
    for combo in combinations(metrics, 2):
        if combo[0] + combo[1] > 15:
            bonus += 1
    return base_score + bonus

def calculate_final_score(ranks, weights):
    weighted_sum = 0
    for i in range(len(ranks)):
        weighted_sum += ranks[i] * weights[i]
    raw_score = evaluate_performance([weighted_sum, ranks[0], weights[1]])
    penalty = 0
    temp_var = 999  # irrelevant variable (distractor)
    unused_list = [1, 2, 3]  # irrelevant data structure (minor distractor)
    if weighted_sum > 30:
        penalty = 5
    return int(raw_score - penalty)

# Main execution
rankings = [7, 5, 8]
weights = [2, 3, 1]
intermediate = rankings[0] + weights[2]  # minor distraction
final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")