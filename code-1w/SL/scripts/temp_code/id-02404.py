from itertools import zip_longest

def calculate_final_score(ranks, coeffs):
    normalized = [max(0, 10 - rank) for rank in ranks]
    weighted = [n * c for n, c in zip_longest(normalized, coeffs, fillvalue=1)]
    raw_score = sum(weighted)
    bonus = 5 if raw_score > 40 else 0
    return raw_score + bonus

# Initial data
rankings = [3, 1, 4, 2, 5]
weights = [2, 1, 3]

final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")