def analyze_performance(metrics, limit):
    # Initialize tracking variables
    cumulative_weight = 0.0
    adjusted_count = 0
    outlier_detected = False
    temp_buffer = []

    # Irrelevant pre-scan: counts negative values (not used in final logic)
    negative_counter = 0
    for val in metrics:
        if val < 0:
            negative_counter += 1

    # Main processing with slicing and conditional logic
    segment = metrics[1:-1]  # Exclude first and last elements
    base_reference = metrics[0] * 0.5

    for i, x in enumerate(segment):
        if x > limit:
            contribution = (x ** 0.5) * (i + 1)
            cumulative_weight += contribution
            adjusted_count += 1
            if x > 2 * limit and not outlier_detected:
                outlier_detected = True
                temp_buffer.append(x * 0.1)
        else:
            # Distractor computation: modifies buffer but doesn't impact output
            temp_buffer = [y + x * 0.05 for y in temp_buffer]

    # Secondary loop: simulates validation pass (partially redundant)
    validation_factor = 1.0
    for j in range(len(temp_buffer)):
        if temp_buffer[j] > base_reference:
            validation_factor *= 0.95

    # Final score calculation
    if adjusted_count == 0:
        final_score = base_reference
    else:
        raw_score = cumulative_weight / adjusted_count
        final_score = raw_score * validation_factor

    # Dead code branch — never executed due to logic above
    if len(metrics) < 0:  # Always false
        final_score = -1

    return final_score

# Input data
aptitude_metrics = [16, 25, 36, 49, 64, 81, 100]
threshold = 30

# Key execution point
final_score = analyze_performance(aptitude_metrics, threshold)
print(f"Result: {final_score}")