def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'great', 'outstanding', 'superb']
    negative_words = ['bad', 'poor', 'terrible', 'awful', 'horrible']
    words = text.lower().split()
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    return score

# Irrelevant helper function (distractor)
def compute_entropy(data):
    from math import log2
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 4)

# Another distractor: unused complex structure
class PerformanceTracker:
    def __init__(self, name):
        self.name = name
        self.history = []
    
    def log(self, value):
        self.history.append(value)

    def get_peak(self):
        return max(self.history) if self.history else 0

# Misleading variable computations
baseline_adjustment = 3.14159
adjustment_factor = sum([i**2 for i in range(5)]) // 4  # evaluates to 7
normalization_constant = (128 >> 3) & 15  # 16 & 15 => 0

# Core logic disguised among distractions
feedback_chain = [
    "The service was excellent and great",
    "Poor execution and terrible results",
    "It was good but not outstanding",
    "Superb quality overall"
]

sentiment_scores = list(map(analyze_sentiment, feedback_chain))

# Distracting intermediate transformations
weight_vector = [1.1, 0.9, 1.0, 1.2]
weighted_scores = [score * weight for score, weight in zip(sentiment_scores, weight_vector)]

# Unused logical branch (dead code path)
if len(weighted_scores) > 10:
    adjusted_weights = [w * 1.5 for w in weighted_scores]
else:
    buffer_var = [abs(w) for w in weighted_scores]  # computation not used later

# Lambda for transformation (required feature)
transform = lambda x: x + 2 if x > 0 else x + 1
enhanced_scores = [transform(int(s)) for s in weighted_scores]  # cast to int for predictability

# More distraction: character counting red herring
total_chars = sum(len(feedback.replace(' ', '')) for feedback in feedback_chain)
char_penalty = total_chars % 7

# State tracking with irrelevant nesting
status_log = []
for idx, score in enumerate(enhanced_scores):
    if score >= 0:
        for _ in range(1):  # artificial nesting level
            status = 'positive' if score > 3 else 'neutral'
            status_log.append(status)
    else:
        status_log.append('negative')

# Final evaluation with logical operations (AND, OR)
def evaluate_performance(scores):
    base = sum(scores)
    bonus = 5 if all(s >= -1 for s in scores) else 0
    penalty = 10 if any(s <= -5 for s in scores) else 0
    # Additional logic step: use of bitwise AND as distraction
    modifier = (base & 15) if base > 0 else 0
    return base + bonus - penalty + modifier

final_score = evaluate_performance(enhanced_scores)
print(f"Target result: {final_score}")