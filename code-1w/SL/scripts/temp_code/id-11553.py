from collections import defaultdict
from itertools import cycle

# Simulated sensor data processing pipeline with performance evaluation

def collect_diagnostics(raw_samples):
    diagnostics = defaultdict(int)
    temp_flags = [0] * len(raw_samples)
    for i, sample in enumerate(raw_samples):
        if sample > 300:
            diagnostics['high'] += 1
            temp_flags[i] = 1
        elif sample < 100:
            diagnostics['low'] += 1
            temp_flags[i] = -1
        else:
            diagnostics['normal'] += 1
    # Irrelevant transformation
    adjusted_flags = [f * 2 for f in temp_flags if f != 0]
    return dict(diagnostics), adjusted_flags

def compute_variance(data):
    mean = sum(data) / len(data)
    squared_diffs = [(x - mean) ** 2 for x in data]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance

def apply_calibration(readings, factor=1.05):
    calibrated = []
    for r in readings:
        corrected = r * factor
        if corrected > 350:
            corrected = 350
        calibrated.append(corrected)
    # Dead code path - never used
    outlier_count = sum(1 for c in calibrated if c > 340)
    scaling_log = {i: val * 0.99 for i, val in enumerate(calibrated)}
    return calibrated

def filter_anomalies(seq):
    window_size = 3
    filtered = seq[:]
    for i in range(window_size, len(seq)):
        window = seq[i - window_size:i]
        avg_window = sum(window) / window_size
        if abs(seq[i] - avg_window) > 50:
            filtered[i] = avg_window
    return filtered

def generate_weight_map(n):
    # Distractor function - generates weights but only one value is actually used
    base_weights = [0.1 * (i + 1) for i in range(n)]
    weight_cycle = cycle(base_weights)
    full_weights = [next(weight_cycle) for _ in range(2 * n)]
    truncated = full_weights[:n]
    inverted = [1.0 / w for w in truncated]
    normalized = [w / sum(truncated) for w in truncated]
    return normalized

def evaluate_performance(metrics, weights):
    score_components = []
    for i, (k, v) in enumerate(metrics.items()):
        contribution = v * weights[i % len(weights)]
        score_components.append(contribution)
    raw_score = sum(score_components)
    penalty = 0
    if metrics.get('high', 0) > 5:
        penalty += 15
    if metrics.get('low', 0) > 3:
        penalty += 10
    adjusted_score = raw_score - penalty
    final_score = round(adjusted_score, 4)
    return final_score

# Main execution flow
if __name__ == '__main__':
    # Input data - simulated system telemetry
    telemetry_data = [
        98, 105, 305, 210, 70, 180, 320, 250, 85, 190,
        310, 200, 65, 220, 330, 175, 90, 240, 302, 160
    ]

    # Step 1: Collect diagnostic counts
    diag_counts, flags = collect_diagnostics(telemetry_data)

    # Step 2: Apply calibration (result used indirectly via filtering)
    calibrated_data = apply_calibration(telemetry_data, factor=1.03)

    # Step 3: Filter anomalies based on local windows
    cleaned_data = filter_anomalies(calibrated_data)

    # Step 4: Compute statistical variance (distractor - not used in final score)
    variance = compute_variance(cleaned_data)
    std_deviation = variance ** 0.5
    noise_level = 'high' if std_deviation > 80 else 'low'

    # Step 5: Generate weights map (only first few elements matter)
    weights = generate_weight_map(4)

    # Step 6: Define actual performance metrics used in scoring
    performance_metrics = {
        'throughput': 85,
        'latency': 72,
        'reliability': 93,
        'high': diag_counts['high'],      # From diagnostics
        'low': diag_counts['low']         # From diagnostics
    }

    # Step 7: Evaluate final performance score
    final_score = evaluate_performance(performance_metrics, weights)

    # Output result
    print(f"Result: {final_score}")