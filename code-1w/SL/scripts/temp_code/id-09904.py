from collections import defaultdict

# Simulate user engagement analytics for a content platform
user_views = [120, 150, 130, 200, 180, 160, 140, 190]
user_ratings = [3.2, 4.1, 3.8, 4.5, 4.0, 3.9, 3.6, 4.3]
user_tags = ['tech', 'lifestyle', 'tech', 'education', 'lifestyle', 'tech', 'education', 'tech']

# Irrelevant distractor: tag frequency counter (semi-used but not critical)
tag_count = defaultdict(int)
for tag in user_tags:
    tag_count[tag] += 1

# Misleading preprocessing: normalize views to arbitrary scale
max_view = max(user_views)
scaled_views = [round(v / max_view * 100) for v in user_views]

# Distractor: unused rating category mapping
rating_category = {}
for r in user_ratings:
    if r < 3.5:
        rating_category[round(r, 1)] = 'low'
    elif r < 4.0:
        rating_category[round(r, 1)] = 'medium'
    else:
        rating_category[round(r, 1)] = 'high'

# Core logic: rank calculation based on combined metrics
rank_data = []
for i in range(len(user_views)):
    view_score = scaled_views[i] * 0.6
    rating_score = user_ratings[i] * 10 * 0.4
    total_score = view_score + rating_score
    rank_data.append((i, total_score))

# Sort by score descending
rank_data.sort(key=lambda x: x[1], reverse=True)

# Bonus logic based on position and tag distribution
bonus_multiplier = 1.0
if tag_count['tech'] > 3:
    bonus_multiplier *= 1.1
if len([v for v in user_views if v > 170]) >= 3:
    bonus_multiplier *= 1.05

# Red herring: dead code path with unreachable adjustment
extreme_case_flag = False
if min(user_ratings) < 2.0:
    bonus_multiplier *= 0.8
    extreme_case_flag = True  # Never reached

# Final score computation from top 3 ranked entries
def calculate_final_score(rank_list, multiplier):
    top_scores = [rank_list[i][1] for i in range(3)]
    avg_top = sum(top_scores) / len(top_scores)
    
    # Distractor: unused intermediate transformation
    transformed = [s ** 0.5 * 10 for s in top_scores]
    
    # Actual return
    return int(avg_top * multiplier)

# Execute main logic
base_influence = sum(scaled_views) / len(scaled_views)
threshold_met = any(r > 4.2 for r in user_ratings)

# Critical execution point
final_score = calculate_final_score(rank_data, bonus_multiplier)

# Output result as required
print(f"Result: {final_score}")