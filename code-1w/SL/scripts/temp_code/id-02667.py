def calculate_final_score(data, thresholds):
    # Irrelevant tracking variables (distractors)
    total_elements = 0
    temp_sum = 0
    debug_log = []

    # Semi-relevant preprocessing with string-based filtering
    processed_data = []
    for i, entry in enumerate(data):
        if isinstance(entry, str):
            cleaned = entry.strip().lower().replace(' ', '')
            if 'error' in cleaned:
                continue
            length_flag = len(cleaned) > 5
        else:
            cleaned = str(entry)
            length_flag = True

        try:
            numeric_val = float(cleaned)
            processed_data.append((i, numeric_val, length_flag))
            temp_sum += numeric_val
        except ValueError:
            debug_log.append(f"Invalid entry at {i}: {cleaned}")

    # Threshold filtering using logical combinations and comparisons
    filtered_values = []
    high_priority_count = 0
    for idx, val, flag in processed_data:
        above_min = val >= thresholds[0]
        below_max = val <= thresholds[1]
        if above_min and below_max:
            if flag or val > thresholds[1] - 10:  # Mixed condition
                high_priority_count += 1
            filtered_values.append(val)

    # Secondary filtering: only keep values appearing in even-indexed positions originally
    final_filtered = [v for (idx, v, f) in processed_data if v in filtered_values and idx % 2 == 0]

    # Real computation path
    base_score = sum(final_filtered)
    penalty = len(filtered_values) - len(final_filtered)
    adjustment_factor = 1.0
    if high_priority_count > 0:
        adjustment_factor = 1.2

    # Red herring: unused complex calculation
    outlier_check = [x for x in final_filtered if x < base_score / (len(final_filtered) + 1e-5)]
    stability_metric = len(outlier_check) * 0.5 if final_filtered else 0

    # Final score computation
    final_score = int((base_score - penalty) * adjustment_factor)

    # Dead code branch (never executed due to logic)
    if False:
        fallback = sum(temp_sum for _ in range(2))
        final_score = fallback

    return final_score

# Main execution
raw_data = ["  DataPoint ", "error log", 42, "ValueTwo", 38, "short", 45, 39]
thresh = (37, 46)
result = calculate_final_score(raw_data, thresh)
print(f"Target result: {result}")