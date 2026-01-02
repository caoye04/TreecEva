def analyze_sentiment(text):
    # Irrelevant sentiment analysis function (dead code path)
    positive_words = ['good', 'great', 'excellent', 'outstanding']
    count = sum(1 for word in positive_words if word in text.lower())
    return count > 0

# Baseline thresholds (distractor variables)
threshold_a = 85.0
threshold_b = 72.5
threshold_c = 60.0

# Fake feedback categories (misleading data)
categories = {'response_time': 4.2, 'accuracy': 4.8, 'tone': 3.9, 'clarity': 4.5}

# Simulated user feedback log with embedded metadata
feedback_log = [
    {'user': 'U1', 'rating': 4, 'comment': 'Good improvement over last version', 'tags': ['enhancement', 'minor']},
    {'user': 'U2', 'rating': 5, 'comment': 'Excellent work on edge cases', 'tags': ['critical', 'bugfix']},
    {'user': 'U3', 'rating': 3, 'comment': 'Needs better documentation', 'tags': ['docs', 'minor']},
    {'user': 'U4', 'rating': 5, 'comment': 'Great performance boost', 'tags': ['performance', 'major']}
]

# Historical benchmark (irrelevant legacy data)
historical_avg = [78.3, 81.1, 79.5, 82.0, 80.2]
legacy_weights = [0.1, 0.2, 0.3, 0.2, 0.2]  # unused

# Unused recursive helper (red herring)
def calculate_depth(data, depth=0):
    if not data:
        return depth
    return calculate_depth(data[1:], depth + 1)

# Character frequency map for tag analysis (partially relevant)
def extract_tag_complexity(log):
    tag_string = ''.join(tag for entry in log for tag in entry['tags'])
    freq_map = {char: tag_string.count(char) for char in set(tag_string)}
    return len(freq_map)  # Measures unique characters in tags

# Core logic disguised among distractors
def compute_rating_product(log):
    product = 1
    for entry in log:
        rating = entry['rating']
        product *= rating
    return product

# Bit manipulation decoy
def obfuscate_value(x):
    return ((x << 3) ^ 0xFE) & 0xFF  # No impact on final result

baseline = 60

# Real transformation chain
length_factor = len(feedback_log)
sentiment_score = 0
for entry in feedback_log:
    comment = entry['comment']
    if 'excellent' in comment.lower() or 'great' in comment.lower():
        sentiment_score += 2
    elif 'good' in comment.lower():
        sentiment_score += 1

# Extract complexity from tags
tag_entropy = extract_tag_complexity(feedback_log)

# Compute multiplicative core
rating_product = compute_rating_product(feedback_log)

# Fake normalization (distractor)
normalized_hist = [x / max(historical_avg) * 100 for x in historical_avg]

# Actual formula hidden in middle
raw_score = length_factor * sentiment_score * (tag_entropy % 7)

# Decoy bitwise operation
obfuscated = obfuscate_value(int(sum(categories.values())))

# Final evaluation using only select components
final_score = raw_score + (rating_product % 100)

# Additional red herring: unused dictionary aggregation
aggregated = {}
for entry in feedback_log:
    for tag in entry['tags']:
        if tag not in aggregated:
            aggregated[tag] = 0
        aggregated[tag] += entry['rating']

Result: final_score