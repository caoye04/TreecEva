def evaluate_performance(log, thresholds):
    # Track correct classifications above dynamic thresholds
    correct_predictions = 0
    total_evaluated = 0
    temp_buffer = []

    for entry in log:
        sample_id, value, label = entry
        baseline = sum([value % t for t in thresholds]) / len(thresholds)
        adjusted_value = value - baseline

        # Irrelevant smoothing step (distractor)
        smoothed = (adjusted_value + (value * 0.1)) / 1.1
        if smoothed < 0: 
            smoothed = 0
        temp_buffer.append(smoothed)

        # Actual decision logic
        if adjusted_value >= 0 and label == 'positive':
            correct_predictions += 1
        elif adjusted_value < 0 and label == 'negative':
            correct_predictions += 1
        total_evaluated += 1

    # Compute precision-like score
    precision_score = correct_predictions / total_evaluated if total_evaluated else 0

    # Secondary metric: consistency check using set operations (semi-relevant)
    unique_magnitudes = {int(abs(e[1])) for e in log}
    fluctuation_index = len([i for i in range(1, len(temp_buffer)) if abs(temp_buffer[i] - temp_buffer[i-1]) > 5])
    stability_bonus = 10 if fluctuation_index < 3 else 0  # capped bonus

    # Final scoring with weighted components
    base_points = int(precision_score * 100)
    adjustment = len(unique_magnitudes) % 7  # minor modifier
    final_score = base_points + stability_bonus - adjustment

    # Dead code path - never executed under current inputs (distractor)
    debug_mode = False
    if debug_mode:
        print(f'Debug: {correct_predictions}, {fluctuation_index}')

    return final_score

# Simulated classification log data
accuracy_log = [
    (101, 89, 'positive'),
    (102, 45, 'negative'),
    (103, 72, 'positive'),
    (104, 33, 'negative'),
    (105, 91, 'positive'),
    (106, 67, 'positive'),  # misclassified below threshold
    (107, 24, 'negative')
]

# Thresholds for adaptive baseline calculation
threshold_set = {8, 12, 17}

# Misleading auxiliary computation (irrelevant)
counterfeit_metric = sum([x[1] & 15 for x in accuracy_log])  # bitwise masking, unused

# Key execution point
final_score = evaluate_performance(accuracy_log, threshold_set)

# Output result
print(f"Result: {final_score}")