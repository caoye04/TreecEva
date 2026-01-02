def analyze_feedback(scores, weights):
    weighted_sum = 0
    total_weight = 0
    temp_debug = []
    for i, (score, weight) in enumerate(zip(scores, weights)):
        if score < 0:
            temp_debug.append(f'Invalid score at {i}')
            continue
        weighted_sum += score * weight
        total_weight += weight
    
    # Distractor: unused normalization
    normalized = [s / max(scores) for s in scores if s > 0]
    average = weighted_sum / total_weight if total_weight else 0
    
    return average


def calculate_compatibility(features_a, features_b):
    set_a = set(features_a)
    set_b = set(features_b)
    intersection = set_a & set_b
    union = set_a | set_b
    jaccard = len(intersection) / len(union) if union else 0
    
    # Distractor: irrelevant transformation
    squared_diffs = [(a - b) ** 2 for a, b in zip(features_a, features_b)]
    
    return jaccard


def calculate_final_score(rankings, preferences):
    base_score = 0
    penalty = 0
    
    # Real logic: count how many rankings match preferred categories
    for rank, item in enumerate(rankings):
        if item in preferences['top_categories']:
            base_score += (5 - rank)  # higher rank = more points
        
        # Distractor: misleading category tracking
        temp_tracker = {}
        for cat in preferences['top_categories']:
            temp_tracker[cat] = temp_tracker.get(cat, 0) + 1
    
    # Real logic: apply multiplier if top pick matches favorite
    if rankings[0] == preferences['favorite']:
        base_score *= 2
    
    # Distractor: dead code path (never executed due to structure)
    debug_stats = {}
    for k, v in preferences.items():
        if isinstance(v, list):
            debug_stats[k] = len(v)
        elif k == 'rare_key':
            debug_stats['special'] = 999  # unreachable

    # Real logic: subtract penalty based on length mismatch
    expected_len = preferences.get('expected_rankings', 5)
    if len(rankings) != expected_len:
        penalty += abs(len(rankings) - expected_len)
    
    final = base_score - penalty
    
    # Key assignment point
    final_score = int(final)
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    user_feedback = [4.5, 3.0, 5.0, 2.5, -1.0]
    importance_weights = [0.2, 0.3, 0.1, 0.2, 0.2]
    
    # Unused but plausible distractor variables
    system_threshold = 3.5
    calibration_data = [0.1, 0.5, 0.3]
    adjustment_factor = sum(calibration_data) / len(calibration_data)
    
    # Real inputs
    product_rankings = ['electronics', 'books', 'clothing', 'home', 'toys']
    user_prefs = {
        'favorite': 'electronics',
        'top_categories': ['electronics', 'books', 'sports'],
        'expected_rankings': 5,
        'theme': 'tech_lover'
    }
    
    # Distractor: unused helper call
    compatibility = calculate_compatibility([1,2,3], [3,2,1])
    
    # Distractor: intermediate analysis with side-effect-free function
    avg_feedback = analyze_feedback(user_feedback, importance_weights)
    
    # Key statement
    final_score = calculate_final_score(product_rankings, user_prefs)
    
    print(f"Result: {final_score}")