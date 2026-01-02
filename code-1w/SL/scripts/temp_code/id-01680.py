def analyze_sentiment(text_blocks):
    sentiment_scores = []
    for block in text_blocks:
        positive_words = {"great", "good", "excellent", "happy", "pleased"}
        negative_words = {"bad", "terrible", "awful", "unhappy", "poor"}
        words = block.lower().split()
        pos_count = len([w for w in words if w in positive_words])
        neg_count = len([w for w in words if w in negative_words])
        score = pos_count - neg_count
        sentiment_scores.append(score)
    return sentiment_scores


def compute_reliability(confidence_levels):
    reliability = 0
    for i, conf in enumerate(confidence_levels):
        reliability += (i + 1) * conf  # Weighted by position
    return reliability / len(confidence_levels) if confidence_levels else 0


def evaluate_performance(feedback_set, weights):
    # Core logic starts here
    raw_scores = analyze_sentiment(feedback_set)
    
    # Irrelevant helper: counts characters per feedback (not used in final score)
    total_chars = sum(len(fb) for fb in feedback_set)
    char_frequency_map = {chr(i): total_chars % (i+1) for i in range(97, 100)}  # a-c only, red herring

    # Distractor variables
    temp_adjustment = 0
    for k, v in char_frequency_map.items():
        temp_adjustment += ord(k) % v if v != 0 else 0  # unused later

    # Actual computation begins
    weighted_sum = 0
    max_score = 0
    for idx, (score, weight) in enumerate(zip(raw_scores, weights)):
        adjusted = score * weight
        if adjusted > 0:
            max_score = max(max_score, adjusted)
        weighted_sum += adjusted
    
    # Secondary logic: count how many feedbacks had net positive sentiment
    positive_feedback_count = sum(1 for s in raw_scores if s > 0)
    bonus = 5 if positive_feedback_count >= 2 else 0
    
    # Final score calculation
    final_score = weighted_sum + bonus
    
    # Dead code path - never executed due to fixed condition
    if False and temp_adjustment > 100:
        final_score *= 1.1
        outlier_flag = True
    
    return final_score

# Main execution
feedback_texts = [
    "The team did a great job and was excellent overall",
    "Poor execution and bad timing ruined the event",
    "Excellent work, really pleased with the results"
]

weights = [0.5, 0.3, 0.7]

# Unused but plausible-looking data structures
auxiliary_data = list(zip(feedback_texts, [len(t) for t in feedback_texts]))
index_mapping = {i: txt for i, txt in enumerate(feedback_texts)}

final_score = evaluate_performance(feedback_texts, weights)
print(f"Target result: {final_score}")