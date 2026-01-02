def calculate_performance(scores, threshold):
    normalized = [round(s ** 0.5, 2) for s in scores]
    passed = [s for s in normalized if s >= threshold]
    filtered_scores = list(map(lambda x: x * 1.1, passed))
    extra_offset = 5  # Irrelevant variable (minimal distraction)
    total_score = sum(filtered_scores)
    return total_score

scores_input = [81, 64, 49, 36, 25]
result = calculate_performance(scores_input, 7.0)
print(f"Result: {result}")