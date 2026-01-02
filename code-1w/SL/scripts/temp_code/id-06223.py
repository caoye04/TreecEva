def analyze_sentiment(texts):
    sentiment_scores = {}
    for i, text in enumerate(texts):
        words = text.lower().split()
        positive = len([w for w in words if w in {'great', 'good', 'excellent', 'amazing'}])
        negative = len([w for w in words if w in {'bad', 'terrible', 'awful', 'poor'}])
        sentiment_scores[i] = positive - negative
    return sentiment_scores


def normalize(values):
    total = sum(abs(v) for v in values)
    if total == 0:
        return [0 for _ in values]
    return [round(v / total, 4) for v in values]


def filter_outliers(scores, threshold=2):
    mean = sum(scores) / len(scores)
    deviances = [abs(s - mean) for s in scores]
    return [s for s, d in zip(scores, deviances) if d <= threshold]

# Simulated user feedback ratings from multiple sources
text_feedback = [
    "This is great and amazing work",
    "Poor effort, really bad outcome",
    "Excellent quality, absolutely excellent",
    "It's not terrible, but could be better",
    "Amazing, great, excellent - truly wonderful"
]

numeric_ratings = [4.2, 3.8, 4.9, 2.5, 4.7, 3.1, 4.0]
engagement_levels = [85, 72, 93, 60, 95, 68, 80]

# Step 1: Analyze textual sentiment
sentiments = analyze_sentiment(text_feedback)

# Misleading intermediate: engagement impact (not used later)
engagement_impact = [level * 0.01 for level in engagement_levels]
scaled_ratings = [r * e for r, e in zip(numeric_ratings, engagement_impact)]

# Normalize ratings (distractor computation)
normalized_ratings = normalize(numeric_ratings)

# Filter outlier sentiments based on index pattern
sentiment_values = list(sentiments.values())
filtered_sentiments = filter_outliers(sentiment_values)

# Weight assignment using enumerate and zip (required features)
weights = {}
for idx, (rating, sent) in enumerate(zip(normalized_ratings[:len(filtered_sentiments)], filtered_sentiments)):
    weight_key = f"source_{idx}"
    weights[weight_key] = round(rating * abs(sent) * 10, 2)

# Simulated feedback map with redundant structure
feedback_map = {}
for idx, text in enumerate(text_feedback):
    feedback_map[f"source_{idx}"] = {
        'raw_text': text,
        'sentiment': sentiments[idx],
        'length': len(text),
        'word_count': len(text.split()),
        'processed_flag': True
    }

# Aggregate performance function combining multiple concepts
def aggregate_performance(feedback_dict, weight_dict):
    base_accumulator = 0
    adjustment_factor = 0
    
    # Use of dictionary operations and conditional logic
    for key, data in feedback_dict.items():
        sent = data['sentiment']
        wc = data['word_count']
        
        # Key contribution logic
        if sent > 0 and wc >= 5:
            base_accumulator += sent * 2
        elif sent < 0:
            base_accumulator -= abs(sent)
        
        # Adjustment via external weights if present
        if key in weight_dict:
            adjustment_factor += weight_dict[key] * 0.05
    
    # Final computation with distractor variables included
    temp_result = base_accumulator + adjustment_factor
    scaling_offset = sum(1 for x in numeric_ratings if x >= 4.0)  # irrelevant count
    noise_floor = len(text_feedback) % 3  # unused artifact
    
    final_value = temp_result * (1 + adjustment_factor / 100)
    return int(round(final_value))

# Critical execution point
final_score = aggregate_performance(feedback_map, weights)
print(f"Target result: {final_score}")