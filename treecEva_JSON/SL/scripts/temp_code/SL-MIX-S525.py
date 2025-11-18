import re
from itertools import combinations

def calculate_sentiment_stability(review_text):
    # Tokenize and filter
    tokens = re.findall(r'\b\w+\b', review_text.lower())
    stop_words = {'the', 'and', 'or', 'but', 'is', 'are', 'was', 'were'}
    filtered_tokens = [t for t in tokens if t not in stop_words]
    
    # Character set operations
    char_sets = [frozenset(token) for token in filtered_tokens]
    if len(char_sets) < 2:
        return 0.0
    
    # Compute pairwise intersections
    intersection_counts = [
        len(set_a & set_b) for set_a, set_b in combinations(char_sets, 2)
    ]
    
    # Sentiment stability index calculation
    total_intersections = sum(intersection_counts)
    max_possible = len(filtered_tokens) * (len(filtered_tokens) - 1) // 2 * min(len(s) for s in char_sets)
    
    # Avoid division by zero
    if max_possible == 0:
        return 0.0
    
    # Final index with floating point adjustment
    sentiment_stability_index = round((total_intersections / max_possible) * 100, 2)
    return sentiment_stability_index

# Input processing
user_review = "The product quality is excellent and performance is outstanding"
sentiment_stability_index = calculate_sentiment_stability(user_review)
print(f"Result: {sentiment_stability_index}")