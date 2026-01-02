from itertools import combinations

def evaluate_performance(metric_a, metric_b):
    return (metric_a ** 2 + metric_b) // 3

def calculate_final_score(ranks, wts):
    base_scores = [evaluate_performance(r, w) for r, w in zip(ranks, wts)]
    
    # Irrelevant distraction: unused variable (minimal interference)
    temp_debug_log = [x * 0.1 for x in base_scores]
    
    filtered_scores = [s for s in base_scores if s > 5]
    score_pairs = list(combinations(filtered_scores, 2))
    
    aggregate = 0
    for pair in score_pairs:
        aggregate += pair[0] + pair[1]
    
    adjustment = len(filtered_scores) * 1.5
    final_score = aggregate - adjustment
    
    return int(final_score)

# Input data
rankings = [7, 5, 9, 3, 8]
weights = [2, 4, 6, 1, 5]

result = calculate_final_score(rankings, weights)
print(f"Result: {result}")