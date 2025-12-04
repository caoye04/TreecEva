def analyze_product_reviews(reviews, ratings):
    # Calculate sentiment scores for each review
    sentiment_scores = []
    for i, review in enumerate(reviews):
        # Simple sentiment score based on word count and rating
        word_count = len(review.split())
        base_score = word_count * 0.1
        weight = ratings[i] / 5.0
        sentiment_score = base_score * weight
        sentiment_scores.append(round(sentiment_score, 1))
    
    # Calculate average rating for reference (not used in final calculation)
    avg_rating = sum(ratings) / len(ratings) if ratings else 0
    
    # Process reviews with ratings and sentiment scores
    combined_data = []
    for i, (review, rating, score) in enumerate(zip(reviews, ratings, sentiment_scores)):
        relevance = min(10, len(review.split()) / 5)
        adjusted_score = score
        if 'excellent' in review.lower():
            adjusted_score += 2
        elif 'good' in review.lower():
            adjusted_score += 1
        elif 'poor' in review.lower():
            adjusted_score -= 1
        combined_data.append((i, adjusted_score, relevance))
    
    # Track highest relevance (not used in final calculation)
    max_relevance = max([data[2] for data in combined_data]) if combined_data else 0
    
    # Filter scores based on relevance threshold
    threshold = 5
    filtered_scores = []
    for idx, score, relevance in combined_data:
        if relevance > threshold:
            filtered_scores.append(score)
    
    # Calculate product score based on filtered sentiment scores
    product_score = sum(filtered_scores)
    
    # Calculate alternative score (not used)
    alternative_score = sum([r for r in ratings if r > 3])
    
    return product_score

# Sample data
reviews = [
    "This product is excellent and exceeded my expectations",
    "Good quality but a bit expensive",
    "Poor performance, would not recommend",
    "Average product, nothing special",
    "Very good design and functionality"
]

ratings = [5, 4, 2, 3, 4]

result = analyze_product_reviews(reviews, ratings)
print(f"Result: {result}")