def analyze_performance(records):
    total_entries = len(records)
    valid_count = 0
    temp_sum = 0
    warning_flags = []

    # Irrelevant preprocessing: counting string lengths
    cumulative_length = 0
    for entry in records:
        if isinstance(entry, str):
            cumulative_length += len(entry.strip())

    # Real logic begins: parsing performance tuples
    scores = []
    for idx, record in enumerate(records):
        if isinstance(record, tuple) and len(record) == 3:
            name, result_str, timestamp = record
            if 'error' not in result_str.lower():
                try:
                    numeric_value = float(result_str)
                    scores.append(numeric_value)
                    valid_count += 1
                    temp_sum += numeric_value
                except ValueError:
                    warning_flags.append(idx)

    # Distractor: unused normalization attempt
    normalized_scores = [s / max(scores) for s in scores if max(scores) > 0] if scores else []

    avg_score = temp_sum / valid_count if valid_count > 0 else 0

    # Simulate conditional adjustment using set operations
    categories = {'A', 'B', 'C'}
    observed = set()
    for record in records:
        if isinstance(record, tuple) and record[0].startswith('Test'):
            observed.add(record[0][4])  # extract category letter

    bonus_applied = False
    if observed >= {'A', 'B'}:  # sufficient coverage
        bonus_applied = True
        avg_score *= 1.1

    # Secondary distractor: zip-based alignment check (not affecting final result)
    indices = list(range(len(scores)))
    paired_data = list(zip(indices, scores))
    outliers = [i for i, s in paired_data if s > avg_score * 1.5]

    # Final computation with string method red herring
    status_log = "complete_success verification_passed"
    tokens = status_log.upper().split()
    token_match = any("VER" in t for t in tokens)

    adjustment_factor = 0.95 if not token_match else 1.0

    final_score = int(avg_score * adjustment_factor)

    # Dead code path - never executed due to fixed condition
    if len(observed) > 100:
        final_score = -1  # unreachable

    return final_score


data_log = [
    "raw entry 1",
    ("TestA", "85.6", "2023-01-01"),
    ("TestB", "92.3", "2023-01-02"),
    ("TestC", "error_invalid", "2023-01-03"),
    ("TestA", "78.4", "2023-01-04"),
    ("TestB", "88.1", "2023-01-05"),
    "footer_checksum_complete"
]

final_score = analyze_performance(data_log)
print(f"Target result: {final_score}")