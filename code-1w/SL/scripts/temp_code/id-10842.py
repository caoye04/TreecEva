from itertools import combinations

def analyze_performance(data):
    base_score = 0
    temp_offset = 0
    for i, value in enumerate(data):
        if i % 2 == 0:
            base_score += value * 2
        else:
            temp_offset += value // 2
    
    # Distractor: irrelevant transformation
    transformed = [x ** 0.5 for x in data if x > 5]
    sum_transformed = sum(transformed)

    return base_score - temp_offset

def calculate_ranking(points, penalties):
    raw_total = sum(points)
    penalty_deduction = 0
    
    for idx, (p, q) in enumerate(zip(points, penalties)):
        if p > 10 and idx < 5:
            penalty_deduction += q * 2
        elif p <= 5:
            penalty_deduction += q

    # Semi-relevant logic: uses set to deduplicate redundant penalties
    unique_penalties = len(set(penalties))
    adjustment = unique_penalties if unique_penalties % 3 == 0 else 0

    # Complex but partially distracting computation
    combo_count = 0
    for combo in combinations(penalties, 3):
        if sum(combo) > 15:
            combo_count += 1
    
    # Final score influenced only by key elements
    final_score = raw_total - penalty_deduction + adjustment
    
    # Dead code path (never executed under normal input)
    if len(points) > 100:
        fallback = sum(penalties) // len(points)
        final_score -= fallback
    
    return final_score

# Main execution
metrics = [8, 12, 6, 15, 3, 9]
diagnostic_data = [1, 4, 2, 5, 3, 6]

score_a = analyze_performance(metrics)
score_b = analyze_performance(diagnostic_data)

points = [10, 14, 7, 16, 5]
penalties = [3, 5, 2, 4, 1]

final_score = calculate_ranking(points, penalties)

Result: {final_score}