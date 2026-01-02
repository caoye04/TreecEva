def aggregate_performance(feedback, weight_map):
    base_scores = {k: len(v) * 1.5 for k, v in feedback.items()}
    
    # Irrelevant computation: counting duplicate entries (never used)
    flattened = [item for sublist in feedback.values() for item in sublist]
    duplicate_count = len(flattened) - len(set(flattened))
    temp_bias = duplicate_count * 0.1

    # Semi-relevant transformation: normalize keys (only some affect result)
    normalized_keys = {k.lower(): k for k in weight_map.keys()}
    adjusted_weights = {k: weight_map[normalized_keys.get(k, k)] for k in feedback.keys()}
    
    # Core logic with conditional expression and set operations
    raw_contributions = []
    for category, entries in feedback.items():
        unique_entries = set(entries)
        entry_count = len(unique_entries)
        
        # Conditional expression determining scaling factor
        scaling = 1.2 if entry_count >= 3 else 0.8
        
        # Additional distraction: unused trend analysis
        trend_direction = 'positive' if all(x.isdigit() for x in unique_entries[:2]) else 'neutral'
        trend_factor = 1.1 if trend_direction == 'positive' else 1.0
        
        contribution = entry_count * scaling
        raw_contributions.append(contribution)
    
    # Weighted aggregation using dictionary lookup
    weighted_contributions = [
        raw_contributions[i] * adjusted_weights[list(feedback.keys())[i]]
        for i in range(len(raw_contributions))
    ]
    
    # Final score calculation
    total_raw = sum(raw_contributions)
    total_weighted = sum(weighted_contributions)
    final_score = int((total_weighted / len(weighted_contributions)) + 0.5) if weighted_contributions else 0
    
    # Print target result
    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_set = {
    'Usability': ['smooth', 'intuitive', 'smooth', 'responsive'],
    'Performance': ['fast', 'laggy', 'fast', 'optimized', 'efficient'],
    'Design': ['aesthetic', 'modern']
}
weights = {'usability': 1.4, 'performance': 2.0, 'design': 1.0}

# Execute and capture result
final_score = aggregate_performance(feedback_set, weights)