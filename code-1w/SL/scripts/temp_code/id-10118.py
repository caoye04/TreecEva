def evaluate_model(ground_truth, predicted):
    confusion_matrix = {}
    class_counts = set(ground_truth)
    tp = 0
    fp = 0
    fn = 0

    for cls in class_counts:
        for i in range(len(ground_truth)):
            if ground_truth[i] == cls and predicted[i] == cls:
                tp += 1
            elif ground_truth[i] != cls and predicted[i] == cls:
                fp += 1
            elif ground_truth[i] == cls and predicted[i] != cls:
                fn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    dummy_calc = sum([i * i for i in range(5)])  # Irrelevant computation
    temp_buffer = [x for x in range(len(predicted)) if x % 7 == 0]  # Dead-end list

    return f1


def process_results(dataset, preds):
    baseline_shift = 0.1
    adjustment_factor = len(dataset) % 3
    raw_f1 = evaluate_model(dataset, preds)

    adjusted_f1 = raw_f1 + baseline_shift * adjustment_factor

    outlier_filter = lambda x: x > 0.5
    filtered = list(filter(outlier_filter, preds))  # Misleading use

    # Simulated confidence scaling (not affecting result)
    confidence_scores = {i: round((preds[i] + dataset[i]) / 2, 3) for i in range(len(preds))}
    avg_confidence = sum(confidence_scores.values()) / len(confidence_scores) if confidence_scores else 0

    # Distractor: unused dictionary operations
    stats_summary = {
        'size': len(dataset),
        'f1_raw': raw_f1,
        'adjusted': adjusted_f1,
        'confidence': avg_confidence
    }
    stats_summary.update({'version': '2.1'})

    final_value = adjusted_f1 * 1000  # Scale to integer-friendly output
    return int(final_value)

# Main execution
validation_set = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
predictions = [1, 1, 1, 0, 0, 1, 0, 1, 1, 0]

intermediate_metric = sum(a ^ b for a, b in zip(validation_set, predictions))  # XOR-based error count (unused)
duplicate_check = len(set(validation_set)) == len(validation_set)  # Always false, irrelevant

final_score = process_results(validation_set, predictions)
print(f"Result: {final_score}")