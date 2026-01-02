from collections import Counter

def analyze_sentiment(text_blocks):
    sentiment_scores = []
    neutral_count = 0
    
    for block in text_blocks:
        words = block.lower().split()
        positive = ['good', 'excellent', 'great', 'well']
        negative = ['bad', 'poor', 'terrible', 'awful']
        
        pos_score = sum(1 for w in words if w in positive)
        neg_score = sum(1 for w in words if w in negative)
        
        if pos_score > neg_score:
            sentiment_scores.append('positive')
        elif neg_score > pos_score:
            sentiment_scores.append('negative')
        else:
            sentiment_scores.append('neutral')
            neutral_count += 1  # distractor: not used later
    
    return Counter(sentiment_scores)


def compute_baseline(trend_data):
    total = 0
    count = 0
    adjustment = 0.5  # red herring
    for val in trend_data:
        if val > 0:
            total += val ** 0.5
            count += 1
    return int(total / count) if count else 0


def evaluate_performance(feedbacks, base):
    score = base * 10
    multiplier = 1
    
    for category, freq in feedbacks.items():
        if category == 'positive':
            score += freq * 7
        elif category == 'negative':
            score -= freq * 5
        else:
            score += freq * 2  # neutral gives small boost
    
    # Irrelevant transformation
    temp_data = [score + i for i in range(3) if i % 2 == 0]
    temp_sum = sum(temp_data)  # dead computation
    
    if score > 100:
        multiplier = 1.1
    
    score *= multiplier
    
    # Final adjustment based on arbitrary rule
    if score % 10 == 0:
        score -= 3

    return int(score)

# Main execution
user_feedback = [
    "The service was excellent and great",
    "Poor response and terrible support",
    "Everything was good but a bit slow",
    "Not bad, not great, just well enough",
    "Excellent overall experience"
]

usage_trends = [16, 25, 9, 4]  # used to compute baseline

sentiment_distribution = analyze_sentiment(user_feedback)
baseline = compute_baseline(usage_trends)
final_score = evaluate_performance(sentiment_distribution, baseline)

print(f"Result: {final_score}")