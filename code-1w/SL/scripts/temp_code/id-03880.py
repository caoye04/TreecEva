def analyze_sentiment(text):
    positive_words = {'great', 'good', 'excellent', 'amazing', 'wonderful', 'positive'}
    negative_words = {'bad', 'poor', 'terrible', 'awful', 'horrible', 'negative'}
    words = text.lower().split()
    pos_count = len([w for w in words if w in positive_words])
    neg_count = len([w for w in words if w in negative_words])
    return pos_count - neg_count


def transform_data(records):
    processed = []
    total_chars = 0
    for record in records:
        cleaned = record.strip().replace("#", "").title()
        total_chars += len(cleaned)
        processed.append(cleaned)
    avg_length = total_chars / len(processed) if processed else 0
    return processed, avg_length

feedback_logs = [
    "great job on the excellent work",
    "poor effort and bad attitude",
    "amazing results with wonderful outcomes",
    "terrible performance overall"
]

# Irrelevant transformation (distractor)
transformed_data, average_len = transform_data(feedback_logs)
size_factor = len(transformed_data) * 2.5

# Core logic obscured by auxiliary variables
sentiment_scores = [analyze_sentiment(log) for log in feedback_logs]
valid_scores = [score for score in sentiment_scores if score != 0]

# Misleading aggregation
magnitude_sum = sum(abs(s) for s in sentiment_scores)
directional_sum = sum(s for s in sentiment_scores)

# Threshold filtering based on net sentiment
threshold = 1 if directional_sum > 0 else -1

# Key computation with nested logic
convergence = 0
for i in range(len(valid_scores)):
    if i % 2 == 0:
        convergence += valid_scores[i] ** 2
    else:
        convergence -= abs(valid_scores[i])

# Final scoring with redundant operations
baseline = len(valid_scores) * 3
adjustment = magnitude_sum // 2 if threshold > 0 else -(-magnitude_sum // 2)
final_score = baseline + convergence + adjustment

# Dead code path (distractor)
if size_factor < 0:
    final_score *= -1

Result: final_score