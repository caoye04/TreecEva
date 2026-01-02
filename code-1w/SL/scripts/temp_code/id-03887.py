def analyze_feedback(reviews):
    positive_keywords = {'great', 'excellent', 'good', 'amazing', 'outstanding'}
    negative_keywords = {'poor', 'bad', 'terrible', 'awful', 'worst'}
    feedback_scores = []
    
    for review in reviews:
        words = review.lower().split()
        pos_count = len([w for w in words if w in positive_keywords])
        neg_count = len([w for w in words if w in negative_keywords])
        score = pos_count - neg_count
        feedback_scores.append(score)
    
    avg_sentiment = sum(feedback_scores) / len(feedback_scores) if feedback_scores else 0
    return avg_sentiment

reviews = [
    "This is excellent and great work!",
    "Terrible experience, very bad service.",
    "Good effort but could be better",
    "Outstanding quality and amazing attention to detail"
]

sentiment_value = analyze_feedback(reviews)

# Irrelevant string transformation (distractor)
uppercase_reviews = [r.upper() for r in reviews]
dummy_transform = ''.join([r[0] for r in uppercase_reviews])

# Performance metrics with multiple factors
metrics = {
    'accuracy': 0.92,
    'latency': 45,
    'throughput': 120,
    'consistency': 0.88
}

adjustments = {
    'sentiment_boost': sentiment_value * 0.1,
    'penalty_rate': 0.05 if sentiment_value < 0 else 0.02,
    'multiplier': 1.1
}

# Auxiliary computation - character frequency distractor
all_text = ' '.join(reviews).lower()
char_freq = {c: all_text.count(c) for c in set(all_text) if c.isalpha()}
top_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)[:5]

# Secondary helper function with red herring logic
def calculate_efficiency(latency, throughput, threshold=50):
    if latency < threshold:
        return throughput * 1.2
    else:
        return throughput * 0.8

# Simulated efficiency score (not directly used)
efficiency_score = calculate_efficiency(metrics['latency'], metrics['throughput'])

# Core processing logic with meaningful steps
scaling_factor = (metrics['accuracy'] + metrics['consistency']) / 2
base_performance = (metrics['throughput'] * scaling_factor) + (100 * sentiment_value)
adjusted_performance = base_performance * adjustments['multiplier']

if adjustments['penalty_rate'] > 0:
    adjusted_performance -= metrics['latency'] * adjustments['penalty_rate']

# Final aggregation incorporating set-based filtering result (dummy influence)
distinct_first_letters = len(set(dummy_transform))
final_score = int(adjusted_performance + distinct_first_letters * adjustments['sentiment_boost'] * 10)

# Print result as required
print(f"Result: {final_score}")