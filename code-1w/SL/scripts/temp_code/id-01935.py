from itertools import combinations

def evaluate_performance(levels):
    return sum(l**2 for l in levels)

def calculate_final_score(ranks, weights):
    base = sum(ranks)
    weighted_bonus = sum(w * 0.5 for w in weights)
    adjustment = len(list(combinations(ranks, 2)))
    return int(base + weighted_bonus + adjustment)

# Irrelevant helper (minimal distraction)
def unused_helper(data):
    return [x for x in data if x > 0]

# Main computation
skill_levels = [3, 7, 2, 5]
bonus_weights = [10, 20, 30]
rankings = [4, 6, 8]

interim = evaluate_performance(skill_levels)
final_score = calculate_final_score(rankings, bonus_weights)

print(f"Result: {final_score}")