def analyze_feedback(reviews):
    sentiment_count = {'positive': 0, 'neutral': 0, 'negative': 0}
    word_frequency = {}
    total_length = 0

    for review in reviews:
        words = review.lower().split()
        total_length += len(words)

        # Determine sentiment (simplified)
        if 'excellent' in words or 'great' in words or 'good' in words:
            sentiment_count['positive'] += 1
        elif 'poor' in words or 'bad' in words or 'terrible' in words:
            sentiment_count['negative'] += 1
        else:
            sentiment_count['neutral'] += 1

        # Track word frequency (distractor computation)
        for word in words:
            cleaned = ''.join(ch for ch in word if ch.isalnum())
            if cleaned:
                word_frequency[cleaned] = word_frequency.get(cleaned, 0) + 1

    avg_length = total_length / len(reviews) if reviews else 0
    return sentiment_count, avg_length, word_frequency


def compute_weights(n):
    # Irrelevant helper: computes Fibonacci-like sequence
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

reviews_list = [
    "The product is excellent and great quality",
    "Good value for money, very satisfied",
    "Poor design and terrible user experience",
    "It's okay, nothing special but works",
    "Absolutely bad packaging, not recommended",
    "Great features and excellent support"
]

# Extract metrics
sentiments, average_word_count, freq_map = analyze_feedback(reviews_list)

# Distractor variables
fibonacci_offset = compute_weights(len(reviews_list))
temp_scaling = sum(freq_map.get(w, 0) for w in ['the', 'and', 'is'])
adjusted_avg = average_word_count * (1 + fibonacci_offset * 0.01)

# Core logic for performance evaluation
consistency_bonus = 10 if abs(sentiments['positive'] - sentiments['negative']) <= 2 else 5
volume_penalty = len(reviews_list) > 5 else 0  # boolean used in arithmetic context

base_metric = sentiments['positive'] * 10 - sentiments['negative'] * 8 + consistency_bonus

# Conditional expression usage (required feature)
penalty_factor = 0.9 if volume_penalty else 1.0
scaled_metric = base_metric * penalty_factor

# Dictionary-based weighting (required feature)
weights = {'positive': 1.2, 'neutral': 0.5, 'negative': -1.5}
weighted_sum = sum(weights[k] * v for k, v in sentiments.items())

# Final integration step
intermediate_result = scaled_metric + weighted_sum * 2
aux_debug_value = temp_scaling + adjusted_avg  # dead-end variable

final_score = int(intermediate_result + 0.5)  # round to nearest integer

print(f"Result: {final_score}")