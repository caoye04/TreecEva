def analyze_performance(ratings, threshold=6.5):
    adjusted_ratings = [round(r * 1.1, 1) for r in ratings]
    above_threshold = [r for r in adjusted_ratings if r >= threshold]
    trimmed_data = above_threshold[1:-1]
    filtered_ratings = [r for r in trimmed_data if r > 7.0]
    bonus_points = len(adjusted_ratings) - len(filtered_ratings)
    final_score = sum(filtered_ratings)
    return final_score

ratings_input = [5.8, 6.2, 6.9, 7.1, 7.4, 6.8, 7.6]
final_score = analyze_performance(ratings_input)
print(f"Target result: {final_score}")