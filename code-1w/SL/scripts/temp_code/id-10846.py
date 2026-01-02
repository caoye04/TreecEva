from collections import defaultdict

# Simulate user interaction logs with feature usage counts
interaction_logs = [
    ('feature_a', 'user1'), ('feature_b', 'user2'), ('feature_a', 'user3'),
    ('feature_c', 'user1'), ('feature_b', 'user3'), ('feature_a', 'user2'),
    ('feature_c', 'user3'), ('feature_b', 'user1'), ('feature_a', 'user1')
]

# Track how many times each user interacts with each feature
detailed_tracker = defaultdict(lambda: defaultdict(int))
user_engagement = defaultdict(int)
feature_popularity = {}
baseline_offset = 7

for feature, user in interaction_logs:
    detailed_tracker[feature][user] += 1
    user_engagement[user] += 1

# Compute total interactions per feature
for feature in detailed_tracker:
    feature_popularity[feature] = sum(detailed_tracker[feature].values())

# Misleading intermediate calculation - not used later
phantom_score = 0
for user in user_engagement:
    if user_engagement[user] > 2:
        phantom_score += 10
    else:
        phantom_score += 3

# Actual signal: count distinct users per feature
distinct_users = {feat: len(detailed_tracker[feat]) for feat in detailed_tracker}

# Simulate qualitative feedback scores (e.g., survey data)
raw_feedback = {
    'feature_a': [4, 5, 3, 4],
    'feature_b': [2, 3, 3],
    'feature_c': [5, 5]
}

# Average feedback per feature
feedback_averages = {}
for feat, ratings in raw_feedback.items():
    feedback_averages[feat] = round(sum(ratings) / len(ratings), 2)

# Normalize around baseline satisfaction (arbitrary anchor)
normalized_sentiment = {}
for feat in feedback_averages:
    normalized_sentiment[feat] = feedback_averages[feat] - 3.5  # neutral threshold

# Combine engagement (distinct users) and sentiment into performance score
def aggregate_performance(sentiment_map):
    total_weighted = 0.0
    for feature, net_sentiment in sentiment_map.items():
        # Weight by number of distinct users who used the feature
        user_count = distinct_users[feature]
        total_weighted += user_count * net_sentiment
    return round(total_weighted, 2)

# Key statement
final_score = aggregate_performance(normalized_sentiment)

# Distractor: unused transformation
consolidated_report = []
for feature in feature_popularity:
    consolidated_report.append({
        'feature': feature,
        'total_uses': feature_popularity[feature],
        'satisfaction_delta': normalized_sentiment[feature]
    })

# Output the target result
print(f"Target result: {final_score}")