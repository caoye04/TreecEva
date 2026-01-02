from collections import defaultdict

# Simulate student quiz scoring with bonus logic
def calculate_final_score(raw_scores, deductions):
    score_map = defaultdict(int)
    total_candidates = len(raw_scores)
    
    for i, score in enumerate(raw_scores):
        if score >= 6:
            score_map['passing'] += 1
        score_map['total_sum'] += score

    # Apply penalty adjustments only for high performers
    adjusted_sum = score_map['total_sum']
    for j, (score, penalty) in enumerate(zip(raw_scores, deductions)):
        if raw_scores[j] > 8:
            adjusted_sum -= penalty

    base_average = score_map['total_sum'] / total_candidates
    final_penalty = deductions[0] * 0.5
    result = base_average - final_penalty
    
    # Irrelevant distraction: counting digits in penalty values
    digit_count = 0
    temp = int(deductions[0])
    while temp > 0:
        digit_count += 1
        temp //= 10
    
    return int(result)

# Input data
test_scores = [7, 9, 5, 10, 8]
fine_points = [2, 1, 0, 3, 2]

result = calculate_final_score(test_scores, fine_points)
print(f"Result: {result}")