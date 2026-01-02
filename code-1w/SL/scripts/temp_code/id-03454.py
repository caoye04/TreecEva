from collections import defaultdict

# Simulate player stats and bonus multipliers
stats = [78, 85, 92, 64, 88]
bonuses = [1.1, 1.0, 1.2, 0.9, 1.25]

# Irrelevant distraction: unused variable
unused_threshold = 50

# Apply weighted scoring using list comprehension and lambda
calculate_weighted = lambda base, mult: int(base * mult)
weighted_achievements = [calculate_weighted(score, bonus) for score, bonus in zip(stats, bonuses)]

# Aggregate by category using defaultdict (irrelevant categorization)
category_map = defaultdict(list)
for idx, val in enumerate(weighted_achievements):
    category = 'high' if val >= 90 else 'medium' if val >= 75 else 'low'
    category_map[category].append(val)

# Compute final score as sum of top 3 weighted achievements
sorted_weights = sorted(weighted_achievements, reverse=True)
top_three_total = sum(sorted_weights[:3])
penalty = len([x for x in stats if x < 70]) * 2  # small penalty for low base scores
final_score = top_three_total - penalty

# Output result
print(f"Result: {final_score}")