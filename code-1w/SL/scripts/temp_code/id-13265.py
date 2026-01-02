def analyze_metrics(data, threshold=5.0):
    # Irrelevant transformation
    temp_offsets = [x * 0.1 for x in data]
    adjusted_values = [x + 2 if x < threshold else x - 1 for x in data]
    
    # Distractor: complex but unused calculation
    outlier_count = sum(1 for x in data if abs(x - sum(data)/len(data)) > 2)
    penalty_factor = outlier_count * 0.5 if outlier_count > 3 else 0

    # Relevant logic: count how many are above dynamic benchmark
    benchmark = sum(adjusted_values) / len(adjusted_values)
    performance = sum(1 for x in adjusted_values if x > benchmark)

    return performance


def calculate_adjusted_performance():
    raw_input = [3, 7, 2, 8, 5, 6, 4, 9]
    
    # Unused preprocessing step (distractor)
    processed = list(map(lambda x: (x ** 2 + 1) // x, raw_input))
    
    # Secondary distractor variables
    normalized = [round(x / sum(raw_input), 3) for x in raw_input]
    entropy_proxy = sum(-p * __import__('math').log(p) for p in normalized if p > 0)
    
    # Core logic hidden among noise
    base_metric = analyze_metrics(raw_input, threshold=5.5)
    adjustment = 0
    
    # Conditional logic affecting final score
    if base_metric >= 4:
        adjustment += 10
    else:
        adjustment -= 5
    
    # Another irrelevant loop
    for i in range(len(raw_input)):
        if i % 3 == 0:
            adjustment += raw_input[i] // 4  # Minor side effect

    final_score = base_metric * 15 + adjustment
    
    # This is the key assignment
    final_score = calculate_dynamic_bonus(final_score, base_metric)
    
    return final_score


def calculate_dynamic_bonus(score, metric):
    # Bonus logic with conditional expression
    multiplier = 1.2 if metric > 4 else 0.8
    extra = sum([i for i in range(metric) if i % 2 == 0])
    
    # Dead code path (not taken due to fixed input)
    if False and score < 0:
        score -= 100
    
    return int(score * multiplier) + extra

# Entry point
final_score = 0
final_score = calculate_adjusted_performance()
print(f"Target result: {final_score}")