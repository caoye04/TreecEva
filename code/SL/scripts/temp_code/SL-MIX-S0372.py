import re

# Sentiment weights for words
positive_weights = {'amazing': 5, 'excellent': 4, 'good': 3, 'nice': 2}
negative_weights = {'awful': -5, 'bad': -3, 'poor': -2, 'terrible': -4}

# Stop words to filter out
stop_words = frozenset(['the', 'and', 'is', 'in', 'on', 'at', 'to', 'of', 'for', 'with'])

# Sample user reviews
reviews = [
    "The product is amazing and excellent in quality.",
    "It is a good product but has poor customer service.",
    "Terrible experience, very bad and awful support."
]

# Initialize sentiment score
final_sentiment_score = 0

# Process each review
for review in reviews:
    # Tokenize and clean words
    tokens = [re.sub(r'[^a-zA-Z]', '', word).lower() for word in review.split()]
    
    # Filter out stop words using set difference
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    # Nested loop to calculate sentiment
    for word in filtered_tokens:
        if word in positive_weights:
            final_sentiment_score += positive_weights[word]
        elif word in negative_weights:
            final_sentiment_score += negative_weights[word]
        else:
            # Neutral words contribute 0, so no action needed
            continue
        
        # Early break if sentiment exceeds a threshold
        if final_sentiment_score > 10:
            break
    
    # Apply adjustment after each review
    if final_sentiment_score < 0:
        final_sentiment_score = int(final_sentiment_score * 0.9)

print(f"Result: {final_sentiment_score}")