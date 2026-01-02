from collections import Counter

def analyze_sentiment(feedback):
    positive_words = {'good', 'great', 'excellent', 'amazing', 'awesome'}
    negative_words = {'bad', 'terrible', 'awful', 'poor', 'worst'}
    neutral_words = {'okay', 'fine', 'average', 'decent'}

    word_count = Counter(feedback.lower().split())
    
    pos_score = sum(word_count[word] for word in positive_words if word in word_count)
    neg_score = sum(word_count[word] for word in negative_words if word in word_count)
    neu_score = sum(word_count[word] for word in neutral_words if word in word_count)

    sentiment_balance = pos_score - neg_score + (neu_score // 3)
    return max(sentiment_balance, 0)


def calculate_stability(metric_history):
    diffs = [abs(metric_history[i] - metric_history[i-1]) for i in range(1, len(metric_history))]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    stability = 100 - (avg_diff * 5)
    return round(stability, 2)


def process_feedback(reliability_factor, feedback_log):
    # Irrelevant intermediate computation (distractor)
    temp_data = [len(entry.split()) for entry in feedback_log]
    avg_length = sum(temp_data) / len(temp_data)
    length_influence = int(avg_length * 0.7)  # Not used in final logic

    raw_sentiment = sum(analyze_sentiment(entry) for entry in feedback_log)
    
    # Misleading normalization step
    normalized_sentiment = raw_sentiment / len(feedback_log) if feedback_log else 0
    adjusted_sentiment = int(normalized_sentiment * 1.5)

    # Stability from metrics (semi-relevant but overcomplicated)
    dummy_metrics = [95, 87, 90, 88, 92]
    system_stability = calculate_stability(dummy_metrics)
    stability_bonus = int(system_stability // 10)

    # Core logic: combine reliability and sentiment
    base_score = reliability_factor * 10
    feedback_weight = 3
    score_contribution = adjusted_sentiment * feedback_weight
    
    final_score = base_score + score_contribution + stability_bonus
    
    # Dead code path (distractor)
    if False:
        fallback = sum(ord(c) for c in "error") % 100
        final_score = fallback

    return final_score

# Main execution
reliability = 7
feedback_list = [
    "The system is excellent and amazing, really awesome",
    "Not bad, pretty good overall",
    "Terrible performance, very poor results",
    "Great speed and excellent responsiveness"
]

final_score = process_feedback(reliability, feedback_list)
print(f"Target result: {final_score}")