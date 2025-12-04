# E-commerce product rating calculator

def analyze_reviews(reviews):
    sentiment_scores = []
    for review in reviews:
        # Extract words and calculate basic sentiment
        words = review.lower().split()
        positive_words = ['great', 'excellent', 'good', 'love', 'perfect']
        negative_words = ['bad', 'poor', 'terrible', 'hate', 'disappointing']
        
        # Count positive and negative words (not used in final calculation)
        pos_count = sum(1 for word in words if word in positive_words)
        neg_count = sum(1 for word in words if word in negative_words)
        
        # Assign sentiment score based on review length and content
        score = len(review) % 3 + 2
        sentiment_scores.append(score)
    
    return sentiment_scores

# Product reviews dataset
product_reviews = [
    "This product is excellent and works great!",
    "Disappointed with the quality, wouldn't recommend.",
    "Perfect for my needs, very happy with purchase.",
    "Good value but shipping was slow."
]

# Calculate review scores
review_scores = analyze_reviews(product_reviews)

# Some additional metrics (distractors)
review_count = len(product_reviews)
average_length = sum(len(review) for review in product_reviews) / review_count
max_score = max(review_scores)
min_score = min(review_scores)

# Filter scores based on arbitrary threshold (intervention)
threshold = 3
filtered_scores = [score for score in review_scores if score > threshold]

# Define importance weights for each filtered review
importance_weights = [0.5, 0.8]

# Calculate weighted product rating
product_rating = sum([(weight * score) for score, weight in zip(filtered_scores, importance_weights)])

# Some post-calculation processing (distractors)
scaled_rating = product_rating / sum(importance_weights)
rating_category = "High" if scaled_rating > 4 else "Medium" if scaled_rating > 2 else "Low"

print(f"Result: {product_rating}")