def analyze_component(values, threshold):
    count_above = 0
    sum_relevant = 0
    temp_result = 0

    for i, val in enumerate(values):
        if val > threshold:
            count_above += 1
            sum_relevant += val
        temp_result += (val * (i + 1))  # Irrelevant cumulative weighted sum

    average = sum_relevant / count_above if count_above > 0 else 0
    return average, temp_result


def validate_sequence(seq):
    valid = True
    dummy_sum = 0
    for idx, num in enumerate(seq):
        if idx > 0 and seq[idx-1] >= num:
            valid = False
        dummy_sum += num * (idx % 3)  # Distractor computation
    return valid


def calculate_performance(data):
    scores = []n    adjustments = []
    total_weight = 0

    for key, values in data.items():
        avg, _ = analyze_component(values, threshold=50)
        weight = len([v for v in values if v > 0])  # Count of positive values
        total_weight += weight
        
        sorted_vals = sorted(values, reverse=True)
        top_three_avg = sum(sorted_vals[:3]) / 3 if len(sorted_vals) >= 3 else 0
        
        # Complex adjustment logic with red herring
        adjustment_factor = 1.0
        if len(values) % 2 == 0:
            adjustment_factor *= 0.95
        if validate_sequence(values):
            adjustment_factor *= 1.1
        
        adjusted_score = (avg + top_three_avg) * adjustment_factor
        scores.append(adjusted_score)
        adjustments.append(adjustment_factor)

    # Final aggregation
    base_performance = sum(scores) / len(scores) if scores else 0
    
    # Dummy normalization using zip and enumerate (semi-relevant but not critical)
    normalized = []
    for i, (s, a) in enumerate(zip(scores, adjustments)):
        normalized.append(s / (a + 0.1 * (i % 2)))  # Minor distortion, not used later

    # Actual final score calculation
    raw_total = sum(scores)
    penalty = len([x for x in adjustments if x < 1.0]) * 5  # Penalty for low adjustments
    final_score = raw_total - penalty

    return int(final_score)

# Main execution
benchmark_data = {
    'module_a': [65, 70, 58, 92, 45],
    'module_b': [72, 68, 81, 77, 60],
    'module_c': [50, 55, 60, 65, 70],
    'module_d': [88, 90, 85]
}

intermediate_check = [sum(vals) for vals in benchmark_data.values()]  # Unused diagnostic
baseline_estimate = sum(intermediate_check) // len(intermediate_check)  # Misleading metric

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")