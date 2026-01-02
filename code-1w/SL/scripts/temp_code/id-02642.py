def evaluate_performance(metrics, data):
    # Precompute auxiliary statistics (some irrelevant)
    total_entries = len(data)
    null_count = sum(1 for x in data if x < 0)
    adjustment_factor = 0.9 if null_count > 2 else 1.1

    # Distractor: complex but unused transformation
    transformed = list(map(lambda x: (x ** 2 + 3) * 0.5 for _ in range(2)), data))
    filtered_data = [x for x in data if x >= 0]

    # Actual logic begins: compute weighted score using metric weights
    base_weights = {'precision': 0.4, 'recall': 0.3, 'f1': 0.3}
    precision = sum(filtered_data) / len(filtered_data) if filtered_data else 0
    recall = sum(x * 0.9 for x in filtered_data) / len(filtered_data) if filtered_data else 0

    # Simulate conditional weight rebalancing (only triggered if avg > 50)
    average_val = sum(data) / len(data)
    if average_val > 50:
        base_weights['precision'] += 0.1
        base_weights['f1'] -= 0.1

    # F1 score approximation using harmonic combo (relevant)
    f1_component = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    # Build metric map dynamically (some keys are unused)
    metric_map = {
        'precision': precision * base_weights['precision'],
        'recall': recall * base_weights['recall'],
        'f1': f1_component * base_weights['f1'],
        'legacy_offset': null_count * adjustment_factor,
        'placeholder': len(transformed) % 7  # unused field
    }

    # Introduce distractor dictionary operations
    temp_ops = [{'op': lambda x: x * 1.05, 'key': k} for k in metric_map.keys()]
    applied = {t['key']: t['op'](v) for t, v in zip(temp_ops, metric_map.values())}

    # Final aggregation with selective inclusion
    valid_keys = ['precision', 'recall', 'f1']
    final_score = sum(applied[k] for k in valid_keys if k in applied)

    # Additional red herring: modify but don't use
    final_score_adjusted = final_score * adjustment_factor
    return int(final_score)  # deterministic integer output

# Input data with mixed characteristics
raw_data = [85, 72, -1, 90, 45, 68, -1, 88, 77]

# Key execution point
final_score = evaluate_performance(metric_map=None, raw_data=raw_data)
print(f"Result: {final_score}")