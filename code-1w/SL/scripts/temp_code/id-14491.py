def analyze_sentiment(texts):
    sentiment_scores = []
    for text in texts:
        score = 0
        words = text.lower().split()
        positive = ['good', 'excellent', 'great', 'outstanding']
        negative = ['bad', 'terrible', 'poor', 'awful']
        
        # Real logic
        for word in words:
            if word in positive:
                score += 2
            elif word in negative:
                score -= 3
        sentiment_scores.append(score)
    
    return sentiment_scores


def compute_weights(n):
    # Distractor: complex-looking but unused later
    weights = [1] * n
    for i in range(1, n):
        weights[i] = weights[i-1] * 0.9
    scaled = [w / sum(weights) for w in weights]
    return scaled

feedback_samples = [
    "excellent service and great experience",
    "poor communication and bad follow-up",
    "good effort but terrible execution",
    "outstanding results overall"
]

# Real data processing
raw_scores = analyze_sentiment(feedback_samples)

# Mapping indices to scores with enumerate (required feature)
index_score_map = dict(enumerate(raw_scores))

# Some irrelevant transformation
offset_adjusted = [s + 5 for s in raw_scores if s < 0]
buffer_sum = sum(offset_adjusted) if offset_adjusted else 0  # unused almost

# Build feedback map using dictionary operations (required)
feedback_map = {}
for idx, score in index_score_map.items():
    category = 'positive' if score > 0 else 'negative'
    if category not in feedback_map:
        feedback_map[category] = []
    feedback_map[category].append(score)

# Introduce zip usage (required): pair with dummy priority levels
priorities = [1, 2, 3, 4]
decay_factors = compute_weights(4)
paired_data = list(zip(raw_scores, priorities, decay_factors))  # partially used

# Misleading lambda that looks important but isn't central
apply_decay = lambda x, d: x * d
adjusted_scores = [apply_decay(score, df) for score, _, df in paired_data]

# Actual key computation
steady_count = len([s for s in raw_scores if s == -1 or s == 1])
correction_factor = 1.5 if steady_count >= 2 else 0.8

# Core aggregation logic
positive_total = sum(feedback_map.get('positive', []))
negative_total = sum(feedback_map.get('negative', []))
base_aggregate = positive_total + abs(negative_total)

# Final scoring with distractors present but not dominant
scaling_constant = 10
phantom_offset = buffer_sum * 0.1  # negligible effect
final_score = (base_aggregate * correction_factor) + scaling_constant - phantom_offset

Result: {final_score}