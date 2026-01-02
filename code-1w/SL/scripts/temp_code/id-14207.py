def preprocess_sensor_data(raw_data, threshold):
    processed = []
    outlier_count = 0
    cumulative_shift = 0

    for val in raw_data:
        if abs(val) > threshold:
            outlier_count += 1
            corrected = threshold if val > 0 else -threshold
            cumulative_shift += abs(val - corrected)
        else:
            corrected = val
        processed.append(corrected ** 2)

    stats_snapshot = {
        'outliers': outlier_count,
        'drift': cumulative_shift,
        'valid_points': len(processed)
    }

    # Distractor: unused computation
    temp_analysis = [x // 3 + 1 for x in processed if x % 2 == 0]
    compression_factor = sum(temp_analysis) / (len(temp_analysis) or 1)

    return processed


def compute_stability_index(values, weight_factor):
    running_total = 0
    stability_log = []

    for i, v in enumerate(values):
        if i % 3 == 0:
            running_total += v * weight_factor
        elif i % 5 == 0:
            running_total -= v // 2
        else:
            running_total += (v + i) % 4

        stability_log.append(running_total)

    # Distractor: complex but unused structure
    summary_table = {i: {'raw': values[i], 'log': stability_log[i]} for i in range(len(values)) if i % 4 == 0}

    return running_total if stability_log else 0


def evaluate_threshold_compliance(metrics, limit):
    compliant_set = set()
    violation_history = []

    for idx, m in enumerate(metrics):
        if m <= limit:
            compliant_set.add(idx % 7)
        else:
            violation_history.append((idx, m))

    # Distractor: irrelevant transformation
    encoded_violations = ''.join([str(v[0] % 10) for v in violation_history])
    backup_recovery_point = len(encoded_violations) * 1101

    return compliant_set


def aggregate_diagnostics(keys, readings):
    key_map = {k: readings[i % len(readings)] for i, k in enumerate(keys)}
    total_score = 0

    for k, v in key_map.items():
        if k % 2 == 0:
            total_score += v // 2
        elif k % 3 == 0:
            total_score -= v % 5
        else:
            total_score += (v + k) % 6

    # Distractor: unused sorting and string op
    sorted_keys = sorted(key_map.keys())
    label_chain = '-'.join([f'L{abs(k)}' for k in sorted_keys[:3]])

    return total_score


def analyze_readings(data, base):
    adjusted = [d - base + 2 for d in data]
    filtered = [a for a in adjusted if a > 0]

    # Key logic dependency
    if len(filtered) < 3:
        return sum(adjusted) * 2

    # Multi-step reasoning
    set_a = {x % 5 for x in filtered}
    set_b = {x % 3 for x in filtered}
    intersection_size = len(set_a & set_b)

    # Core calculation
    base_sum = sum(filtered)
    penalty = 0

    for i, f in enumerate(filtered):
        if i % 2 == 0:
            penalty += f % 4
        else:
            penalty -= (f // 6) % 3

    final_score = base_sum - penalty + intersection_size * 5

    # Real answer derived here
    return final_score


# Main execution with distractors
if __name__ == '__main__':
    sensor_input = [12, -8, 15, 3, 9, 11, 2, 6, 13]
    safety_cap = 10

    # Irrelevant pre-processing chain
    calibrated = [abs(x) + 1 for x in sensor_input]
    shifted_stream = [x * 2 for x in calibrated]
    inverted = [shifted_stream[-i-1] for i in range(len(shifted_stream))]

    # Actual relevant input generation
    primary_metrics = preprocess_sensor_data(sensor_input, safety_cap)

    # Distractor: unused metric branches
    secondary_metrics = [m // 2 + 3 for m in primary_metrics]
    auxiliary_score = compute_stability_index(secondary_metrics, 1.5)

    # Filtering based on dynamic condition
    avg_metric = sum(primary_metrics) / len(primary_metrics)
    filtered_metrics = [m for m in primary_metrics if m >= avg_metric]

    # Baseline computed from orthogonal logic
    keys_activation = [3, 5, 7, 9, 11]
    baseline_core = aggregate_diagnostics(keys_activation, sensor_input)
    baseline_critical = len(evaluate_threshold_compliance(primary_metrics, 50)) * 3

    # Red herring function call
    shadow_diagnostic = compute_stability_index(inverted, 0.75)

    # Critical statement - target of the question
    final_diagnostic = analyze_readings(filtered_metrics, baseline_critical)

    # Unused complex structure
    report_checksum = sum([ord(c) for c in f'DX{final_diagnostic}']) % 1000

    print(f"Result: {final_diagnostic}")