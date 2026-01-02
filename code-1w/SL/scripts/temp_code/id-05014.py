def evaluate_performance(feedback):
    sentiment_map = {'positive': 1, 'neutral': 0, 'negative': -1}
    weights = [0.1, 0.15, 0.25, 0.5]
    base_score = 50
    adjustment = 0
    temp_sum = 0
    ignored_counter = 0

    for i, entry in enumerate(feedback):
        parts = entry.lower().strip().split(':')
        if len(parts) < 2:
            ignored_counter += 1
            continue

        category = parts[0].strip()
        comment = ':'.join(parts[1:]).strip()

        # Irrelevant string processing (distractor)
        word_count = len(comment.split())
        char_count = len(comment.replace(' ', ''))
        temp_sum += word_count * (i + 1)

        sentiment_hint = None
        if 'good' in comment or 'excellent' in comment or 'happy' in comment:
            sentiment_hint = 'positive'
        elif 'bad' in comment or 'poor' in comment or 'disappointed' in comment:
            sentiment_hint = 'negative'
        else:
            sentiment_hint = 'neutral'

        # Actual logic contribution
        sentiment_value = sentiment_map[sentiment_hint]
        adjustment += sentiment_value * weights[i % len(weights)]

    # Dummy loop with no effect (dead code path - distractor)
    running_tally = 0
    for _ in range(5):
        running_tally += ignored_counter * 0.1
        running_tally = round(running_tally, 2)

    # Final score calculation
    final_score = base_score + (adjustment * 10)
    final_score = int(round(final_score))

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_entries = [
    "user: I am very happy with the service",
    "quality: excellent performance overall",
    "delivery: bad timing and poor communication",
    "support: I felt disappointed with the response"
]

# Execution point
final_score = evaluate_performance(feedback_entries)