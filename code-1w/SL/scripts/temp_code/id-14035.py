def analyze_performance(metrics, thresholds):
    # Irrelevant transformation (distractor)
    normalized = [m / max(metrics) for m in metrics]
    weighted = list(map(lambda x: x * 1.5, normalized))

    # Key logic: count how many metrics exceed their corresponding threshold
    exceeded = 0
    for i, (metric, threshold) in enumerate(zip(metrics, thresholds)):
        if metric > threshold:
            exceeded += 1

    # Secondary path: calculate decay factor (not used in final result, but looks important)
    decay_factor = 0.0
    temp_sum = 0
    for j in range(len(weighted)):
        temp_sum += weighted[j] / (j + 1)
    decay_factor = round(temp_sum, 4)

    # Tertiary distractor: set operation that computes unused coverage
    expected_range = set(range(1, 101))
    observed_values = set([int(m) for m in metrics])
    coverage = len(observed_values.intersection(expected_range))

    return exceeded


def calculate_aggregate(data_points, config):
    base_tally = 0
    adjustment = 0

    # Simulate multi-stage processing with nested control flow
    for idx, point in enumerate(data_points):
        if idx % 2 == 0:
            base_tally += point ** 0.5
        else:
            base_tally -= point // 4

        # Misleading conditional branch (dead code due to structure)
        if point > 1000:
            adjustment += 1  # Never reached in current data

    # Use of enumerate and zip together (required idiom)
    offsets = [10, 5, -3, 8]
    for i, (d, o) in enumerate(zip(data_points, offsets)):
        if i % 2 == 1:
            base_tally += o  # Only odd indices contribute

    # Unused helper computation (adds interference)
    outlier_flags = [1 if abs(d - sum(data_points)/len(data_points)) > 20 else 0 for d in data_points]
    flagged_count = sum(outlier_flags)

    # Final aggregation uses only base_tally, ignoring adjustment and others
    aggregate = int(base_tally) + 50  # Constant offset for calibration
    return aggregate

# Main execution block
sensor_readings = [49, 64, 81, 100]
alert_levels = [45, 70, 80, 95]

exceeded_count = analyze_performance(sensor_readings, alert_levels)

scaling_factors = [2, 3, 1, 4]
transformed = []
for val, scale in zip(sensor_readings, scaling_factors):
    transformed.append(val * scale)

# Additional irrelevant state tracking
status_log = {}
for step in range(3):
    status_log[f'step_{step}'] = 'completed'

# Core answer computation
final_score = calculate_aggregate(transformed, {'mode': 'strict', 'window': 3})

# Print required output
print(f"Result: {final_score}")