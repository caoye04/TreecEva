def analyze_performance_metrics(values, config):
    total_points = 0
    temp_sum = 0
    adjustment_factor = config.get('adjustment', 1.0)
    penalty_rate = config.get('penalty', 0.1)
    base_threshold = config.get('threshold', 50)

    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    processed_chunks = []
    cumulative_noise = 0.0

    for i, val in enumerate(values):
        if val < 0:
            outlier_count += 1
            continue

        # Real computation begins
        if val > base_threshold:
            total_points += int((val - base_threshold) * adjustment_factor)
        else:
            temp_sum += val % 7

        # Distractor: noise accumulation with no real impact
        for j in range(2):
            cumulative_noise += (i + j) * 0.01

        # Early break that rarely triggers (misleading path)
        if i == 5 and val > 1000:
            break

    # Semi-relevant transformation
    intermediate = (total_points + temp_sum) % 97

    # Dead code path (distractor)
    if len(processed_chunks) > 100:
        intermediate *= 2

    return intermediate


def calculate_adjusted_efficiency(entries, limits):
    data_stream = [x * 2 for x in entries if x % 2 == 1]  # Only odd values doubled
    filtered_data = [x for x in data_stream if x < limits['max_val']]

    # Use of zip and enumerate (required Python features)
    indexed_weights = []
    for idx, (a, b) in enumerate(zip(filtered_data, reversed(filtered_data))):
        weight = (a + b) * (idx % 4 + 1)
        indexed_weights.append(weight)

        # Redundant computation
        if idx % 3 == 0:
            _ = a ** 0.5  # Not stored or used

    # Core logic mixed with distraction
    raw_efficiency = sum(indexed_weights) // len(indexed_weights) if indexed_weights else 0

    # Extra steps with modular arithmetic
    modifier = sum([i * w % 5 for i, w in enumerate(indexed_weights)])
    adjusted_efficiency = (raw_efficiency + modifier) % 83

    # Misleading state tracking
    history_log = []
    for val in indexed_weights:
        history_log.append(f"Entry:{val%10}")  # Unused side info

    # Final result calculation
    scaling_constant = limits.get('scale', 3)
    final_score = (adjusted_efficiency * scaling_constant) - 15

    return final_score

# Main execution
if __name__ == "__main__":
    data_points = [23, 45, 67, 89, 12, 34, 56, 78, 91]
    thresholds = {"max_val": 150, "scale": 4}
    config_params = {"adjustment": 1.2, "penalty": 0.05, "threshold": 40}

    # Call to helper function (distractor)
    _ = analyze_performance_metrics(data_points, config_params)

    # Key statement
    final_score = calculate_adjusted_efficiency(data_points, thresholds)

    print(f"Result: {final_score}")