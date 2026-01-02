def analyze_sentiment(texts):
    sentiment_scores = []
    neutral_count = 0
    temp_multiplier = 1.0

    for i, text in enumerate(texts):
        clean_text = text.strip().lower()
        positive_words = ['good', 'excellent', 'great']
        negative_words = ['bad', 'poor', 'terrible']

        pos_count = sum(1 for word in positive_words if word in clean_text)
        neg_count = sum(1 for word in negative_words if word in clean_text)

        if pos_count > neg_count:
            score = len(clean_text) % 10 + pos_count * 2
        elif neg_count > pos_count:
            score = -(len(clean_text) % 7 + neg_count * 3)
        else:
            neutral_count += 1
            score = 0

        adjustment = temp_multiplier * (i + 1)
        adjusted_score = score + adjustment  # Irrelevant adjustment (not used later)
        sentiment_scores.append(score)

    return sentiment_scores


def transform_data(raw_data):
    processed = []
    offset = 5
    for idx, val in enumerate(raw_data):
        shifted = val << 1
        inverted = ~shifted & 0xFF
        processed.append(inverted + offset)
    return processed


def evaluate_performance(feedback_logs):
    base_scores = analyze_sentiment(feedback_logs)
    transformed = transform_data([abs(x) for x in base_scores if x != 0])

    cumulative = 0
    decay_factor = 0.9
    peak_detected = False
    peak_index = -1

    for j, ts in enumerate(transformed):
        if ts > 100 and not peak_detected:
            peak_detected = True
            peak_index = j

        # Real computation path
        cumulative += ts * (decay_factor ** j)

    # Dead code branch - misleading
    if peak_detected and peak_index > 5:
        cumulative *= 0.8

    # Additional irrelevant tracking
    temp_tracker = []
    for k in range(len(transformed)):
        temp_tracker.append(k * cumulative // (j + 1) if j > 0 else 0)

    final_score = int(cumulative) + 17  # Final deterministic result
    return final_score

# Main execution
feedback_chain = [
    "  Excellent service and great staff!  ",
    "Poor communication and bad follow-up.",
    "It was good, but could be better.",
    "Terrible experience overall.",
    "Great job, excellent work!",
    "Neutral comment without clear sentiment."
]

interim_data = [len(msg) for msg in feedback_chain]  # Unused auxiliary data
placeholder = ''.join([msg[0] for msg in feedback_chain if msg.strip()])  # Distractor

final_score = evaluate_performance(feedback_chain)
print(f"Result: {final_score}")