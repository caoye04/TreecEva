def analyze_sentiment(rating):
    return 'positive' if rating >= 3 else 'negative'

sentiment_map = {'positive': 1, 'negative': -1}

def process_feedback(feedback):
    count = len(feedback)
    total = sum(feedback)
    avg = total / count if count > 0 else 0
    category = 'high' if avg >= 3 else 'low'
    return {'avg': avg, 'count': count, 'category': category}

# Simulated feedback scores from users
raw_data = [4, 5, 2, 3, 5, 4, 1, 3, 4]

# Misleading transformation - not used in final logic
transformed = [x ** 0.5 for x in raw_data if x % 2 == 1]
cumulative_shift = sum(transformed) / len(transformed) if transformed else 0

# Actual processing path
filtered_data = [x for x in raw_data if x != 1]  # Remove lowest score
feedback_summary = process_feedback(filtered_data)

# Secondary analysis with distractor variables
valid_entries = [x for x in raw_data if x > 0]
duplicate_check = {x: valid_entries.count(x) for x in set(valid_entries)}
peak_detected = max(valid_entries) > 4

# Lambda for dynamic weighting (used)
weight_fn = lambda x: 1.2 if x > 3 else 0.8
weighted_scores = [score * weight_fn(score) for score in filtered_data]

# Build feedback list with sentiment tagging
feedback_list = []
for val in weighted_scores:
    raw_val = int(round(val / (1.2 if val > 3.6 else 0.8)))
    sentiment = analyze_sentiment(raw_val)
    entry = {
        'value': val,
        'sentiment': sentiment,
        'weight': weight_fn(raw_val)
    }
    feedback_list.append(entry)

# Evaluation function using dictionary and conditional expression
def evaluate_performance(reports):
    if not reports:
        return 0
    base = sum(r['value'] for r in reports)
    adjustment = sum(sentiment_map[r['sentiment']] for r in reports) * 0.5
    bonus = 10 if len(reports) > 5 else 0
    penalty = -5 if any(r['value'] < 2 for r in reports) else 0
    return base + adjustment + bonus + penalty

# Critical execution point
final_score = evaluate_performance(feedback_list)

print(f"Result: {final_score}")