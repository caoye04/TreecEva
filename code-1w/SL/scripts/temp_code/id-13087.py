def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'amazing', 'great', 'outstanding']
    negative_words = ['bad', 'poor', 'terrible', 'awful', 'worst']
    words = text.lower().split()
    score = sum(1 for w in words if w in positive_words) - sum(1 for w in words if w in negative_words)
    return 'positive' if score > 0 else 'negative' if score < 0 else 'neutral'

feedback_pool = [
    "This was excellent and amazing work",
    "Terrible effort and poor execution",
    "Great job overall, truly outstanding",
    "Not bad, but could be better",
    "Absolutely worst experience ever"
]

sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0}
for feedback in feedback_pool:
    label = analyze_sentiment(feedback)
    sentiment_counts[label] += 1

# Irrelevant aggregation
word_count_tally = sum(len(f.split()) for f in feedback_pool)
dummy_metric = (sentiment_counts['positive'] * 2 + sentiment_counts['negative']) % 4

# Chain construction with distraction
feedback_chain = []
current_index = 0
while current_index < len(feedback_pool) and len(feedback_chain) < 3:
    feedback_chain.append(feedback_pool[current_index])
    current_index += 2  # Skip every other

# Dummy transformation using lambda
transform = lambda x: x.upper() if 'good' in x.lower() else x.replace(' ', '_')
_ = [transform(f) for f in feedback_pool]  # Dead computation

# Core evaluation logic
def evaluate_performance(chain):
    base = 0
    for entry in chain:
        if 'excellent' in entry or 'outstanding' in entry:
            base += 10
        elif 'great' in entry:
            base += 7
        elif 'good' in entry:
            base += 5
        if 'poor' in entry or 'terrible' in entry:
            base -= 8
    adjustment = len(chain) * 2
    return base + adjustment if base > 0 else base - adjustment

final_score = evaluate_performance(feedback_chain)
print(f"Target result: {final_score}")