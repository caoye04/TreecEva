def analyze_feedback(rating_str, review_text):
    rating = float(rating_str.strip())
    word_count = len(review_text.split())
    char_count = len(review_text.replace(' ', ''))
    
    # Secondary metrics (slightly distracting but plausible)
    sentiment_hint = review_text.lower().count('good') - review_text.lower().count('bad')
    exclamation_rich = review_text.count('!') > 2
    
    if rating >= 4.0 and word_count > 50:
        base_score = 90
    elif rating >= 3.0 and word_count > 30:
        base_score = 70
    else:
        base_score = 50

    length_bonus = 10 if word_count > 60 else 5 if word_count > 40 else 0
    clarity_penalty = 5 if char_count / (word_count + 1) > 6.5 else 0
    
    final_score = base_score + length_bonus - clarity_penalty
    
    # Conditional expression using string method
    feedback_type = 'detailed' if 'detailed' in review_text.lower() else 'generic'
    final_score += 5 if feedback_type == 'detailed' and sentiment_hint > 0 else 0
    
    return final_score

# Input data
rating_input = "4.5"
review = "This is a detailed and thorough review! I really enjoyed the features. Excellent work!!!"

result = analyze_feedback(rating_input, review)
final_score = result
print(f"Result: {final_score}")