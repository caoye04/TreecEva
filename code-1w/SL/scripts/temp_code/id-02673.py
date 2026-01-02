def calculate_entropy(values):
    from math import log2
    total = sum(values)
    entropy = 0
    for v in values:
        if v > 0:
            prob = v / total
            entropy -= prob * log2(prob)
    return entropy

# Simulate user engagement metrics across platform sections
def analyze_engagement(views, thresholds):
    high_engagement = []
    for i, v in enumerate(views):
        if v >= thresholds.get(i, 50):
            high_engagement.append(i)
    return set(high_engagement)

# Core ranking logic with distractors
def calculate_final_score(data, bonus):
    base_points = 0
    penalty = 0
    temp_result = []
    
    # Irrelevant entropy calculation (distractor)
    entropy_value = calculate_entropy([data['page_views'], data['clicks'], data['shares']])
    
    # Real scoring logic
    if data['page_views'] > 1000:
        base_points += 25
    if data['clicks'] > 500:
        base_points += 20
    if data['shares'] > 200:
        base_points += 30
    
    # Conditional expression usage
    adjustment = 10 if data['retention_rate'] >= 0.7 else -5
    base_points += adjustment
    
    # Simulated redundant string processing (distractor)
    status_msg = "High" if base_points > 50 else "Low"
    status_flag = status_msg.lower().strip() + "_engagement"
    
    # Set operations for eligible categories
    all_categories = {'tech', 'news', 'sports', 'lifestyle'}
    performance_categories = analyze_engagement(
        [data['page_views'], data['clicks'], data['shares'], data.get('watch_time', 0)],
        {0: 800, 1: 400, 2: 150, 3: 300}
    )
    eligible_boost = len(all_categories & performance_categories)
    
    # Accumulate score with bonus and irrelevant temp storage
    for i in range(eligible_boost):  # Up to 4 iterations
        temp_result.append(bonus * (i + 1))
    
    final_points = base_points + sum(temp_result[:2])  # Only first two bonuses count
    
    # Dead code path (never executed due to logic above)
    if len(temp_result) > 10:
        final_points -= 999  # unreachable
    
    return int(final_points)

# Input data
rank_data = {
    'page_views': 1250,
    'clicks': 560,
    'shares': 210,
    'retention_rate': 0.75,
    'watch_time': 320
}

bonus_multiplier = 7

# Key execution point
final_score = calculate_final_score(rank_data, bonus_multiplier)

print(f"Result: {final_score}")