import math

# Simulated user feedback analysis with distractors
def analyze_sentiment(texts):
    sentiment_scores = []
    for text in texts:
        score = 0
        words = text.split()
        for word in words:
            if word.lower() in ['good', 'great', 'excellent']:
                score += 0.5
            elif word.lower() in ['bad', 'terrible', 'awful']:
                score -= 0.3
        sentiment_scores.append(max(-1.0, min(1.0, score)))
    return sentiment_scores

# Irrelevant helper (dead code path)
def deprecated_normalize(vals):
    total = sum([abs(v) for v in vals])
    return [v / (total + 1e-8) for v in vals]

# Noise generator (distractor)
def generate_noise(n):
    noise = []
    for i in range(n):
        val = (i * 0.73) % 1.0
        noise.append(val)
    return noise

# Core logic: performance aggregation with weighted feedback
feedback_logs = [
    "user experience was excellent and smooth",
    "interface is bad and confusing",
    "great functionality but terrible navigation",
    "excellent overall impression",
    "bad performance and awful response time"
]

sentiments = analyze_sentiment(feedback_logs)

# Distractor variables
baseline_shift = sum([math.sin(i) for i in range(len(sentiments))])
phantom_weights = [math.log(2 + i) for i in range(len(sentiments))]
useless_stats = {
    'avg_noise': sum(generate_noise(5)) / 5,
    'max_sentiment': max(sentiments),
    'min_sentiment': min(sentiments)
}

# Actual weight vector (masked among distractors)
weights = [0.8, 0.6, 0.9, 0.7, 0.5]

# Red herring normalization function (unused)
def normalize_vector(vec):
    norm = math.sqrt(sum([x ** 2 for x in vec]))
    return [x / (norm + 1e-8) for x in vec] if norm > 0 else vec

# Real processing begins
weighted_sum = 0.0
for i in range(len(sentiments)):
    weighted_sum += sentiments[i] * weights[i]

# Secondary adjustment based on consistency metric
consistency_penalty = 0.0
for i in range(1, len(sentiments)):
    if abs(sentiments[i] - sentiments[i-1]) > 0.8:
        consistency_penalty += 0.1

adjusted_score = weighted_sum - consistency_penalty

# Data transformation via dictionary mapping (actual use)
score_categories = {
    'low': [s for s in sentiments if s < 0],
    'neutral': [s for s in sentiments if -0.1 <= s <= 0.1],
    'high': [s for s in sentiments if s > 0.5]
}

category_bonus = 0.0
if len(score_categories['high']) >= 2:
    category_bonus += 0.25
if len(score_categories['low']) == 0:
    category_bonus += 0.15

# List comprehension for signal filtering (meaningful usage)
filtered_signals = [s * w for s, w in zip(sentiments, weights) if abs(s) > 0.2]
bonus_amplifier = sum(filtered_signals) / (weighted_sum + 1e-8) if weighted_sum != 0 else 0

calibration_factor = math.cos(len(filtered_signals) * 0.1)

# Final aggregation function
def aggregate_performance(scores, w):
    raw = sum(s * w[i] for i, s in enumerate(scores))
    penalty = sum(0.05 for s in scores if s < -0.4)
    bonus = 0.2 if all(s > -0.5 for s in scores) else 0.0
    return raw - penalty + bonus

# Critical execution point
final_score = aggregate_performance(sentiments, weights)

# Additional red herring computation (unused result)
shadow_score = sum([math.exp(s) for s in sentiments]) / len(sentiments)

# Print required output
print(f"Result: {final_score}")