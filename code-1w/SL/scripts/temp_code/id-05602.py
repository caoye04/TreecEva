def analyze_feedback(reviews):
    word_count = 0
    positive_keywords = {'excellent', 'great', 'good', 'amazing', 'outstanding'}
    negative_keywords = {'poor', 'bad', 'terrible', 'awful', 'worst'}
    neutral_count = 0
    total_chars = 0

    for review in reviews:
        words = review.lower().split()
        word_count += len(words)
        total_chars += sum(len(word) for word in words)
        
        # Irrelevant aggregation
        if 'service' in review.lower():
            neutral_count += 1

    avg_length = total_chars / word_count if word_count else 0
    return word_count, avg_length, neutral_count


def sanitize_input(data):
    cleaned = []
    for item in data:
        item = item.strip().rstrip('!?.')
        if len(item) > 0:
            cleaned.append(item)
    return cleaned

# Simulated user feedback strings
customer_reviews = [
    "Great product!",
    "Poor quality overall.",
    "Amazing value for money",
    "Good experience with excellent support",
    "Terrible experience, worst purchase"
]

# Preprocessing step with distraction
raw_data = [rev + '!' for rev in customer_reviews]
decoy_sum = sum(len(r) % 7 for r in raw_data)
processed_reviews = sanitize_input(raw_data)

# Extract keyword-based signals
feedback_set = set()
ratings = []
length_distribution = []

for text in processed_reviews:
    words = set(text.lower().split())
    if words & {'excellent', 'great', 'amazing', 'outstanding'}:
        feedback_set.add('positive')
        ratings.append(5)
    elif words & {'poor', 'bad', 'terrible', 'awful', 'worst'}:
        feedback_set.add('negative')
        ratings.append(2)
    else:
        feedback_set.add('neutral')
        ratings.append(3)
    
    # Distractor: collect but don't use
    length_distribution.append(len(text))

# Auxiliary calculation with partial relevance
total_reviews = len(ratings)
avg_rating = sum(ratings) / total_reviews if total_reviews else 0
diversity_index = len(feedback_set)

# Misleading complexity
weight_map = {5: 1.2, 3: 1.0, 2: 0.5}
weighted_total = sum(weight_map.get(r, 1.0) * r for r in ratings)
normalized_weight = weighted_total / total_reviews if total_reviews else 0

# Core logic hidden among distractions
def evaluate_performance(sentiment_pool, scores):
    base = len(sentiment_pool) * 10
    bonus = 0
    if 'positive' in sentiment_pool:
        bonus += 15
    if 'negative' not in sentiment_pool:
        bonus += 10
    
    # Real computation
    rating_factor = sum(scores) // len(scores) if scores else 0
    adjustment = 0
    for s in scores:
        if s == 5:
            adjustment += 3
    return base + bonus + rating_factor + adjustment

# Key execution point
counts, avg_len, _ = analyze_feedback(processed_reviews)
final_score = evaluate_performance(feedback_set, ratings)
print(f"Result: {final_score}")