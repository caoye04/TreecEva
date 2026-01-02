def analyze_performance(scores, threshold=75):
    # Simulate multi-step analysis with distractions
    temp_processed = []
    outlier_count = 0
    cumulative_shift = 0.0

    for idx, score in enumerate(scores):
        if score < 50:
            outlier_count += 1
            shifted = score * 1.1
            cumulative_shift += shifted
        else:
            adjusted = score * 0.95
            if adjusted > threshold:
                temp_processed.append(adjusted - 10)
            else:
                temp_processed.append(adjusted)

    # Distractor: unused normalization path
    normalized_scores = [s / max(temp_processed) * 100 for s in temp_processed if s > 0]
    ignored_total = sum(normalized_scores[:3]) if len(normalized_scores) > 3 else 0

    # Real computation begins here
    sliced_window = temp_processed[1:-1]  # Use slice to exclude first and last
    filtered_active = [val for val in sliced_window if val >= threshold - 5]

    base_tally = 0
    for val in filtered_active:
        if val % 2 == 0:
            base_tally += int(val // 3)
        else:
            base_tally += int(val % 7)

    checksum = 0
    for i in range(len(filtered_active)):
        checksum += (i + 1) * filtered_active[i]  # Weighted sum, not used later

    # Secondary distractor variables
    dummy_frame = (base_tally * 2) % 1000
    shadow_copy = temp_processed.copy()
    shadow_copy.reverse()

    # Critical path
    final_tally = base_tally * 2
    adjustment_factor = len(filtered_active) * 3
    result_score = final_tally + adjustment_factor

    # Output required format
    print(f"Result: {result_score}")

    return result_score

# Input data
exam_scores = [88, 45, 92, 78, 63, 91, 47, 85]
analyze_performance(exam_scores)