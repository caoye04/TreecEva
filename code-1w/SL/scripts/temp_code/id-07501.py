def analyze_sentiment(texts):
    sentiment_scores = []
    for text in texts:
        words = text.lower().split()
        score = sum(1 for w in words if w in ['excellent', 'good', 'great']) - \
                sum(1 for w in words if w in ['poor', 'bad', 'terrible'])
        sentiment_scores.append(score)
    return sentiment_scores

# Simulate system feedback logs with verbosity levels and response quality
timestamps = [101, 102, 103, 104, 105]
verbosity_levels = [3, 5, 2, 6, 4]
response_quality = [8, 7, 5, 9, 6]
raw_feedback = [
    "The model response was excellent but slightly verbose",
    "Good explanation, though not perfect",
    "Poor reasoning chain, needs improvement",
    "Great logic flow and good structure",
    "Bad output, terrible formatting"
]

# Irrelevant aggregation (distractor)
total_interactions = sum(1 for t in timestamps if t > 100)
mean_verbosity = sum(verbosity_levels) / len(verbosity_levels)

# Relevant data processing
sentiments = analyze_sentiment(raw_feedback)
feedback_tuples = list(zip(timestamps, verbosity_levels, response_quality, sentiments))

# Filter high-quality responses
filtered_logs = [entry for entry in feedback_tuples if entry[2] >= 7]

# Extract sentiment values from filtered logs using enumerate
extracted_sentiments = []
for i, log in enumerate(filtered_logs):
    if i % 2 == 0:  # Only even-indexed entries considered
        extracted_sentiments.append(log[3])

# Misleading intermediate calculation (not used)
avg_response_time = sum(timestamps) / len(timestamps)

# Define benchmarking function with lambda
benchmark_threshold = lambda x: x >= 0

def evaluate_performance(feedback_logs, threshold_func):
    valid_count = 0
    total_sentiment = 0
    for log in feedback_logs:
        sent = log[3]
        if threshold_func(sent):
            total_sentiment += sent
            valid_count += 1
    # Final score based on average sentiment of acceptable entries
    return int(total_sentiment / valid_count) if valid_count > 0 else 0

# Execute main logic
final_score = evaluate_performance(filtered_logs, benchmark_threshold)
print(f"Result: {final_score}")