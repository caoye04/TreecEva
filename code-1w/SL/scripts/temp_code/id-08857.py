def analyze_sentiment(text_data):
    if not text_data:
        return 0
    
    # Irrelevant processing: character counting and case conversion
    upper_count = sum(1 for c in text_data if c.isupper())
    lower_count = sum(1 for c in text_data if c.islower())
    total_chars = len(text_data)
    ratio = upper_count / total_chars if total_chars > 0 else 0
    
    # Distractor computation
    temp_value = (upper_count * 2 + lower_count) % 7
    
    # Actual sentiment signal: count exclamation marks
    excitement_level = text_data.count('!')
    return excitement_level


def normalize_scores(raw_scores):
    if not raw_scores:
        return []
    max_score = max(raw_scores)
    min_score = min(raw_scores)
    range_score = max_score - min_score or 1
    
    # List comprehension: relevant transformation
    normalized = [(x - min_score) / range_score for x in raw_scores]
    
    # Dead code path (irrelevant)
    if len(normalized) > 10:
        smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
    else:
        smoothed = normalized[:]  # Copy, not used later
    
    return normalized

def evaluate_performance(feedback_list):
    sentiment_scores = []
    dummy_accumulator = 0  # Misleading variable
    
    for entry in feedback_list:
        # Extract feedback string
        feedback_text = entry.get('feedback', '')
        rating = entry.get('rating', 0)
        
        # Compute sentiment from text
        sent_score = analyze_sentiment(feedback_text)
        
        # Irrelevant bitwise manipulation
        masked_rating = rating ^ 3
        dummy_accumulator += masked_rating & 1  # Useless accumulation
        
        # Core logic: combine rating and sentiment
        adjusted_score = rating + sent_score * 2
        sentiment_scores.append(adjusted_score)
    
    # Normalize scores using helper function
    norm_scores = normalize_scores(sentiment_scores)
    
    # Aggregate final result
    if norm_scores:
        final_value = sum(norm_scores) * 100
    else:
        final_value = 0
    
    # Early return not taken (distractor control flow)
    if final_value < 0:
        return -1
    
    # Key assignment
    final_score = int(final_value)
    return final_score

# Input data
feedback_entries = [
    {'feedback': 'Great service!', 'rating': 4},
    {'feedback': 'Poor experience.', 'rating': 2},
    {'feedback': 'Absolutely fantastic!!!', 'rating': 5},
    {'feedback': 'Okay, nothing special', 'rating': 3}
]

# Execution point of interest
final_score = evaluate_performance(feedback_entries)
print(f"Result: {final_score}")