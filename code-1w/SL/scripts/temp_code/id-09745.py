def evaluate_performance(ratings, threshold=5):
    adjusted_ratings = [r ** 0.5 for r in ratings if r >= threshold]
    normalized_ratings = [r / max(adjusted_ratings) for r in adjusted_ratings]
    base_score = len(normalized_ratings)
    adjustment_factor = 1.25 if base_score > 3 else 0.9
    final_score = sum(normalized_ratings) * adjustment_factor
    return final_score

ratings_input = [6, 8, 5, 9, 4, 7]
result = evaluate_performance(ratings_input)
print(f"Target result: {result}")