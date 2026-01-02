def analyze_sentiment(value):
    if value > 0.5:
        return 2
    elif value > 0.2:
        return 1
    else:
        return 0

# Simulate user feedback sequence over time
temporal_weights = [0.1, 0.3, 0.4, 0.6, 0.7, 0.8, 0.9]
raw_feedback = [0.25, 0.34, 0.67, 0.45, 0.88, 0.12, 0.59]

# Irrelevant transformation - distractor
distorted_signal = [abs(x - 0.5) * 2 for x in raw_feedback]

# Extract sentiment categories using helper function
sentiment_labels = [analyze_sentiment(score) for score in raw_feedback]

# Weighted accumulation with decay factor
weight_decay = 0.95
adjusted_weights = [w * (weight_decay ** i) for i, w in enumerate(temporal_weights)]

# Normalization step (partially relevant)
sum_weights = sum(adjusted_weights)
normalized_weights = [w / sum_weights for w in adjusted_weights] if sum_weights > 0 else adjusted_weights

# Compute weighted sentiment index
weighted_sentiment = sum(sentiment_labels[i] * normalized_weights[i] for i in range(len(sentiment_labels)))

# Secondary metric - engagement level (distractor)
engagement_level = sum(1 for x in raw_feedback if x > 0.4)
average_feedback = sum(raw_feedback) / len(raw_feedback)

# Feedback smoothing via moving average (semi-relevant preprocessing)
smoothed_feedback = []
for i in range(len(raw_feedback)):
    window = raw_feedback[max(0, i-2):i+1]
    smoothed_feedback.append(sum(window) / len(window))

# Aggregate performance function
def aggregate_performance(feedback_sequence):
    cumulative = 0
    multiplier = 1
    for idx, val in enumerate(feedback_sequence):
        if val >= 0.5:
            cumulative += val * 10
            if idx % 2 == 0:
                multiplier *= 1.1
        else:
            cumulative -= 2
    return int(cumulative * multiplier)

# Unused diagnostic check - dead code path
def diagnostic_check(seq):
    return all(x >= 0 for x in seq)

# Key computation
baseline_shift = sum(temporal_weights) - len(raw_feedback)
feedback_sequence = [x for x in raw_feedback if x > 0.15]  # Filter noise
final_score = aggregate_performance(feedback_sequence)

# Print result as required
print(f"Result: {final_score}")