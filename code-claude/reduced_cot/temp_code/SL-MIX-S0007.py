# Calculate product quality score based on ratings and weights
def analyze_products(ratings, importance):
    # Pair ratings with their importance weights
    items = list(zip(ratings, importance))
    
    # Filter out items with low importance (below 3)
    filtered_items = [(r, w) for r, w in items if w >= 3]
    
    # Calculate average rating for reference
    avg_rating = sum(r for r, _ in items) / len(items) if items else 0
    
    # Calculate weighted product score
    product_score = sum(map(lambda x: x[0] * x[1], filtered_items))
    
    # Calculate normalized score (not used in final result)
    norm_factor = sum(w for _, w in filtered_items)
    normalized = product_score / norm_factor if norm_factor else 0
    
    return product_score

# Product ratings (1-10) and importance weights (1-5)
product_ratings = [7, 8, 6, 9, 4]
importance_weights = [5, 2, 4, 3, 1]

result = analyze_products(product_ratings, importance_weights)
print(f"Result: {result}")