def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'great', 'outstanding']
    negative_words = ['bad', 'poor', 'terrible', 'awful']
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    return pos_count - neg_count

# Simulate preprocessing of user feedback logs
def preprocess_logs(raw_logs):
    cleaned = [log.strip().lower() for log in raw_logs]
    filtered = [log for log in cleaned if 'feedback' in log]
    return filtered

# Compute average sentiment from logs
def compute_avg_sentiment(logs):
    sentiments = []
    for log in logs:
        sentiment = analyze_sentiment(log)
        sentiments.append(sentiment)
    total = sum(sentiments)
    count = len(sentiments)
    return total / count if count > 0 else 0.0

# Evaluate team performance based on feedback and thresholds
def evaluate_performance(feedback_logs, threshold):
    # Preprocess logs (some may be irrelevant)
    processed_logs = preprocess_logs(feedback_logs)
    
    # Extract key metrics
    log_count = len(processed_logs)
    char_count = sum(len(log) for log in processed_logs)
    avg_length = char_count / log_count if log_count > 0 else 0
n    # Dummy distraction: calculate word frequency set (not used later)
    all_words = set()
    for log in processed_logs:
        all_words.update(log.split())
    rare_words = {word for word in all_words if len(word) > 7}
    rare_word_count = len(rare_words)

    # Core logic: compute average sentiment
    avg_sentiment = compute_avg_sentiment(processed_logs)
    
    # Secondary metric: count logs with strong sentiment
    strong_feedback_count = 0
    for log in processed_logs:
        sent = analyze_sentiment(log)
        if abs(sent) >= 2:
            strong_feedback_count += 1

    # Additional red herring: simulate unrelated computation
    entropy_proxy = 0
    for i in range(min(log_count, 5)):
        if i % 2 == 0:
            entropy_proxy += (i + 1) * 1.5

    # Final scoring logic
    base_score = avg_sentiment * 10
    bonus = 5 if strong_feedback_count > 2 else 0
    penalty = -3 if log_count < 3 else 0
    
    final_score = base_score + bonus + penalty
    
    # This print is required to expose the result
    print(f"Result: {final_score}")
    return final_score

# Input data
feedback_data = [
    "Feedback: excellent service today",
    "Poor experience with support",
    "Great! Outstanding response time",
    "feedback: bad connection issues",
    "Average interaction, nothing special"
]

threshold = 0.5

# Key execution point
final_score = evaluate_performance(feedback_data, threshold)