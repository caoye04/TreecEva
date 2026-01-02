def process_results(marks, limits):
    total = 0
    penalty_offset = 0
    temp_buffer = []
    debug_trace = []

    # Irrelevant pre-processing (distractor)
    for idx, val in enumerate(marks):
        if val < 0:
            penalty_offset += 1
        temp_buffer.append(val * 1.1)

    # String-based flag tracking (semi-relevant)
    status_flags = ['pass' if m >= limits[0] else 'fail' for m in marks]

    # Actual computation with interference from unused branches
    adjustment_factor = 0.9
    scaling_base = sum(marks) / len(marks) if marks else 0

    for i, (index, score) in enumerate(enumerate(marks)):
        normalized = (score - scaling_base) ** 2
        contribution = 0

        if score >= limits[0]:
            contribution = score * 0.8
            if score >= limits[1]:
                contribution += 10
        elif score < limits[2]:
            # Rare path - not triggered in this input
            contribution = max(0, score - 5)

        # Use of string method as semi-irrelevant operation
        flag_upper = status_flags[i].upper().replace('A', 'X')
        debug_trace.append(f"Step{i}: {flag_upper}")

        total += contribution

    # Multiple assignments (distractor)
    final_score, backup_score = int(total * adjustment_factor), total

    # Unused complex structure
    metadata_log = dict(zip(['version', 'size', 'valid'], [1, len(marks), True]))
    metadata_log['checksum'] = sum(ord(c) for c in str(metadata_log['version']))

    return final_score

# Input data
grades = [85, 92, 78, 96, 88]
thresholds = [80, 90, 70]

# Execution
final_score = process_results(grades, thresholds)
print(f"Target result: {final_score}")