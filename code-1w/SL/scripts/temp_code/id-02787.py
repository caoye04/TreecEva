from collections import defaultdict

# Simulate sensor data aggregation and performance scoring
def collect_diagnostics(sensor_logs):
    diagnostics = defaultdict(int)
    temp_flags = [0] * len(sensor_logs)

    for i, log in enumerate(sensor_logs):
        if 'ERROR' in log:
            diagnostics['errors'] += 1
            temp_flags[i] = 1
        elif 'WARNING' in log:
            diagnostics['warnings'] += 1
            temp_flags[i] = 2
        else:
            diagnostics['clean'] += 1
            temp_flags[i] = 0

    # Irrelevant transformation (distractor)
    adjusted_flags = [f * 1.5 for f in temp_flags]
    total_adjusted = sum(adjusted_flags)

    return diagnostics, total_adjusted

def compute_baseline(deviation_list):
    base = sum(d % 7 for d in deviation_list)  # Modular arithmetic distraction
    extra_offset = 0
    for d in deviation_list:
        if d > 5:
            extra_offset += d // 5
    return base + extra_offset

def evaluate_performance(weights, metrics):
    score = 0.0
    normalization_factor = sum(weights.values()) + 1e-8

    # Relevant scoring logic
    for k, w in weights.items():
        if k in metrics:
            score += (metrics[k] * w) / normalization_factor

    # Dead computation path (distractor)
    outlier_count = 0
    for v in metrics.values():
        if v > 100:
            outlier_count += 1
    dummy_penalty = outlier_count * 0.01  # Not used

    return int(score)

# Main execution
if __name__ == '__main__':
    logs = [
        'STATUS_OK', 'ERROR_CRITICAL', 'WARNING_LOW', 'STATUS_OK',
        'WARNING_HIGH', 'ERROR_MINOR', 'STATUS_OK', 'STATUS_OK'
    ]
    deviations = [3, 8, 12, 5, 9, 14]

    # Collect diagnostic counts
    raw_metrics, adjustment_sum = collect_diagnostics(logs)

    # Compute baseline (semi-relevant)
    baseline_value = compute_baseline(deviations)

    # Weight configuration for evaluation
    metric_weights = {
        'errors': 10,
        'warnings': 5,
        'clean': 1,
        'missing': 3
    }

    # Introduce irrelevant derived metric
    total_entries = len(logs)
    error_rate = raw_metrics['errors'] / total_entries if total_entries else 0
    inverse_rate = (1 - error_rate) * 100

    # Key statement
    final_score = evaluate_performance(metric_weights, raw_metrics)

    print(f"Result: {final_score}")