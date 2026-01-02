def calculate_performance_rating():
    # Employee performance evaluation system based on metrics
    base_scores = [85, 90, 78, 92, 88]
    weights = [0.2, 0.3, 0.15, 0.25, 0.1]
    
    # Irrelevant distraction: unused metric tracking
    debug_log = []
    temp_factor = 1.05
    adjustment_offset = -2  # Not actually used in final logic
    
    weighted_total = 0
    for i, (score, weight) in enumerate(zip(base_scores, weights)):
        if score >= 80:
            boosted_score = score * temp_factor  # Boost high performers (but not used)
            debug_log.append(f'High performer {i}: {boosted_score}')
        weighted_total += score * weight
    
    # Secondary processing with conditional expression
    bonus_eligibility = 'yes' if weighted_total > 85 else 'no'
    bonus_multiplier = 1.1 if bonus_eligibility == 'yes' else 1.0
    
    # Complex data structure: performance bands
    bands = {
        'exceeds': (90, float('inf')),
        'meets': (80, 89),
        'needs_improvement': (0, 79)
    }
    
    # Determine band using dictionary lookup and comparison
    performance_band = None
    for band, (low, high) in bands.items():
        if low <= weighted_total <= high:
            performance_band = band
            break
    
    # Additional irrelevant computation
    avg_base = sum(base_scores) / len(base_scores)
    variance_estimate = sum((x - avg_base) ** 2 for x in base_scores) / len(base_scores)
    stability_index = 100 - variance_estimate  # Unused statistic
    
    # Final scoring with nested logic
    if performance_band == 'exceeds':
        base_rating = 5
    elif performance_band == 'meets':
        base_rating = 3
    else:
        base_rating = 1
    
    # Apply bonus only if eligible
    final_score = base_rating * bonus_multiplier
    
    # More red herring variables
    normalized_score = (final_score / 5) * 100
    scaling_factor = 0.95 + (weighted_total / 1000)  # Distractor
    
    return final_score

# Key execution point
final_score = calculate_performance_rating()
print(f"Result: {final_score}")