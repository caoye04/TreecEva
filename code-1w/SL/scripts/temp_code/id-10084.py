def analyze_sentiment(text):
    sentiment_score = 0
    positive_words = ['good', 'excellent', 'great', 'well']
    negative_words = ['poor', 'bad', 'terrible', 'awful']
    words = text.lower().split()
    for word in words:
        if word in positive_words:
            sentiment_score += 1
        elif word in negative_words:
            sentiment_score -= 1
    return sentiment_score

# Simulate system health check (distractor function)
def compute_health_factor(uptime, load):
    if uptime < 100:
        return 0.5 * uptime / (load + 1)
    else:
        return 1.0

# Main evaluation logic
def evaluate_performance(feedback_log, metrics):
    base_value = metrics['initial']
    adjustment = 0
    total_entries = 0
    sentiment_sum = 0
    
    # Track character frequency (semi-relevant computation)
    char_freq = {}
    for entry in feedback_log:
        cleaned = entry.replace(' ', '').lower()
        for c in cleaned:
            char_freq[c] = char_freq.get(c, 0) + 1
    
    # Analyze each feedback and adjust score
    for entry in feedback_log:
        total_entries += 1
        sent_score = analyze_sentiment(entry)
        sentiment_sum += sent_score
        
        # Additional logic based on entry length (misleading path)
        if len(entry) > 20:
            adjustment += 2
        elif len(entry) > 10:
            adjustment += 1
    
    # Irrelevant health computation (distractor)
    dummy_health = compute_health_factor(150, 3)
    unused_diagnostic = {'status': 'ok', 'level': dummy_health}
    
    # Core calculation
    avg_sentiment = sentiment_sum / total_entries if total_entries else 0
    stability_bonus = 1 if metrics['fluctuation'] < 0.5 else -2
    final_score = base_value + adjustment + int(avg_sentiment) + stability_bonus
    
    # Dead code branch (minor interference)
    if False:
        final_score = -999  # unreachable

    return final_score

# Input data
feedback_responses = [
    "The service was excellent and worked well throughout",
    "Poor connection and bad user interface",
    "Great speed but terrible support",
    "Everything was good and great"
]

base_metrics = {
    'initial': 10,
    'fluctuation': 0.3,
    'version': 2.1
}

# Execution point of interest
final_score = evaluate_performance(feedback_responses, base_metrics)
print(f"Result: {final_score}")