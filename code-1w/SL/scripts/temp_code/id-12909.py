from collections import defaultdict

# Simulate a ranked scoring system for a competition
def calculate_final_score(ranks, importance):
    base_scores = [100 - rank for rank in ranks]
    weighted_scores = [base * weight for base, weight in zip(base_scores, importance)]
    return sum(weighted_scores) // len(weighted_scores)

# Irrelevant auxiliary data (minimal distraction - intervention level 4)
team_data = defaultdict(lambda: 'unknown')
team_data['event'] = 'annual_tournament'

# Core input data
rankings = [1, 3, 2, 4]
weights = [3, 2, 4, 1]

# Computation point of interest
final_score = calculate_final_score(rankings, weights)

print(f"Target result: {final_score}")