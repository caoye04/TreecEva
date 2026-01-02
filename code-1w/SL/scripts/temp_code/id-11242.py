from collections import defaultdict

# Simulate contestant rankings from three rounds
round1_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
round2_scores = {'Alice': 88, 'Bob': 87, 'Charlie': 80}
round3_scores = {'Alice': 91, 'Bob': 85, 'Charlie': 84}

# Aggregate total scores using defaultdict
aggregated = defaultdict(int)
for scores in [round1_scores, round2_scores, round3_scores]:
    for name, score in scores.items():
        aggregated[name] += score

# Apply dynamic bonus based on rank improvement (simplified logic)
def calculate_improvement_bonus(scores_list):
    if len(scores_list) < 3:
        return 0
    improvement = (scores_list[2] - scores_list[0])
    return max(improvement, 0)

rankings = {}
for contestant in aggregated:
    history = [round1_scores[contestant], round2_scores[contestant], round3_scores[contestant]]
    base_total = aggregated[contestant]
    bonus = calculate_improvement_bonus(history)
    rankings[contestant] = base_total + bonus

# Bonus weights based on performance consistency (using lambda)
consistency_check = lambda x: 1.0 if (max(x) - min(x)) <= 5 else 0.8
bonus_weights = {name: consistency_check([round1_scores[name], round2_scores[name], round3_scores[name]])
                for name in rankings}

def calculate_final_score(ranks, weights):
    weighted_sum = 0
    for name in ranks:
        weighted_sum += ranks[name] * weights[name]
    return int(weighted_sum / len(ranks))  # Average final score

final_score = calculate_final_score(rankings, bonus_weights)
print(f"Target result: {final_score}")