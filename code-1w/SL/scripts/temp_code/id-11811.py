from itertools import permutations

def evaluate_performance(ranks, weights):
    base_score = 0
    penalty = 0
    temp_adjustment = 0

    # Real logic: weighted sum of rank positions
    for i, rank in enumerate(ranks):
        if rank < 5:
            base_score += weights[i] * (6 - rank)

    # Distractor: complex permutation check that doesn't affect result
    all_perms = list(permutations(range(3)))
    shuffle_count = 0
    for p in all_perms:
        if p[0] > p[1]:
            shuffle_count += 1

    # Irrelevant string transformation
    status_flag = "processing"
    status_flag = status_flag.upper()
    status_flag = status_flag[::-1]

    # Another distractor calculation with no impact
    dummy_matrix = [[i * j for j in range(3)] for i in range(3)]
    trace_sum = sum(dummy_matrix[i][i] for i in range(3))

    # Actual adjustment used in final score
    multiplier = len(ranks) - 2 if len(ranks) > 2 else 1
    temp_adjustment = base_score * 0.8

    # Final computation
    final_score = int(temp_adjustment + 17)  # Only this matters

    return final_score

# Input data
rankings = [1, 3, 2, 4, 5]
weights = [10, 20, 15, 25, 30]

# Key statement
final_score = evaluate_performance(rankings, weights)
print(f"Result: {final_score}")