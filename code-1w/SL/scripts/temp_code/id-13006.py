from collections import Counter, defaultdict

# Simulate user feedback analysis for a training module
def analyze_feedback(responses):
    sentiment_count = Counter()
    total_entries = 0
    irrelevant_sum = 0  # Distractor: not used later

    for entry in responses:
        sentiment = entry['sentiment']
        sentiment_count[sentiment] += 1
        total_entries += 1

        # Dead computation - doesn't affect logic
        if sentiment == 'neutral':
            irrelevant_sum += len(entry['comment'])

    return sentiment_count, total_entries

def calculate_bias_metric(sentiments):
    pos = sentiments.get('positive', 0)
    neg = sentiments.get('negative', 0)
    bias_score = 0
    if pos + neg > 0:
        bias_score = (pos - neg) / (pos + neg)
    
    # Extra calculation with no impact
    adjustment = 0.1 if bias_score > 0.5 else 0.05
    adjusted_bias = bias_score + adjustment  # Unused variable
    return bias_score

def evaluate_performance(feedback_set, ratings_counter):
    base_score = 0
    penalty = 0
    
    # Meaningful logic: count valid positive signals
    for tag in feedback_set:
        if tag.startswith('success'):
            base_score += 3
        elif tag.startswith('error'):
            penalty += 2
    
    # Use of Counter: extract frequency-based metric
    high_ratings = sum(count for rating, count in ratings_counter.items() if rating >= 4)
    low_ratings = sum(count for rating, count in ratings_counter.items() if rating <= 2)
    medium_ratings = ratings_counter.get(3, 0)
    
    # Secondary distraction: computed but not critical
    avg_offset = (high_ratings - low_ratings) / (medium_ratings + 1)
    stability_factor = 1 if abs(avg_offset) < 2 else 0.8
    
    # Core scoring logic
    raw_performance = base_score - penalty
    scaled_performance = raw_performance * (1 + 0.1 * (high_ratings - low_ratings))
    
    # Final decision branch
    if high_ratings > low_ratings and 'success_critical' in feedback_set:
        scaled_performance *= 1.2
    
    return int(scaled_performance)

# Main execution
if __name__ == "__main__":
    user_responses = [
        {'sentiment': 'positive', 'comment': 'good flow'},
        {'sentiment': 'positive', 'comment': 'well structured'},
        {'sentiment': 'negative', 'comment': 'too fast'},
        {'sentiment': 'neutral', 'comment': 'ok'},
        {'sentiment': 'positive', 'comment': 'great examples'}
    ]
    
    ratings = [5, 4, 3, 5, 2, 1, 4, 5]
    ratings_counter = Counter(ratings)
    feedback_tags = {"success_basic", "success_advanced", "error_ui", "success_critical"}
    
    # Analyze sentiment (distractor: used to create noise)
    sentiment_dist, total = analyze_feedback(user_responses)
    bias_metric = calculate_bias_metric(sentiment_dist)
    
    # Key statement
    final_score = evaluate_performance(feedback_tags, ratings_counter)
    
    # Output result as required
    print(f"Result: {final_score}")