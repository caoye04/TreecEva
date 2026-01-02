def process_feedback(reviews, weights):
    base_score = 5.0
    adjustment = 0.0
    temp_sum = 0
    count_valid = 0
    
    # Irrelevant pre-processing (distractor)
    normalized_weights = {k: v / sum(weights.values()) for k in weights}
    weight_factor = sum([v**2 for v in weights.values()])  # Unused computation

    for category, reviews_list in reviews.items():
        if category not in weights:
            continue
        
        category_total = 0
        review_count = 0
        
        for entry in reviews_list:
            # String cleaning (semi-relevant)
            clean_entry = entry.strip().lower()
            if 'n/a' in clean_entry or len(clean_entry) == 0:
                continue
            
            try:
                # Extract numeric rating from string like "rating: 4"
                parts = clean_entry.split(':')
                if len(parts) >= 2:
                    raw_val = parts[1].strip()
                    if raw_val.isdigit():
                        val = int(raw_val)
                        if 1 <= val <= 10:
                            category_total += val
                            review_count += 1
                            temp_sum += val  # Accumulates across categories but used later
            except:
                continue
        
        if review_count > 0:
            avg = category_total / review_count
            adjustment += (avg - base_score) * weights[category]
            count_valid += 1

    # Additional distraction: unused logic
    if count_valid == 0:
        final_adjustment = 0
    else:
        final_adjustment = adjustment / count_valid if count_valid > 1 else adjustment

    # Final score calculation (key result)
    final_score = base_score + (adjustment * 0.8)
    
    # Dead code path (irrelevant)
    debug_snapshot = {
        'intermediate': [base_score, adjustment],
        'meta': f'Score computed with {count_valid} categories'
    }
    
    return round(final_score, 4)

# Input data
reviews = {
    'usability': ['Rating: 7', 'Feedback: n/a', 'Score: 9'],
    'performance': ['Value: 6', '', 'rating: 5'],
    'design': ['rating: 8', 'comment: great', 'rate: 3']
}

weights = {
    'usability': 0.5,
    'performance': 0.3,
    'design': 0.2
}

# Execution
final_score = process_feedback(reviews, weights)
print(f"Result: {final_score}")