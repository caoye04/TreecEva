def analyze_performance(scores, weights):
    normalized = [score / 100.0 for score in scores]
    weighted_contributions = [n * w for n, w in zip(normalized, weights)]
    adjustment_factor = 0.95
    applied_adjustment = [wc * adjustment_factor for wc in weighted_contributions]
    final_score = sum(weighted_contributions)
    return final_score

exam_scores = [88, 94, 76, 91]
importance_weights = [0.2, 0.3, 0.15, 0.35]
result = analyze_performance(exam_scores, importance_weights)
print(f"Result: {result}")