def analyze_metrics(values, threshold=10):
    count_valid = 0
    temp_sum = 0
    penalty = 0
    for i, val in enumerate(values):
        if val > threshold:
            count_valid += 1
            temp_sum += val
        if i % 3 == 0:
            penalty += 2  # Minor penalty every third index
    adjusted_sum = temp_sum - penalty
    return adjusted_sum, count_valid


def normalize_sequence(data):
    max_val = max(data)
    min_val = min(data)
    range_val = max_val - min_val
    normalized = [(x - min_val) / range_val for x in data]
    return normalized


def calculate_performance(raw_input):
    # Preprocessing step with distractor variables
    offset = 5
    scale_factor = 1.0
    filtered_data = [x for x in raw_input if x >= 5]
    
    # Analyze metrics - this returns meaningful intermediate values
    base_score, valid_count = analyze_metrics(filtered_data)
    
    # Distractor computation: normalization not used in final path
    normalized = normalize_sequence(filtered_data)
    avg_normalized = sum(normalized) / len(normalized)
    deviation_penalty = 0
    for n in normalized:
        if n < 0.2:
            deviation_penalty += 0.1
    
    # Real scoring logic begins
    multiplier = 1
    if valid_count > 3:
        multiplier *= 2
    elif valid_count == 3:
        multiplier *= 1.5
    else:
        multiplier *= 0.8
    
    # Use enumerate and zip together in a meaningful but partially distracting way
    indexed = list(enumerate(filtered_data))
    shifted = [x - offset for x in filtered_data[1:]] + [0]
    pairs = list(zip(indexed, shifted))
    
    secondary_bonus = 0
    for (idx, value), sh_val in pairs:
        if idx % 2 == 1 and sh_val > 5:
            secondary_bonus += 3
    
    # Final score calculation - only base_score, multiplier, and secondary_bonus matter
    preliminary = base_score * multiplier
    final_score = preliminary + secondary_bonus
    
    # Irrelevant tracking variables
    record_log = []
    for v in filtered_data:
        record_log.append(f"Item: {v}")
    
    return int(final_score)

# Main execution
benchmark_data = [8, 12, 6, 15, 3, 11, 9]
dummy_var = sum(x**2 for x in benchmark_data)  # Unused computation
scaling_map = {i: v*0.1 for i, v in enumerate(benchmark_data)}  # Dead data structure

final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")