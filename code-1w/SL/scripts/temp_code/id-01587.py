def evaluate_performance(feedback, rating):
    # Irrelevant preprocessing
    normalized = feedback.strip().lower()
    words = normalized.split()
    word_count = len(words)
    
    # Distractor: character frequency analysis (not used in final logic)
    char_freq = {}
    for char in normalized:
        if char.isalpha():
            char_freq[char] = char_freq.get(char, 0) + 1
    
    # Semi-relevant: count positive keywords
    positive_terms = ['excellent', 'great', 'good', 'outstanding', 'impressive']
    negative_terms = ['poor', 'bad', 'terrible', 'lacking', 'weak']
    
    pos_count = sum(1 for word in words if word in positive_terms)
    neg_count = sum(1 for word in words if word in negative_terms)
    
    # Distractor: unused sentiment ratio
    if neg_count > 0:
        sentiment_ratio = pos_count / neg_count
    else:
        sentiment_ratio = pos_count + 1
    
    # Core logic begins: adjust rating based on term presence and length
    adjustment = 0
    if pos_count > neg_count:
        adjustment += 15
    elif neg_count > pos_count:
        adjustment -= 10
    
    # Additional condition based on string characteristics
    all_caps_count = sum(1 for word in words if word.isupper() and len(word) > 1)
    if all_caps_count >= 2:
        adjustment -= 5  # Over-enthusiasm penalty
    
    # Length-based bonus
    if word_count > 10:
        adjustment += 8
    
    # Critical execution point
    final_score = rating + adjustment
    
    # Dead code path - never executed due to logic above
    if word_count == 1000:
        final_score *= 2
    
    return final_score

# Main execution
base_rating = 65
feedback_str = "The performance was GREAT and IMPRESSIVE, truly excellent work overall."

# Extra irrelevant variables
avg_word_length = sum(len(w) for w in feedback_str.split()) / len(feedback_str.split())
symbol_count = feedback_str.count(',') + feedback_str.count('.')

final_score = evaluate_performance(feedback_str, base_rating)
print(f"Result: {final_score}")