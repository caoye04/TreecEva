def evaluate_performance(logs):
    total_entries = len(logs)
    valid_records = []
    temp_sum = 0
    outlier_count = 0

    for log in logs:
        # Parsing phase with string operations
        cleaned = log.strip().lower()
        if 'error' in cleaned:
            outlier_count += 1
            continue
        if 'data:' not in cleaned:
            continue

        # Extract numeric value
        try:
            value_str = cleaned.split('data:')[-1].strip()
            if value_str.isdigit():
                num_value = int(value_str)
                temp_sum += num_value
                valid_records.append(num_value)
        except:
            pass

    # Irrelevant statistical distraction
    mean_val = temp_sum / len(valid_records) if valid_records else 0
    squared_devs = [(x - mean_val) ** 2 for x in valid_records]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    # Secondary filtering: only keep values above median
    sorted_vals = sorted(valid_records)
    mid = len(sorted_vals) // 2
    median_threshold = sorted_vals[mid] if sorted_vals else 0

    filtered_high = [v for v in valid_records if v > median_threshold]

    # Bonus logic based on string pattern density
    pattern_bonus = 0
    for log in logs:
        alpha_chars = ''.join(filter(str.isalpha, log))
        if alpha_chars.islower() and 'debug' not in alpha_chars:
            pattern_bonus += 1

    # Core scoring logic
    base_score = sum(filtered_high)
    adjustment = len(valid_records) - outlier_count
    final_score = base_score + adjustment

    # Dead code path — misleading but harmless
    if variance_estimate < 0:
        final_score *= 2  # unreachable

    return final_score

# Input data with mixed content
data = [
    "  Data:105 ",
    "error: system failure",
    "data:203",
    "debug: reset sequence",
    "data:98",
    "Data:205",
    "data:77",
    "warning: minor anomaly",
    "data:203"
]

result = evaluate_performance(data)
print(f"Result: {result}")