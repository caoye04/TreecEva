def analyze_metrics(entries):
    totals = [0] * len(entries[0])
    counts = [0] * len(entries[0])
    for entry in entries:
        for i, val in enumerate(entry):
            if val > 0:
                totals[i] += val
                counts[i] += 1
    return [totals[i] / counts[i] if counts[i] else 0 for i in range(len(totals))]


def calculate_performance(data):
    # Irrelevant preprocessing: normalize string labels
    label_map = {k: v for k, v in enumerate('abcde')}
    reversed_labels = {v: k for k, v in label_map.items()}
    temp_shift = sum(reversed_labels[c] for c in 'bcde')  # Distractor computation

    # Real logic begins: filter valid records based on threshold
    threshold = 2.5
    filtered_data = [row for row in data if all(x >= threshold or x == 0 for x in row)]

    # Compute column averages using helper function
    avg_metrics = analyze_metrics(filtered_data)

    # Secondary distractor: simulate unused weight adjustments
    weights = [1.1, 0.9, 1.2, 0.8, 1.0]
    adjusted_weights = [w * 1.05 for w in weights]
    shift_factor = sum(adjusted_weights) - sum(weights)

    # Core calculation: weighted sum of average metrics
    weighted_sum = sum(avg_metrics[i] * weights[i] for i in range(len(avg_metrics)))

    # Additional red herring: tuple unpacking with unused values
    metadata_tuple = (len(data), len(filtered_data), sum(counts := [len(row) for row in data]))
    original_count, filtered_count, total_elements = metadata_tuple

    # Final performance score with offset (shift_factor is irrelevant)
    final_score = int(weighted_sum - 0.5 + shift_factor * 0)  # shift_factor used but multiplied by 0

    return final_score

# Simulated benchmark dataset (5 features per entry)
benchmark_data = [
    [3.0, 2.0, 4.5, 0.0, 3.2],
    [2.6, 3.1, 0.0, 2.9, 3.8],
    [3.3, 0.0, 5.0, 3.1, 4.1],
    [0.0, 2.4, 4.8, 3.0, 3.9],
    [2.7, 2.8, 4.6, 3.3, 4.0]
]

# Execution point
final_score = calculate_performance(benchmark_data)
print(f"Target result: {final_score}")