def evaluate_performance(raw_scores, tolerance_level):
    baseline_rating = 65
    adjusted_index = len(raw_scores) // 2
    smoothed_scores = [score * (1 - tolerance_level) for score in raw_scores]
    final_ratings = sorted(smoothed_scores)
    valid_input = len(raw_scores) > 0 and all(s >= 40 for s in raw_scores)
    extra_buffer = [x for x in raw_scores if x > 80]  # Irrelevant distractor list
    unused_metric = sum(smoothed_scores) / len(smoothed_scores) if smoothed_scores else 0  # Distractor computation
    threshold_score = final_ratings[adjusted_index] if valid_input else baseline_rating
    return threshold_score

result = evaluate_performance([78, 85, 90, 72, 88], 0.1)
print(f"Result: {result}")