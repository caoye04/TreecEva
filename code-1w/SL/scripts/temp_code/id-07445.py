import itertools

# Simulated sensor array diagnostics with red herrings
def analyze_sensor_fusion(raw_readings):
    if not raw_readings:
        return 0

    # Irrelevant transformation (decoy)
    transformed = [x ** 2 + 3 for x in raw_readings if x > 0]
    filtered = list(filter(lambda x: x % 2 == 1, transformed))

    # Real but obscured computation path
    base_scores = [abs(x - 5) for x in raw_readings]
    adjustments = [(i * 0.1) for i, _ in enumerate(base_scores)]
    scored = [base_scores[i] - adjustments[i] for i in range(len(base_scores))]

    # Dead code path - never reached due to logic above
    if len(transformed) > 100:
        fallback = sum(transformed) // len(transformed)
        return fallback

    return sum(scored) / len(scored) if scored else 0

# Legacy system compatibility layer (mostly irrelevant)
def legacy_calibrate(data, mode="passive"):
    if mode == "active":
        return [x * 0.95 for x in data]
    elif mode == "debug":
        return [x + 1 for x in data]
    else:
        return data  # Default passthrough

# Core processing with distractors
def compute_phase_shift(elements):
    shift = 0
    accumulator = 0
    history = []

    for idx, val in enumerate(elements):
        if idx % 3 == 0:
            shift += val * 0.1
        elif idx % 3 == 1:
            shift -= val * 0.05
        else:
            accumulator += val
        
        # Distractor: tracking unused metric
        snapshot = {'index': idx, 'value': val, 'shift': round(shift, 3)}
        history.append(snapshot)
    
    # Unused complex structure
    metadata_tree = {
        'version': '2.1a',
        'nodes': [
            {'id': i, 'status': 'ok'} for i in range(len(history))
        ],
        'checksum': sum(h['index'] * h['value'] for h in history) % 17
    }

    return shift  # Only this matters

# Primary aggregation function with multiple concepts
def aggregate_metrics(time_series, influence_weights):
    # Misleading pre-processing
    normalized = [x / max(time_series) if max(time_series) != 0 else 0 for x in time_series]
    zipped_pairs = list(zip(normalized, influence_weights))
    weighted_sum = sum(a * b for a, b in zipped_pairs)

    # Complex but irrelevant grouping
    grouped = {}
    for key, group in itertools.groupby(zipped_pairs, key=lambda pair: int(pair[0] * 10)):
        grouped[key] = list(group)

    # Actual signal extraction (obscured)
    trend_component = compute_phase_shift(time_series)
    secondary_score = analyze_sensor_fusion(time_series)

    # Critical combination step (answer depends on this)
    diagnostic_base = weighted_sum * 100
    adjustment_factor = abs(trend_component - (secondary_score / 10))
    final_diagnostic = int(diagnostic_base - adjustment_factor * 50)

    # Dead assignment - looks important but unused
    audit_trail = {
        'raw_input': time_series,
        'weights_applied': influence_weights,
        'subscores': [diagnostic_base, trend_component, secondary_score],
        'final_raw': diagnostic_base - adjustment_factor * 50
    }

    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Input data
    readings = [4, 7, 2, 9, 1, 6, 3]
    importance = [0.2, 0.3, 0.1, 0.4, 0.1, 0.5, 0.2]

    # Legacy calibration (no effect due to passive mode)
    calibrated = legacy_calibrate(readings, mode="passive_override")

    # Generate auxiliary metrics (distraction)
    avg_reading = sum(calibrated) / len(calibrated)
    peak_deviation = max(abs(x - avg_reading) for x in calibrated)
    entropy_proxy = sum(-x * x for x in normalized := [r / sum(readings) for r in readings])

    # Key data structures with cross-references (some irrelevant)
    trend_data = [x * 1.1 for x in calibrated]
    weights = [w * 1.05 for w in importance]

    # Statement of interest
    final_diagnostic = aggregate_metrics(trend_data, weights)
    
    # Output result
    print(f"Result: {final_diagnostic}")