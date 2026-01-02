def analyze_sentiment(texts):
    sentiment_scores = []
    for text in texts:
        score = 0
        words = text.lower().split()
        positive = ['good', 'excellent', 'great', 'outstanding']
        negative = ['bad', 'poor', 'terrible', 'awful']
        for word in words:
            if word in positive:
                score += 2
            elif word in negative:
                score -= 3
        sentiment_scores.append(score)
    return sentiment_scores

# Irrelevant helper function (distractor)
def calculate_entropy(data):
    from math import log
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 4)

# Simulate system logs with mixed feedback
feedback_entries = [
    'user reported excellent response and great speed',
    'performance was poor and the experience was terrible',
    'outstanding accuracy but bad latency',
    'good overall impression'
]

# Extract feedback ratings using sentiment analysis
raw_sentiments = analyze_sentiment(feedback_entries)

# Track historical stats (mostly unused)
historical_avg = sum(raw_sentiments) / len(raw_sentiments) if raw_sentiments else 0
max_sentiment = max(raw_sentiments)
min_sentiment = min(raw_sentiments)

# Weight vector for multi-criteria evaluation (used later)
weights = [0.4, 0.3, 0.2, 0.1]

# Simulate feature importance drift (distractor computation)
drift_vector = [w * 1.05 for w in weights]
baseline_drift = sum(abs(drift_vector[i] - weights[i]) for i in range(len(weights)))

# Log entry indices and metadata (irrelevant tracking)
log_metadata = {i: {'length': len(entry), 'chars': len(entry.replace(' ', ''))} 
                for i, entry in enumerate(feedback_entries)}

# Count specific keywords across logs (partial distractor, minor relevance)
positive_count = 0
negative_count = 0
for entry in feedback_entries:
    words = entry.lower().split()
    for word in words:
        if word == 'excellent' or word == 'outstanding':
            positive_count += 1
        if word == 'terrible' or word == 'poor':
            negative_count += 1

# Auxiliary scoring based on word frequency (dead path)
frequency_bonus = 0
if positive_count > negative_count:
    frequency_bonus = 10
else:
    frequency_bonus = -5  # Unused in final logic

# Core evaluation function
def evaluate_performance(sentiments, w):
    adjusted = 0
    for idx, (sentiment, weight) in enumerate(zip(sentiments, w)):
        adjusted += sentiment * weight * (idx + 1)  # Emphasis on later feedback
    
    # Apply non-linear correction based on sentiment distribution
    variance = sum((s - historical_avg) ** 2 for s in sentiments) / len(sentiments) if sentiments else 0
    stability_penalty = 0
    if variance > 2.0:
        stability_penalty = 1.5
    
    # Final adjustment
    result = adjusted - stability_penalty
    
    # Additional irrelevant transformation
    temp_result = result ** 2 + 0.25
    normalized = temp_result / (abs(result) + 1)
    
    # Only 'result' feeds forward meaningfully
    return result

# Execute key computation
temp_data = list(enumerate(feedback_entries))
zipped_data = list(zip(raw_sentiments, weights))

# Critical execution point
final_score = evaluate_performance(raw_sentiments, weights)

print(f"Result: {final_score}")