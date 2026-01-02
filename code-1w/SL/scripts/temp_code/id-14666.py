def calculate_final_score(performances, impact_factors):
    base_scores = []
    adjustment_log = []
    temp_buffer = []

    for idx, (perf, factor) in enumerate(zip(performances, impact_factors)):
        raw_score = perf * factor
        if idx % 2 == 0:
            raw_score += len(adjustment_log)  # Minor cumulative tweak
        adjusted_score = round(raw_score / 1.5)
        
        # Distractor: irrelevant transformation
        transformed = adjusted_score ** 0.5 if adjusted_score > 10 else adjusted_score + 2
        temp_buffer.append(transformed)

        base_scores.append(adjusted_score)
        adjustment_log.append(raw_score)

    # Secondary processing with distractor variables
    outlier_count = 0
    filtered_scores = []
    threshold = sum(base_scores) / len(base_scores) if base_scores else 0

    for score in base_scores:
        if abs(score - threshold) > 15:
            outlier_count += 1
        else:
            filtered_scores.append(score)

    # Dead code path - never alters final result
    if outlier_count > 10:
        fallback = 0
        for val in temp_buffer:
            fallback += int(val // 3)
        return fallback

    # Real computation path
    weighted_sum = 0
    for i, score in enumerate(filtered_scores):
        weight = 1 + (i * 0.1)
        weighted_sum += score * weight

    scaling_factor = len(filtered_scores) if filtered_scores else 1
    preliminary_score = weighted_sum / scaling_factor

    # Final adjustment using integer division and rounding
    final_score = int(preliminary_score // 1.2) + 5

    # Extra irrelevant state tracking
    history_tracker = []
    for j in range(3):
        history_tracker.append(f"Snapshot_{j}: {len(base_scores)}")

    return final_score

# Main execution
rankings = [85, 90, 78, 92, 88, 76, 95]
weights = [1.2, 1.4, 0.8, 1.6, 1.3, 0.9, 1.5]

auxiliary_data = [(x**2 % 7) for x in range(len(rankings))]
dummy_matrix = [[i*j for j in range(3)] for i in auxiliary_data]

intermediate_total = sum(auxiliary_data)
placeholder_result = intermediate_total * 0.5  # Unused beyond this point

final_score = calculate_final_score(rankings, weights)
print(f"Target result: {final_score}")