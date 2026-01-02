def evaluate_performance(metrics, base):
    # Initialize various tracking variables
    temp_result = 0
    accumulator = 0
    intermediate = set()
    outlier_count = 0  # distractor: not used in final logic

    # Baseline thresholds (some are red herrings)
    thresholds = {'t1': 5, 't2': 12, 't3': 8, 't4': 20}
    adjustment_factor = 1.5  # used later

    for metric in metrics:
        if metric in base:
            accumulator += base[metric]
            if base[metric] > thresholds['t3']:
                intermediate.add(metric)

    # Simulate some complex processing
    processed_values = [accumulator * 2]
    for i in range(2):  # two iterations only
        processed_values.append(processed_values[-1] // (i + 2))

    # Distractor block: dead logic that doesn't affect outcome
    debug_snapshot = []
    for val in processed_values:
        if val % 2 == 0 and val > 10:
            debug_snapshot.append(val ** 0.5)

    # Real computation begins
    shift_value = len(intermediate) * 3
    temp_result = processed_values[1] + shift_value

    # Apply adjustment using constant
    temp_result = int(temp_result * adjustment_factor)

    # Final logic: use set difference to determine bonus
    expected_metrics = {'m1', 'm2', 'm3', 'm4', 'm5'}
    missing = expected_metrics - metrics
    bonus = 5 if len(missing) == 0 else -2 * len(missing)

    final_score = temp_result + bonus
    return final_score

# Main execution
baseline_data = {
    'm1': 6,
    'm2': 10,
    'm3': 15,
    'm4': 3
}
metric_set = {'m1', 'm2', 'm3', 'm4'}

# Trigger the key statement
final_score = evaluate_performance(metric_set, baseline_data)
print(f"Result: {final_score}")