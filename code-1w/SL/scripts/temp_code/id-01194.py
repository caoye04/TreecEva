def analyze_metrics(data):
    count_valid = 0
    sum_temporary = 0
    temp_factor = 1.5

    for val in data:
        if val < 0:
            continue
        if val > 100:
            sum_temporary += val * 0.1
        else:
            count_valid += 1
            sum_temporary += val

    average = sum_temporary / count_valid if count_valid > 0 else 0
    adjustment = temp_factor if average > 50 else 0.8
    return average * adjustment


def evaluate_performance(x, y, limit):
    base = x * 0.7 + y * 0.3
    penalty = 0

    if base > limit:
        excess = base - limit
        penalty = excess * 0.2 if excess > 10 else excess * 0.1
    
    # Distractor: irrelevant calculation
    dummy_calc = (x + y) ** 0.5
    noise = dummy_calc * 0.01
    
    adjusted_base = base - penalty
    
    # Conditional expression used
    final_score = adjusted_base if adjusted_base >= 0 else 0
    
    # Dead code path (never executed due to logic)
    if False:
        fallback = 999
        final_score = fallback

    return final_score

# Main execution
raw_data = [85, 90, -5, 70, 105, 60, 80]
metric_a = analyze_metrics(raw_data)
metric_b = len([x for x in raw_data if x > 0]) * 2
threshold = 75

# Key computation point
final_score = evaluate_performance(metric_a, metric_b, threshold)
print(f"Target result: {final_score}")