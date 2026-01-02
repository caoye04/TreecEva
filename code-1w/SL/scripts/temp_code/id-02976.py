def evaluate_performance(records, cutoff):
    valid_entries = []
    temp_sum = 0
    outlier_count = 0

    for item in records:
        raw_value = float(item.strip())
        if raw_value < 0:
            continue
        if raw_value > 1000:
            outlier_count += 1
            continue
        temp_sum += raw_value ** 0.5
        valid_entries.append(raw_value)

    # Irrelevant sorting (distraction)
    sorted_values = sorted(valid_entries, reverse=True)
    adjustment_factor = 1.0
    if len(sorted_values) > 5:
        adjustment_factor = 0.95

    # Secondary processing with string-based filtering (semi-relevant)
    str_values = [str(v) for v in valid_entries]
    filtered_by_digit = [v for v in str_values if '7' not in v]
    numeric_filtered = [float(v) for v in filtered_by_digit]

    base_score = sum(numeric_filtered)
    penalty = 0
    if len(numeric_filtered) != len(valid_entries):
        penalty = (len(valid_entries) - len(numeric_filtered)) * 2.5

    # Core logic: apply threshold filter on original scale
    passed_threshold = [v for v in valid_entries if v >= cutoff]
    performance_bonus = len(passed_threshold) * 3

    final_score = base_score - penalty + performance_bonus
    return final_score

# Simulated dataset with mixed content
data = [' 49.0 ', '82.5', '1050', '-34', '77.2', '64.0', '120.1', '90.3', '27.8']
threshold = 75.0
tmp_result = sum([int(float(d.strip())) for d in data if d.strip().isdigit()])  # Distractor computation

intermediate = [d.upper() for d in ['a', 'b']]  # Dead code path, no impact

final_score = evaluate_performance(data, threshold)
print(f"Target result: {final_score}")