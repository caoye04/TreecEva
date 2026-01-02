def analyze_sentiment(text_blocks):
    sentiment_scores = []
    for block in text_blocks:
        score = 0
        if 'excellent' in block or 'outstanding' in block:
            score += 3
        elif 'good' in block or 'great' in block:
            score += 2
        elif 'poor' in block or 'terrible' in block:
            score -= 2
        sentiment_scores.append(score)
    return sentiment_scores

# Irrelevant helper function (distractor)
def compute_text_entropy(text_list):
    import math
    total_entropy = 0.0
    for text in text_list:
        freq = {}
        for c in text:
            freq[c] = freq.get(c, 0) + 1
        for count in freq.values():
            prob = count / len(text)
            if prob > 0:
                total_entropy -= prob * math.log2(prob)
    return round(total_entropy, 4)

# Another red herring: unused data structure
class PerformanceNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Misleading preprocessing chain
def preprocess_feedback(raw_feedback):
    cleaned = [fb.strip().lower() for fb in raw_feedback]
    tokenized = [fb.split() for fb in cleaned]
    flattened_tokens = [word for tokens in tokenized for word in tokens]
    unique_tokens = list(set(flattened_tokens))
    # Below line does nothing for final result
    token_lengths = [len(t) for t in unique_tokens]
    return cleaned  # only returns cleaned, rest was distraction

# Decoy function that looks important but isn't used in critical path
def calculate_decay_factor(n):
    if n <= 0:
        return 1.0
    factor = 1.0
    for i in range(1, n+1):
        factor *= (1 - 1/(i+1))
    return round(factor, 5)

# Real logic buried among noise
def evaluate_consistency(ratings):
    trend = 0
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i-1]:
            trend += 1
        elif ratings[i] < ratings[i-1]:
            trend -= 1
    return abs(trend) < 2  # consistent if minor fluctuation

# Core transformation with distractors around
feedback_sequence = [
    "The service was excellent and outstanding!",
    "Good effort, though could improve.",
    "Poor experience overall, very disappointing",
    "Great staff, really good atmosphere",
    "Outstanding quality and excellent delivery"
]

historical_data = [85, 87, 86, 90, 88, 84, 89]  # Unused legacy metric
legacy_weights = [0.1, 0.15, 0.2, 0.25, 0.3]   # Red herring

weights = [0.2, 0.3, 0.1, 0.25, 0.15]  # Actual weights

# Distractor: complex-looking but unused list comprehension
extended_analysis = [
    (idx, txt, len(txt.split()), txt.count('e'))
    for idx, txt in enumerate(preprocess_feedback(feedback_sequence))
    if 'good' in txt or 'excellent' in txt
]

# Another dead-end computation
redundant_mapping = {
    i: (len(feedback_sequence[i]), len(feedback_sequence[i].split()))
    for i in range(len(feedback_sequence))
}

sentiments = analyze_sentiment(feedback_sequence)

# Hidden conditional dependency
temp_offset = 0
if len(sentiments) % 2 == 0:
    temp_offset += 5
if sum(sentiments) > 5:
    temp_offset += 3

# Simulated consistency check (bypassed but looks involved)
mock_ratings = [4, 5, 3, 5, 4]
consistency_flag = evaluate_consistency(mock_ratings)

# Critical nested logic with slicing and zip
adjusted_sentiments = []
for i, s in enumerate(sentiments):
    adjustment = 0
    if i < len(weights):
        if weights[i] > 0.2:
            adjustment = 1
        elif weights[i] == 0.2:
            adjustment = 0
        else:
            adjustment = -1
    adjusted_sentiments.append(s + adjustment)

# Real aggregation using zip and enumerate (key step)
raw_product = 0
for index, (value, weight) in enumerate(zip(adjusted_sentiments, weights)):
    if index % 2 == 0:
        raw_product += value * weight * 100
    else:
        raw_product += value * weight * 50

# Secondary adjustment based on pattern
pattern_boost = 0
for a, b in zip(adjusted_sentiments, adjusted_sentiments[1:]):
    if a < b:
        pattern_boost += 1
    elif a > b:
        pattern_boost -= 2

# Final calculation chain
baseline = raw_product / len(weights)
volatility_penalty = abs(sum(adjusted_sentiments[:3]) - sum(adjusted_sentiments[2:])) * 2

# The actual answer derivation
final_score = int(baseline - volatility_penalty + temp_offset)

# Print required output
print(f"Target result: {final_score}")