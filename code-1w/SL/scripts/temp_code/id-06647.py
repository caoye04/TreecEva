def analyze_telemetry(data_stream):
    base_offset = 17
    temporal_weights = [0.8, 1.2, 0.9, 1.1]
    adjusted_values = []

    for i, point in enumerate(data_stream):
        if i % 2 == 0:
            adjusted_values.append(point * temporal_weights[i % len(temporal_weights)])
        else:
            adjusted_values.append(point + base_offset)

    filtered_data = [x for x in adjusted_values if x > 50]
    return filtered_data


def calculate_stability(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs) if diffs else 0.0


def calculate_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    penalty_factor = 0.0

    # Simulate system load interference (distractor logic)
    system_load = 0
    for _ in range(3):
        system_load += 1
        temp_debug = [system_load * j for j in range(5)]  # Dead computation

    # Real logic begins
    stability_metric = calculate_stability(metrics)
    if stability_metric > 5:
        penalty_factor = 0.15
    elif stability_metric > 3:
        penalty_factor = 0.08
    else:
        penalty_factor = 0.03

    # Apply penalty
    final_score = weighted_sum * (1 - penalty_factor)

    # Extra distraction: unused transformation
    normalized = list(map(lambda x: x / max(metrics), metrics))
    _ = [x * 100 for x in normalized]  # Computation with no use

    return int(final_score)

# Main execution
raw_input = [45, 60, 52, 70, 49, 80]
processed = analyze_telemetry(raw_input)

# Secondary distractor: irrelevant data transformation
buffer_state = [(i, val * 0.95) for i, val in enumerate(processed) if val < 100]

metrics = [68, 72, 65, 74]  # Final evaluation metrics
weights = [0.2, 0.3, 0.15, 0.35]

final_score = calculate_performance(metrics, weights)
print(f"Result: {final_score}")