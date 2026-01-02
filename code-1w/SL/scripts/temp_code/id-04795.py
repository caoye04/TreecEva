from collections import defaultdict, Counter

# Simulate user engagement data across different content categories
def analyze_engagement_metrics():
    raw_interactions = [120, 150, 95, 200, 175, 130, 180, 210]
    category_tags = ['tech', 'lifestyle', 'tech', 'finance', 'lifestyle', 'tech', 'finance', 'tech']
    
    # Irrelevant distraction: unused transformation
    transformed_scores = [x * 1.1 + 5 for x in raw_interactions if x > 100]
    filtered_mask = [x > 140 for x in raw_interactions]

    # Aggregate interactions by category
    category_totals = defaultdict(int)
    for tag, score in zip(category_tags, raw_interactions):
        category_totals[tag] += score

    # Additional distraction: unused counter logic
    tag_frequency = Counter(category_tags)
    rare_categories = [tag for tag, count in tag_frequency.items() if count < 2]

    # Normalize scores to create rank data
    total_sum = sum(category_totals.values())
    rank_data = {tag: round((score / total_sum) * 100, 2) for tag, score in category_totals.items()}

    # Bonus weights based on alphabetical priority (arbitrary but deterministic)
    sorted_tags = sorted(rank_data.keys())
    bonus_weights = {tag: 1 + i * 0.1 for i, tag in enumerate(sorted_tags)}

    # Dead code path: never executed due to prior filtering
    def legacy_adjustment(x):
        return x * 0.95 if x > 50 else x * 1.05

    # Core calculation with mixed operations
    base_score = sum(rank_data.values())
    weight_factor = sum(bonus_weights[tag] for tag in rank_data if tag in bonus_weights)
    adjustment = len(category_totals) * 0.25
    
    # Final computation
    final_score = (base_score * weight_factor) - adjustment
    
    # Distraction: unused list comprehension with side-effect-free calls
    _ = [len(tag) for tag in category_tags if tag.startswith('t')]
    
    # Output result as required
    print(f"Result: {final_score}")
    
    return final_score

# Execute function
def calculate_final_score(ranks, weights):
    base = sum(ranks.values())
    factor = sum(weights.get(k, 1) for k in ranks)
    adj = len(ranks) * 0.25
    return (base * factor) - adj

result = analyze_engagement_metrics()
