def analyze_sentiment(text):
    positive_words = ['good', 'excellent', 'amazing', 'great', 'outstanding']
    negative_words = ['bad', 'terrible', 'awful', 'poor', 'worst']
    words = text.lower().split()
    score = sum(1 for word in words if word in positive_words)
    score -= sum(1 for word in words if word in negative_words)
    return max(-2, min(2, score))

# Simulate user review preprocessing
tokenize = lambda review: [word for word in review.lower().split() if len(word) > 2]

# Red herring function - not used in final computation
def calculate_length_penalty(review):
    tokens = tokenize(review)
    if len(tokens) < 5:
        return -1
    elif len(tokens) > 20:
        return 0.5
    else:
        return 0

# Core processing with distraction
reviews = [
    "This product is excellent and amazing, truly great!",
    "Terrible quality, absolutely awful experience.",
    "Great design but poor performance overall",
    "Outstanding features and excellent support"
]

weights = [1.2, 0.8, 1.0, 1.5]

# Distractor variables
dummy_scores = [len(r.split()) * 0.1 for r in reviews]
char_count_map = {i: len(reviews[i]) for i in range(len(reviews))}

# Misleading normalization (not applied to final result)
baseline_adjustment = sum(len(r) for r in reviews) / 100

# Actual processing chain
sentiment_vector = [analyze_sentiment(review) for review in reviews]

# Apply weighted scoring with slicing and conditional logic
trimmed_weights = weights[1:] + [1.0]  # shift for no real reason
adjusted_scores = []
for i in range(len(sentiment_vector)):
    raw = sentiment_vector[i]
    # Conditional expression with red herring calculation
    factor = trimmed_weights[i] if raw >= 0 else trimmed_weights[i] * 0.5
    adjusted = raw * factor
    adjusted_scores.append(round(adjusted, 3))

# Secondary distraction: character-based adjustment (unused)
length_factor = sum(char_count_map[k] % 7 for k in char_count_map) / 10

# Final computation
aggregated = sum(adjusted_scores)
penalty = 0
for score in adjusted_scores:
    if score < 0:
        penalty += 0.5

final_score = round(aggregated - penalty + 0.25, 2)  # +0.25 magic constant

# Irrelevant loop with early break
running_total = 0
for x in dummy_scores:
    running_total += x
    if running_total > 1.0:
        break

print(f"Result: {final_score}")