def analyze_sentiment(texts, patterns):
    sentiment_map = {'excellent': 3, 'good': 2, 'average': 1, 'poor': -1, 'awful': -3}
    score = 0
    for text in texts:
        words = text.lower().split()
        for word in words:
            if word in sentiment_map:
                score += sentiment_map[word]
    return score


def extract_keywords(content, min_len=4):
    # Irrelevant helper function - dead code path
    keywords = []
    for word in content.split():
        if len(word) >= min_len and word.isalpha():
            keywords.append(word)
    return keywords


def transform_ratings(ratings):
    # Distractor transformation - not used in final logic
    adjusted = []
    for r in ratings:
        if r < 3:
            adjusted.append(r ** 2)
        else:
            adjusted.append(int(r * 1.5))
    return adjusted


def compute_entropy(data):
    # Misleading statistical computation - red herring
    from math import log2
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

# Unused but plausible-looking data structures
baseline_metrics = {
    'precision': 0.87,
    'recall': 0.76,
    'f1': 0.81
}

auxiliary_weights = [0.1, 0.2, 0.15, 0.25, 0.3]

# Real input data
reviews = [
    "The product is excellent and works good",
    "Average performance, not good or bad",
    "Poor quality, very awful experience",
    "Good value for money, quite excellent",
    "Terrible - feels awful and not good at all"
]

weights = [0.5, 0.8, 0.6, 0.9, 0.7]

# Simulate user engagement metrics - irrelevant accumulation
engagement_logs = [
    "user_1 viewed page",
    "user_2 clicked button",
    "user_3 scrolled down",
    "user_4 shared content"
]

total_interactions = 0
for log in engagement_logs:
    parts = log.split()
    if 'clicked' in parts or 'shared' in parts:
        total_interactions += 1

# Begin relevant processing chain
sentiment_values = []
for i, review in enumerate(reviews):
    tokens = review.lower().replace(',', '').replace('.', '').split()
    base_score = 0
    emphasis_factor = 1.0
    
    # Check for intensifiers
    if 'very' in tokens or 'extremely' in tokens:
        emphasis_factor = 1.5
    
    for j, word in enumerate(tokens):
        if word in ['excellent', 'good', 'average', 'poor', 'awful']:
            base_score += {'excellent': 3, 'good': 2, 'average': 1, 'poor': -1, 'awful': -3}[word]
    
    weighted_score = base_score * weights[i] * emphasis_factor
    sentiment_values.append(weighted_score)

# Secondary transformation with distractors
scaled_values = [v * 1.1 for v in sentiment_values if v > 0]  # Only positive scaled
penalized_values = [v * 0.8 for v in sentiment_values if v < 0]  # Only negative penalized

# Hidden accumulation: sum all original weighted scores regardless of sign
aggregate = 0
for val in sentiment_values:
    aggregate += val  # This is critical but obscured by other operations

# Mock machine learning model (decoy)
def predict_satisfaction(features):
    return sum(f * 0.3 for f in features[:3])

predicted = predict_satisfaction(sentiment_values)

# Core business logic buried in noise
def process_feedback(feedback_list, weight_vector):
    total_impact = 0
    
    # Use enumerate and zip as required
    for idx, (review, weight) in enumerate(zip(feedback_list, weight_vector)):
        clean_text = ''.join(ch for ch in review.lower() if ch.isalnum() or ch == ' ')
        word_list = clean_text.split()
        
        # Count impactful terms
        term_count = {term: 0 for term in ['excellent', 'good', 'average', 'poor', 'awful']}\n        for word in word_list:
            if word in term_count:
                term_count[word] += 1
        
        # Compute raw impact
        raw_impact = 0
        mapping = {'excellent': 3, 'good': 2, 'average': 1, 'poor': -1, 'awful': -3}
        for term, count in term_count.items():
            raw_impact += mapping[term] * count
        
        # Apply position-based decay (subtle logic)
        positional_modifier = 1.0
        if idx < 2:
            positional_modifier = 1.1  # Early reviews slightly amplified
        elif idx > 3:
            positional_modifier = 0.9  # Later reviews slightly reduced
        
        # Final contribution
        contribution = raw_impact * weight * positional_modifier
        total_impact += contribution
    
    # Additional adjustment: bonus if more than two 'excellent'
    excellent_total = 0
    for rev in feedback_list:
        excellent_total += rev.lower().count('excellent')
    if excellent_total > 2:
        total_impact += 5.0
    
    return total_impact

# Execute main logic
final_score = process_feedback(reviews, weights)

# Print result as required
print(f"Result: {final_score}")