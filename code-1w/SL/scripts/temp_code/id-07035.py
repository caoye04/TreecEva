from collections import Counter

def analyze_sentiment(text_blocks):
    sentiment_scores = []n    for block in text_blocks:
        positive_words = ['good', 'excellent', 'great', 'well']
        negative_words = ['bad', 'poor', 'terrible', 'awful']
        pos_count = sum(block.lower().count(word) for word in positive_words)
        neg_count = sum(block.lower().count(word) for word in negative_words)
        score = pos_count - neg_count
        sentiment_scores.append(score)
    return sentiment_scores

def calculate_average(values):
    if len(values) == 0:
        return 0
    total = sum(values)
    avg = total / len(values)
    return round(avg, 2)

def evaluate_performance(feedbacks, threshold):
    count_positive = 0
    total_entries = len(feedbacks)
    for fb in feedbacks:
        if fb > 0:
            count_positive += 1
    
    # Irrelevant aggregation
    temp_aggregate = 0
    for i in range(len(feedbacks)):
        temp_aggregate += abs(feedbacks[i]) * (i + 1)
    dummy_metric = temp_aggregate % 97
    
    # Actual logic path
    ratio = count_positive / total_entries if total_entries > 0 else 0
    if ratio >= threshold:
        performance_level = 1
    else:
        performance_level = 0
    
    # Secondary adjustment based on average sentiment
    avg_sentiment = calculate_average(feedbacks)
    adjustment = 1 if avg_sentiment > 0.5 else 0
    
    # Final score computation
    base_score = count_positive * 10
    bonus = 25 if adjustment and performance_level else 0
    final_score = base_score + bonus
    
    # Dead code - misleading
    if dummy_metric < 50:
        final_score -= 10  # This branch won't execute due to data
    elif dummy_metric == 0:
        final_score += 100

    return final_score

# Main execution
user_reviews = [
    "The service was excellent and worked great",
    "Poor response and bad attitude",
    "Great support, very good solutions",
    "Terrible experience overall",
    "Excellent help, everything was perfect"
]

# Step 1: Extract sentiment scores
sentiments = analyze_sentiment(user_reviews)

# Step 2: Count frequency of each sentiment level
feedback_counts = list(Counter(sentiments).values())

# Step 3: Define benchmark
benchmark_threshold = 0.6

# Step 4: Evaluate performance
final_score = evaluate_performance(feedback_counts, benchmark_threshold)

print(f"Result: {final_score}")