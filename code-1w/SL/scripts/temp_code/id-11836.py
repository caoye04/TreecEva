import math

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [23.4, 19.8, 25.6, 20.1, 27.3, 18.9, 22.0, 24.5]
    calibration_offset = 1.2
    threshold = 21.5
    temp_stats = {}
    adjusted_readings = []

    # Irrelevant statistical placeholders (distractors)
    outlier_count = 0
    stability_index = 0.0
    noise_floor = 0.05
    peak_reading = max(raw_readings)
    baseline_average = sum(raw_readings) / len(raw_readings)

    # Apply offset and filter significant readings
    for val in raw_readings:
        adjusted = val + calibration_offset
        adjusted_readings.append(round(adjusted, 2))

    above_threshold = [v for v in adjusted_readings if v > threshold]

    # Compute moving average over window of 3 (unused red herring)
    moving_averages = []
    for i in range(len(adjusted_readings) - 2):
        avg = (adjusted_readings[i] + adjusted_readings[i+1] + adjusted_readings[i+2]) / 3
        moving_averages.append(round(avg, 2))

    # Destructuring assignment with dummy variables
    first, *middle, last = adjusted_readings

    # Dictionary operations: group by integer part
    grouped_by_int = {}
    for v in adjusted_readings:
        int_part = int(v)
        if int_part not in grouped_by_int:
            grouped_by_int[int_part] = []
        grouped_by_int[int_part].append(v)

    # Set operations to find unique ceiling values (distraction)
    ceiling_set = set(math.ceil(x) for x in adjusted_readings)
    floor_set = set(math.floor(x) for x in adjusted_readings)
    common_bounds = ceiling_set.intersection(floor_set)

    # Real processing begins: only this matters
    processed_logs = []
    for entry in above_threshold:
        # Transform using non-linear scaling
        transformed = math.log(entry) * 10
        processed_logs.append(round(transformed, 3))

    return processed_logs


def analyze_readings(logs):
    # Initialize various irrelevant accumulators
    total_entries = len(logs)
    cumulative_sum = 0.0
    fluctuation_score = 0.0
    decay_factor = 0.95
    trend_sequence = []

    # String-based tagging (irrelevant but plausible)
    labels = ['A', 'B', 'C', 'D', 'E']
    tag_map = {i: label for i, label in enumerate(labels)}
    encoded_tags = [tag_map.get(i % 5, 'X') for i in range(len(logs))]
    tagged_data = dict(zip(range(len(logs)), encoded_tags))

    # Set operation: simulate filtering by category
    valid_indices = set(range(len(logs)))
    excluded_indices = {0, 2, 4}
    active_indices = valid_indices - excluded_indices

    # Actual computation path
    weighted_total = 0.0
    for i, reading in enumerate(logs):
        weight = math.sin(i + 1) ** 2 + 0.5  # damping factor
        weighted_total += reading * weight

    # Secondary transformation
    intermediate_result = abs(weighted_total) * 1.75

    # Final adjustment based on length and pattern
    length_factor = len(logs) ** 1.5
    final_diagnostic = intermediate_result - (length_factor * 2.1)

    # Dead code branch (never executed - misleading)
    if False:
        backup_repair = sum(logs) / math.pi
        final_diagnostic = backup_repair * 100

    # Decoy function definition
    def legacy_compatibility_mode():
        return sum(logs) // len(logs)

    return round(final_diagnostic, 6)

# Main execution flow
processed_logs = collect_diagnostics()
final_diagnostic = analyze_readings(processed_logs)
print(f"Result: {final_diagnostic}")