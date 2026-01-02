def analyze_feedback(responses):
    sentiment_scores = []
    for response in responses:
        clean_response = response.strip().lower()
        if 'excellent' in clean_response:
            sentiment_scores.append(5)
        elif 'good' in clean_response:
            sentiment_scores.append(4)
        elif 'average' in clean_response:
            sentiment_scores.append(3)
        elif 'poor' in clean_response:
            sentiment_scores.append(2)
        elif 'terrible' in clean_response:
            sentiment_scores.append(1)
        else:
            sentiment_scores.append(3)  # neutral default
    return sentiment_scores

# Simulated user feedback strings
feedback_strings = [
    '   Excellent service and fast delivery!   ',
    'The product was good but packaging could improve.',
    'Average experience overall.',
    'Poor quality, very disappointed.',
    'Terrible! Will not buy again.',
    'It\'s okay, nothing special.'
]

# Extract sentiment
sentiments = analyze_feedback(feedback_strings)

# Misleading distraction: irrelevant text analysis
word_count = 0
for text in feedback_strings:
    word_count += len(text.split())
fake_metric = word_count * 0.75

# Real metrics processing
metrics = {
    'response_count': len(feedback_strings),
    'avg_sentiment': sum(sentiments) / len(sentiments),
    'consistency': sentiments.count(max(set(sentiments), key=sentiments.count)),
    'trend': sentiments[-1] - sentiments[0]  # change from first to last
}

# Thresholds for scoring
thresholds = {
    'high_performance': 4.0,
    'moderate_performance': 2.5,
    'low_penalty': -1.0
}

# Distractor variables
baseline_adjustment = 0.5
normalization_factor = 1.0 / (len(sentiments) + 1e-8)
phantom_score = (sum(sentiments) * normalization_factor) + baseline_adjustment

# Core logic with slicing and string methods
recent_trend = feedback_strings[-3:]  # last three responses
recent_analysis = [r.lower().replace('!', '').replace('.', '') for r in recent_trend]
dynamic_weight = len([r for r in recent_analysis if 'good' in r or 'excellent' in r])

# Main processing function
def process_performance(perf_metrics, limits):
    score = 0
    
    if perf_metrics['avg_sentiment'] > limits['high_performance']:
        score += 40
    elif perf_metrics['avg_sentiment'] > limits['moderate_performance']:
        score += 30
    else:
        score += 15
    
    if perf_metrics['consistency'] >= 2:
        score += 10
    
    if perf_metrics['trend'] >= 0:
        score += 5
    else:
        score -= 3
    
    # Bonus based on recent positive mentions (uses list comprehension and string containment)
    recent_positive_bonus = 0
    for entry in recent_analysis:
        if 'excellent' in entry or 'good' in entry:
            recent_positive_bonus += 2
    score += min(recent_positive_bonus, 6)
    
    # Irrelevant adjustment (distractor)
    dummy_shift = 0
    for i in range(3):
        dummy_shift += (score % (i + 2))
    final_normalized = score - dummy_shift + 0.0  # fake refinement
    
    return int(score)  # deterministic integer result

# Execute main computation
final_score = process_performance(metrics, thresholds)

# Output result as required
print(f"Result: {final_score}")