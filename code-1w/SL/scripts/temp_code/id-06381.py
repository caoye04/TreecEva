import math

# Simulated sensor readings and system thresholds
def collect_diagnostics(raw_readings):
    normalized = [round(x * 0.98 + 2.1, 2) for x in raw_readings]
    offset = sum(normalized) / len(normalized)
    adjusted = [x - offset for x in normalized]
    return adjusted

# Legacy function – unused but looks relevant
def legacy_calibrate(data):
    return [d * 0.5 for d in data if d > 0]

# Signal filter using string-based tagging (red herring)
def tag_anomalies(values):
    labels = []
    for v in values:
        if v > 0:
            labels.append('POS')
        elif v < 0:
            labels.append('NEG')
        else:
            labels.append('ZERO')
    # Use of string methods as required
    joined = ''.join(labels).replace('POS', 'P').replace('NEG', 'N')
    return joined.count('P') - joined.count('N')

# Core metric aggregator with distraction paths
def aggregate_metrics(readings, limits):
    # Irrelevant preprocessing block (distraction)
    temp_snapshot = readings[::2]  # Every other reading – unused
    temp_snapshot = [t * 1.1 for t in temp_snapshot if t != 0]

    # Actual computation begins
    clipped = [max(min(r, limits['upper']), limits['lower']) for r in readings]
    squared_errors = [(x - 0.5) ** 2 for x in clipped]
    mse = sum(squared_errors) / len(squared_errors)
    rmse = math.sqrt(mse)

    # Bitwise red herring: use of irrelevant bit logic on indices
    indices_effect = 0
    for i in range(len(clipped)):
        indices_effect ^= i & 7  # Cumulative XOR – never used again

    # Conditional path that appears important but is bypassed
    if rmse < 0.1:
        adjustment_factor = 10
    else:
        adjustment_factor = 1  # This will always be taken

    # Destructuring assignment (required concept)
    first_val, *rest_vals = clipped
    peak = max(rest_vals) if rest_vals else first_val

    # Complex conditional expression with short-circuit (logic)
    penalty = (len([r for r in clipped if r > 0.7]) > 3) and (peak > 0.9) or False
    penalty_score = 15 if penalty else 0

    # Final computation chain
    base_score = rmse * 1000
    debug_offset = len([x for x in readings if x < 0]) % 4  # Looks suspicious but minor
    final_diagnostic = int(base_score - debug_offset + penalty_score)

    # Dead code: early return simulation that doesn't trigger
    if False:
        return -999  # Decoy result

    return final_diagnostic

# Unused helper – looks like it's part of pipeline
def validate_consistency(arr):
    return all(abs(arr[i] - arr[i+1]) < 1 for i in range(len(arr)-1))

# Main execution
if __name__ == '__main__':
    # Real input data
    sensor_input = [0.12, 0.34, 0.67, 0.89, 0.45, 0.73, 0.91, 0.55, 0.77, 0.21]
    threshold_config = {'lower': 0.05, 'upper': 0.85}

    # Preprocess (only this matters)
    processed = collect_diagnostics(sensor_input)

    # Critical statement
    final_diagnostic = aggregate_metrics(processed, threshold_config)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")