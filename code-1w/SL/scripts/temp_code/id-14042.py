def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'great', 'outstanding']
    negative_words = ['bad', 'poor', 'terrible', 'awful']
    words = text.lower().split()
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 2
    return score

# Simulate user feedback processing chain
def build_feedback_chain(responses):
    chain = []
    temp_buffer = []
    sentiment_map = {}
    
    for i, response in enumerate(responses):
        clean_response = response.strip().replace('!', '').replace('.', '')
        sentiment = analyze_sentiment(clean_response)
        entry = {'index': i, 'text': clean_response, 'sentiment': sentiment}
        chain.append(entry)
        temp_buffer.append(sentiment * 0.5)  # unused distraction
        
        # Misleading state tracking
        if i % 2 == 0:
            sentiment_map[f'even_{i}'] = sentiment * 0.1
    
    # Dead code: never used
    if len(temp_buffer) > 100:
        reset_buffer = True
    
    return chain

# Core evaluation logic
def evaluate_performance(chain):
    base_weight = 0.8
    adjustment_factor = 0.1
    total = 0.0
    count = 0
    
    # Lambda for dynamic threshold (actual use)
    significance_filter = lambda x: x != 0 and abs(x) >= 1
    
    for item in chain:
        raw_val = item['sentiment']
        if significance_filter(raw_val):
            total += raw_val * base_weight
            count += 1
        else:
            total += raw_val * adjustment_factor  # minor contribution
    
    # Distractor computation
    avg_sentiment = total / len(chain) if chain else 0
    volatility_index = sum([abs(item['sentiment']) for item in chain]) / len(chain) if chain else 0
    
    # Unused derived metrics
    outlier_count = len([x for x in chain if abs(x['sentiment']) > 1])
    stability_score = (count / len(chain)) * 10 if chain else 0
    
    # Final score depends only on total
    final_score = int(round(total * 10))
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Input data
user_responses = [
    "This was excellent!",
    "I had a bad experience.",
    "Great service overall.",
    "Poor quality work.",
    "Outstanding support received."
]

# Execution flow
feedback_chain = build_feedback_chain(user_responses)
final_score = evaluate_performance(feedback_chain)