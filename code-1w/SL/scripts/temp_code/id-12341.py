def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'amazing', 'outstanding']
    negative_words = ['bad', 'poor', 'terrible', 'awful']
    words = text.lower().split()
    score = 0
    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1
    return score

# Irrelevant helper function (decoy)
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

# Unused but plausible transformation
transform_map = {i: chr((i * 3 + 7) % 26 + 97) for i in range(26)}

def preprocess_inputs(raw_list):
    cleaned = [item.strip().lower() for item in raw_list if isinstance(item, str)]
    filtered = [c for c in cleaned if len(c) > 1]
    return filtered

# Simulated user feedback logs (distraction)
raw_feedback = [
    'Good effort',
    'Terrible response',
    'Amazing solution',
    'Awful performance',
    'Excellent job',
    'Poor outcome',
    'Outstanding result',
    'Bad implementation'
]

# Secondary analysis path (dead code path)
word_frequency = {}
for entry in raw_feedback:
    for word in entry.lower().split():
        word_frequency[word] = word_frequency.get(word, 0) + 1

# Actual logic begins here — nested scoring system
base_scores = [analyze_sentiment(f) for f in raw_feedback]

# Accumulate trend with conditional adjustment
running_trend = []
total_shift = 0
prev = 0
for s in base_scores:
    diff = s - prev
    if abs(diff) >= 2:
        total_shift += diff * 0.5
    running_trend.append(total_shift)
    prev = s

# Decoy data structure
stats_summary = {
    'count': len(base_scores),
    'average': sum(base_scores) / len(base_scores),
    'variance': sum((x - sum(base_scores)/len(base_scores))**2 for x in base_scores) / len(base_scores),
    'peaks': [i for i, x in enumerate(base_scores) if (i == 0 or base_scores[i-1] < x) and (i == len(base_scores)-1 or base_scores[i+1] < x)]
}

# Core evaluation chain (key logic)
def build_feedback_chain(scores):
    chain = []
    multiplier = 1
    for idx, val in enumerate(scores):
        if idx % 3 == 0:
            multiplier = 2 if val > 0 else 1
        adjusted = val * multiplier
        chain.append(adjusted)
    return [int(x) for x in chain]

feedback_chain = build_feedback_chain(base_scores)

# Auxiliary computation (distractor)
cumulative_products = []
prod = 1
for x in feedback_chain:
    if x != 0:
        prod *= abs(x)
    cumulative_products.append(prod % 100)

# Real answer derivation — multi-step aggregation
consecutive_positive = 0
max_streak = 0
for x in feedback_chain:
    if x > 0:
        consecutive_positive += 1
        max_streak = max(max_streak, consecutive_positive)
    else:
        consecutive_positive = 0

# Final weighting using list comprehension and dictionary lookup
weights = {'streak': max_streak, 'base_sum': sum(feedback_chain), 'penalty': len([x for x in feedback_chain if x < 0])}

# Critical statement
final_score = evaluate_performance(feedback_chain)

# Primary target function
def evaluate_performance(chain):
    # Sum of squares of positive elements minus triple the number of negatives
    positive_squares = sum([x**2 for x in chain if x > 0])
    negative_count = len([x for x in chain if x < 0])
    base_value = positive_squares - 3 * negative_count
    
    # Conditional bonus
    if len(chain) > 5:
        streak = 0
        best = 0
        for x in chain:
            if x >= 2:
                streak += 1
                best = max(best, streak)
            else:
                streak = 0
        if best >= 3:
            base_value += 10
    
    # Apply scaling based on input pattern
    pattern_factor = 1
    if chain[0] < 0 and chain[-1] > 0:
        pattern_factor = 1.5
    elif chain[0] > 0:
        pattern_factor = 0.8
    
    return int(base_value * pattern_factor)

# Print result
print(f"Target result: {final_score}")