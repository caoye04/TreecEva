def calculate_final_score(ranks, scores):
    adjusted = sum(scores) // len(scores)
    bonus = len(ranks.intersection({1, 2, 3})) * 10
    penalty = len(ranks.difference({1, 2, 3, 4, 5})) * 2
    return adjusted + bonus - penalty

# Simulate competition ranking and scoring
team_ranks = {1, 3, 5, 7, 9}
base_scores = [85, 90, 78, 92]

# Irrelevant variable (minor distraction)
unused_multiplier = 1.5

final_score = calculate_final_score(team_ranks, base_scores)
print(f"Result: {final_score}")