def analyze_metrics(raw_data, config):
    # Preprocess: extract valid entries
    valid_entries = [x for x in raw_data if x > 0]
    offset_correction = sum(valid_entries) / len(valid_entries) if valid_entries else 0

    # Misleading transformation (not used in final path)
    transformed = [round(x ** 0.5 + offset_correction) for x in valid_entries]
    temp_sum = sum(transformed) * 0.95  # Distractor computation

    # Core logic begins
    normalized = [x / (offset_correction + 1e-5) for x in valid_entries]
    squared_devs = [(x - 1.0) ** 2 for x in normalized]
    avg_deviation = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    return avg_deviation


def evaluate_performance(metrics, data):
    # Use set operations to filter active metrics
    required_fields = {'latency', 'throughput', 'accuracy'}
    optional_fields = {'jitter', 'power', 'cost'}
    provided_fields = set(metrics.keys())

    missing = required_fields - provided_fields
    if missing:
        return -1  # Invalid configuration

    # Track auxiliary state (some irrelevant)
    status_flags = {}
    for field in provided_fields:
        if field in optional_fields:
            status_flags[field] = 'optional_present'
        else:
            status_flags[field] = 'required_verified'

    # Real computation starts
    base_score = 0.0
    weights = {'latency': 0.4, 'throughput': 0.35, 'accuracy': 0.25}
    
    # Simulate calibration using string-based keys
    metric_names = [k.upper() for k in weights.keys()]
    calibrated = {k: metrics[k] * weights[k] for k in weights}
    
    # Additional distraction: enumerate and zip usage (semi-relevant)
    adjustments = [0.1, -0.05, 0.02]
    for i, (name, val) in enumerate(zip(metric_names, calibrated.values())):
        # This loop modifies nothing; just adds noise
        _temp = val * (1 + adjustments[i % 3])

    base_score = sum(calibrated.values())

    # Apply penalty based on deviation from expected range
    deviations = []
    expected_ranges = {
        'latency': (0.1, 100),
        'throughput': (1000, 10000),
        'accuracy': (0.8, 1.0)
    }
    for key, rng in expected_ranges.items():
        val = metrics[key]
        if not (rng[0] <= val <= rng[1]):
            deviations.append((val - rng[0]) if val < rng[0] else (val - rng[1]))

    penalty = sum(abs(d) for d in deviations) * 0.01
    final_score = base_score - penalty

    # Dead code branch (never reached due to logic above)
    if len(provided_fields) == 0:
        fallback = sum(data) / len(data)
        final_score = fallback  # Not executed

    return final_score

# Main execution
raw_input_data = [12, 45, 23, 67, 34, 89]
dummy_config = {'version': '2.1', 'mode': 'test'}

# Simulate sensor drift correction (irrelevant to final result)
corrected_readings = [x * 0.99 for x in raw_input_data]
aggregate_reading = sum(corrected_readings)

# Key data structures
metric_set = {
    'latency': 45.0,
    'throughput': 7200,
    'accuracy': 0.93
}
benchmark_data = [5, 10, 15, 20]

interim_analysis = analyze_metrics(raw_input_data, dummy_config)
final_score = evaluate_performance(metric_set, benchmark_data)

print(f"Result: {final_score}")