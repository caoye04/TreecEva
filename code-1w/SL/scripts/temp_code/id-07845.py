def evaluate_performance():
    raw_scores = [88, 92, 75, 85, 94, 90, 70]
    thresholds = {'min_pass': 75, 'excellence': 90}
    adjusted_scores = [score + 5 for score in raw_scores if score >= thresholds['min_pass']]
    
    # Track indices of improved students
    improvement_log = []
    for i, score in enumerate(adjusted_scores):
        if score >= thresholds['excellence']:
            improvement_log.append(i)

    ranks = [len(adjusted_scores) - sorted(adjusted_scores).index(score) for score in adjusted_scores]
    filtered_ranks = [rank for rank in ranks if rank <= 5]
    
    total_score = sum(filtered_ranks)
    return total_score

result = evaluate_performance()
print(f"Result: {result}")