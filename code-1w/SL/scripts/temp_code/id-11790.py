def process_results(entries, limits):
    # Initialize tracking variables
    count_valid = 0
    temp_sum = 0
    outlier_flag = False
    debug_log = []

    # Precompute threshold bounds
    lower_bound = limits['min']
    upper_bound = limits['max']
    mid_threshold = (lower_bound + upper_bound) / 2

    # Irrelevant statistical placeholder (distractor)
    mean_approximation = sum(range(lower_bound, upper_bound)) / len(range(lower_bound, upper_bound))

    scaling_factor = 1.5 if len(entries) > 5 else 0.8

    for entry in entries:
        # Extract numeric value from string-encoded data (e.g., 'score: 78')
        if ':' in entry:
            raw_value_str = entry.split(':')[1].strip()
            if raw_value_str.isdigit():
                raw_value = int(raw_value_str)
            else:
                continue  # Skip invalid
        else:
            continue

        # Check if within acceptable range
        if lower_bound <= raw_value <= upper_bound:
            count_valid += 1
            temp_sum += raw_value

            # Additional check for mid-threshold crossing (semi-relevant)
            if raw_value > mid_threshold:
                adjustment = (raw_value - mid_threshold) * 0.1
                temp_sum += adjustment  # Minor boost for above-average scores

        else:
            # Outlier logic that never triggers final output
            if raw_value < lower_bound:
                debug_log.append(f'Low outlier: {raw_value}')
            else:
                debug_log.append(f'High outlier: {raw_value}')
            outlier_flag = True

    # Distractor computation: unused entropy-like metric
    if count_valid > 0:
        probability_distribution = [1/count_valid] * count_valid
        theoretical_entropy = -sum(p * __import__('math').log(p) for p in probability_distribution)

    # Secondary loop with partial relevance: checks formatting quality
    format_issues = 0
    for entry in entries:
        if not entry.strip().startswith('s') or not entry.endswith(str(entry[-1])):
            format_issues += 1

    # Final score depends only on scaled average of valid entries
    if count_valid == 0:
        base_score = 0
    else:
        base_score = temp_sum / count_valid

    # Apply scaling based on data size (only factor that matters)
    final_score = int(base_score * scaling_factor)

    # Red herring: unused transformation
    inverted_scores = [upper_bound - x + lower_bound for x in range(count_valid)]

    return final_score

# Input data
input_entries = [
    "score: 65", "score: 70", "score: 75",
    "score: 80", "score: 85", "score: 90",
    "score: 45", "score: 95"  # 45 is below min, 95 above max
]

data = input_entries
timeout_config = {"timeout": 30}
thresholds = {'min': 50, 'max': 90}

# Execute and print result
result_var = process_results(data, thresholds)
print(f"Result: {result_var}")