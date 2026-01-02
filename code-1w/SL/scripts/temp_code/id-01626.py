from collections import defaultdict

# Simulate user engagement scores across different content categories
category_views = ['tech', 'lifestyle', 'tech', 'fitness', 'lifestyle', 'tech', 'fitness']
engagement_scores = [85, 72, 90, 60, 80, 95, 65]

# Count frequency of views per category
view_count = defaultdict(int)
for category in category_views:
    view_count[category] += 1

# Calculate average engagement per category
avg_engagement = {}
tech_total = lifestyle_total = fitness_total = 0
tech_count = lifestyle_count = fitness_count = 0

for i, cat in enumerate(category_views):
    if cat == 'tech':
        tech_total += engagement_scores[i]
        tech_count += 1
    elif cat == 'lifestyle':
        lifestyle_total += engagement_scores[i]
        lifestyle_count += 1
    elif cat == 'fitness':
        fitness_total += engagement_scores[i]
        fitness_count += 1

avg_engagement['tech'] = tech_total / tech_count if tech_count else 0
avg_engagement['lifestyle'] = lifestyle_total / lifestyle_count if lifestyle_count else 0
avg_engagement['fitness'] = fitness_total / fitness_count if fitness_count else 0

# Rank categories by average engagement
ranked_categories = sorted(avg_engagement, key=avg_engagement.get, reverse=True)
rank_data = {cat: rank + 1 for rank, cat in enumerate(ranked_categories)}

# Bonus logic based on ranking
base_bonus = 1.5
bonus_multiplier = base_bonus if rank_data['tech'] == 1 else 1.0

# Irrelevant distraction: unused function
unrelated_calc = lambda x: x ** 2 + 2 * x + 1

# Final score calculation
def calculate_final_score(rank_dict, bonus):
    total_ranks = sum(rank_dict.values())
    tech_rank = rank_dict['tech']
    return int((100 / tech_rank) * bonus + (10 - total_ranks))

final_score = calculate_final_score(rank_data, bonus_multiplier)
print(f"Result: {final_score}")