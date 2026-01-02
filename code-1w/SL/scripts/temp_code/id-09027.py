def evaluate_performance(raw_scores, passing_threshold=50):
    total = sum(raw_scores)
    count = len(raw_scores)
    average = total / count
    adjusted_scores = [score * 1.1 for score in raw_scores]
    normalized_avg = min(max(average, 0), 100) * 1.05
    passing_grade = normalized_avg >= passing_threshold
    extra_buffer = 5  # Irrelevant distractor variable
    temp_flag = False  # Unused flag, minor distraction
    threshold_score = max(0, min(normalized_avg, 100)) if passing_grade else 0
    return threshold_score

result = evaluate_performance([45, 55, 50, 48, 52])
print(f"Result: {result}")