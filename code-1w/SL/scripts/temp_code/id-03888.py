def analyze_sentiment(texts):
    sentiment_scores = {}
    for text in texts:
        words = text.lower().split()
        positive_count = sum(1 for w in words if w in ['good', 'excellent', 'great', 'amazing'])
        negative_count = sum(1 for w in words if w in ['bad', 'terrible', 'awful', 'poor'])
        sentiment_scores[text[:10]] = positive_count - negative_count
    return sentiment_scores

feedback_samples = [
    "This product is excellent and amazing!",
    "Terrible quality and poor service.",
    "Great experience overall, good support.",
    "Amazing features but bad user interface."
]

sentiments = analyze_sentiment(feedback_samples)

# Irrelevant aggregation (distractor)
total_chars = sum(len(s) for s in feedback_samples)
mean_length = total_chars / len(feedback_samples) if feedback_samples else 0

# Simulate confidence levels for each feedback (unused later)
confidence_levels = {key: abs(score) * 0.5 for key, score in sentiments.items()}

# Real processing begins: extract magnitude trends
magnitude_trend = [abs(v) for v in sentiments.values()]
high_impact_count = sum(1 for m in magnitude_trend if m >= 2)

# Secondary analysis: character frequency in keys (distraction)
key_chars = ''.join(sentiments.keys())
char_frequency = {}
for c in key_chars:
    char_frequency[c] = char_frequency.get(c, 0) + 1

# Filter top characters (irrelevant to final result)
top_chars = sorted(char_frequency, key=char_frequency.get, reverse=True)[:3]

# Core logic disguised among distractions
def evaluate_performance(feedback_dict, min_threshold):
    raw_values = list(feedback_dict.values())
    midpoint = len(raw_values) // 2
    first_half_avg = sum(raw_values[:midpoint]) / midpoint if midpoint > 0 else 0
    second_half_avg = sum(raw_values[midpoint:]) / (len(raw_values) - midpoint) if len(raw_values) > midpoint else 0
    
    # Hidden slicing pattern
    deltas = [second_half_avg - first_half_avg]
    if len(raw_values) > 3:
        recent_change = raw_values[-1] - raw_values[-2]
        deltas.append(recent_change)
    
    trend_boost = sum(deltas) * 10
    base_performance = sum(abs(v) for v in raw_values)
    adjustment = 5 if len([v for v in raw_values if v > 0]) > len(raw_values) / 2 else -5
    
    # Actual answer computation
    result = int(base_performance + trend_boost + adjustment)
    
    # Dead code path (red herring)
    if result < 0:
        result = abs(result)  # never reached due to data
    
    return result

threshold = 1.5
feedback_data = sentiments

# Key execution point
calibration_offset = sum(1 for k in char_frequency if k in 'aeiou') * 0.5  # unused
final_score = evaluate_performance(feedback_data, threshold)
print(f"Result: {final_score}")