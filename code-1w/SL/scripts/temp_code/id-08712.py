def analyze_performance(ratings, threshold=5):
    adjusted_ratings = [r + 1 for r in ratings if r < 8]
    filtered_ratings = [r for r in adjusted_ratings if r >= threshold]
    bonus_applied = False
    if sum(filtered_ratings) > 15:
        filtered_ratings.append(5)
        bonus_applied = True
    final_score = sum(filtered_ratings)
    return final_score

ratings_input = [4, 7, 3, 9, 6, 2]
result = analyze_performance(ratings_input)
print(f"Result: {result}")