from collections import defaultdict

# Simulate user engagement metrics across content categories
def analyze_engagement(events):
    category_count = defaultdict(int)
    total_interactions = 0
    
    for event in events:
        cat = event['category']
        category_count[cat] += 1
        total_interactions += 1

    return dict(category_count), total_interactions

def normalize_scores(raw_counts, base_total):
    normalized = {}
    for k, v in raw_counts.items():
        normalized[k] = round(v / base_total * 100, 2)
    return normalized

def apply_weighting(scores_dict, weights):
    weighted = {}
    temp_debug_sum = 0  # distractor: used only for logging, not in logic
    for key, score in scores_dict.items():
        if key in weights:
            weighted[key] = score * weights[key]
        else:
            weighted[key] = score * 0.8  # default weight
        temp_debug_sum += weighted[key]  # irrelevant accumulation
    return weighted

def rank_categories(weighted_scores):
    items = list(weighted_scores.items())
    # Sort by value descending, then by key ascending (alphabetical tiebreaker)
    items.sort(key=lambda x: (-x[1], x[0]))
    return [item[0] for item in items]

def calculate_final_score(ranks, bonuses):
    score = 0
    for idx, category in enumerate(ranks):
        if idx < 3:
            score += (3 - idx) * 10  # top 3 get diminishing points
        if category in bonuses:
            score += bonuses[category]
    
    # Artificial complexity: extra loop with no impact
    adjustment = 0
    for i in range(5):  # dead computation
        adjustment += i * 0.1
    score = int(round(score + adjustment))  # adjustment has negligible effect
    
    return score

# Main execution
if __name__ == "__main__":
    # Input data: user interaction logs
    activity_log = [
        {'user': 'u1', 'action': 'view', 'category': 'gaming'},
        {'user': 'u2', 'action': 'like', 'category': 'tech'},
        {'user': 'u3', 'action': 'share', 'category': 'gaming'},
        {'user': 'u4', 'action': 'comment', 'category': 'lifestyle'},
        {'user': 'u5', 'action': 'view', 'category': 'tech'},
        {'user': 'u6', 'action': 'like', 'category': 'gaming'},
        {'user': 'u7', 'action': 'share', 'category': 'lifestyle'},
        {'user': 'u8', 'action': 'view', 'category': 'fashion'},
        {'user': 'u9', 'action': 'like', 'category': 'fashion'},
        {'user': 'u10', 'action': 'comment', 'category': 'tech'}
    ]

    # Step 1: Count occurrences per category
    counts, total = analyze_engagement(activity_log)
    
    # Step 2: Normalize to percentages
    norm_scores = normalize_scores(counts, total)
    
    # Step 3: Apply strategic importance weights
    influence_weights = {
        'gaming': 1.2,
        'tech': 1.5,
        'lifestyle': 0.9,
        'fashion': 1.1
    }
    weighted_vals = apply_weighting(norm_scores, influence_weights)
    
    # Step 4: Rank categories by influence
    ranked_categories = rank_categories(weighted_vals)
    
    # Step 5: Calculate final engagement score
    bonus_points = {
        'tech': 7,
        'gaming': 5
    }
    final_score = calculate_final_score(ranked_categories, bonus_points)
    
    # Print result as required
    print(f"Result: {final_score}")