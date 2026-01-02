from collections import Counter

def analyze_sentiment(text_list):
    sentiment_scores = {'positive': 0, 'negative': 0, 'neutral': 0}
    word_freq = Counter()
    
    for text in text_list:
        words = text.lower().split()
        word_freq.update(words)
        
        if 'excellent' in words or 'great' in words:
            sentiment_scores['positive'] += 1
        elif 'poor' in words or 'terrible' in words:
            sentiment_scores['negative'] += 1
        else:
            sentiment_scores['neutral'] += 1
    
    return sentiment_scores, word_freq

def compute_baseline(trend_data):
    total = 0
    count = 0
    for val in trend_data:
        if val > 0:
            total += val ** 0.5
            count += 1
    return total / count if count else 0

def evaluate_performance(feedback_counts, adj_factor):
    base = sum(feedback_counts.values())
    bonus = 0
    
    if feedback_counts['positive'] > feedback_counts['negative']:
        bonus += 15
    
    # Irrelevant transformation
    temp_vals = [v * 2 for v in feedback_counts.values()]
    temp_sum = sum(temp_vals)  # Unused variable (distractor)
    
    penalty = 0
    if feedback_counts['negative'] > 0:
        penalty = 10
    
    raw_score = base + bonus - penalty
    adjusted_score = raw_score * adj_factor
    
    # Dead code path (conditional never reached in current logic)
    if len(temp_vals) > 100:
        adjusted_score *= 0.9
    
    return int(adjusted_score)

def main():
    reviews = [
        "The product was excellent and great",
        "Terrible quality and poor design",
        "It's acceptable, nothing special",
        "Great build and excellent features",
        "Poor customer support"
    ]
    
    trends = [4, 9, 16, 25]
    
    sentiments, freq_map = analyze_sentiment(reviews)
    
    # Compute baseline (unused in final result - distractor)
    baseline = compute_baseline(trends)
    
    # Transform frequency map into score-like metric (semi-relevant)
    adjustment_factor = 1.0
    if freq_map.get('great', 0) >= 2:
        adjustment_factor += 0.2
    if 'poor' in freq_map:
        adjustment_factor -= 0.1
    
    # Simulate auxiliary state tracking
    session_log = []
    session_log.append(f'Processed {len(reviews)} reviews')
    session_log.append(f'Unique words: {len(freq_map)}')
    
    # Key execution point
    final_score = evaluate_performance(sentiments, adjustment_factor)
    
    # Print required output
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()