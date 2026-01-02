def evaluate_performance(ratings, threshold=3):
    adjusted_ratings = [r + (1 if r < 4 else 0) for r in ratings]
    high_performers = [r for r in adjusted_ratings if r >= threshold]
    filtered_ratings = [r * 2 for r in high_performers if r % 2 == 1]
    total_score = sum(filtered_ratings)
    return total_score

ratings_data = [2, 3, 4, 5, 1, 3]
special_bonus = 10  # Irrelevant distractor variable
total_score = evaluate_performance(ratings_data)
print(f"Result: {total_score}")