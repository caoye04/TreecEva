def process_feedback(raw_text):
    cleaned = raw_text.strip().lower()
    words = cleaned.split()
    word_count = len(words)
    
    # Distractor: irrelevant sentiment analysis
    positive_terms = ['good', 'great', 'excellent', 'well']
    negative_terms = ['bad', 'poor', 'terrible', 'awful']
    pos_score = sum(1 for w in words if w in positive_terms)
    neg_score = sum(1 for w in words if w in negative_terms)
    
    # Real logic: extract numeric ratings embedded in parentheses
    ratings = []
    for word in words:
        if word.startswith('(') and word.endswith(')'):
            try:
                num = int(word[1:-1])
                if 1 <= num <= 10:
                    ratings.append(num)
            except ValueError:
                continue
    
    return ratings

def validate_ratings(rating_list):
    if not rating_list:
        return False
    # Check if all ratings are above average
    avg = sum(rating_list) / len(rating_list)
    return all(r > avg - 2 for r in rating_list)

def compute_weighted_average(rating_list):
    weights = [0.5] * len(rating_list)
    decay = 0.9
    for i in range(1, len(weights)):
        weights[i] = weights[i-1] * decay
    
    total_weighted = sum(r * w for r, w in zip(rating_list, weights))
    total_weight = sum(weights)
    return round(total_weighted / total_weight, 4)

def evaluate_performance(feedback_entries):
    all_ratings = []
    temp_debug_log = []  # Dead variable
    
    for entry in feedback_entries:
        # Simulate preprocessing step
        processed = process_feedback(entry)
        if not processed:
            continue
            
        # Distractor: analyze text structure (unused)
        sentence_length_score = max(len(e.split()) for e in entry.split('.'))
        if sentence_length_score > 20:
            flag_complex = True
        else:
            flag_complex = False
        
        # Only use validated rating sets
        if validate_ratings(processed):
            weighted_avg = compute_weighted_average(processed)
            scaled = int(round(weighted_avg * 10))
            all_ratings.append(scaled)
        else:
            # Fallback: use median
            sorted_ratings = sorted(processed)
            median_val = sorted_ratings[len(sorted_ratings)//2]
            all_ratings.append(median_val * 5)  # Different scaling
    
    # Final aggregation
    if not all_ratings:
        final = 50
    else:
        base_final = sum(all_ratings) // len(all_ratings)
        adjustment = len([r for r in all_ratings if r > 70]) * 2
        final = base_final + adjustment
        
        # Clamp to valid range
        final = max(10, min(final, 100))
    
    return final

# Main execution
raw_feedback = [
    "The service was excellent (8) and staff were great (9)",
    "Poor experience overall (3). Not recommended (2)",
    "It was good (7), but could improve (5) in some areas (6)",
    "Absolutely terrible! (1) Very disappointed.",
    "Well done! Great job! (9) (10) (8)"
]

feedback_list = raw_feedback  # Assignment for clarity

# Key statement
final_score = evaluate_performance(feedback_list)
print(f"Target result: {final_score}")