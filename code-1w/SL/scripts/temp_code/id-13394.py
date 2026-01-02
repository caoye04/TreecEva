def analyze_workload(inputs):
    # Irrelevant preprocessing
    temp_buffer = [x ^ 255 for x in inputs if x % 2 == 0]
    checksum = sum(temp_buffer) % 1000

    # Distractor: complex but unused transformation
    transformed = []
    for i in range(len(inputs)):
        if i > 0 and inputs[i] > inputs[i-1]:
            val = (inputs[i] << 2) | 7
            transformed.append(val)

    # Real logic starts: filter critical thresholds
    critical_values = [x for x in inputs if x > 50 and x < 200]
    if len(critical_values) == 0:
        return 0

    # Bit manipulation red herring
    masked_values = [v & 0xFF for v in critical_values]
    xor_fingerprint = 0
    for m in masked_values:
        xor_fingerprint ^= m

    # Unused recursive distraction
    def explore_paths(depth, limit):
        if depth >= limit:
            return 1
        return depth + explore_paths(depth + 2, limit - 1)

    # Meaningless aggregation
    entropy_proxy = 0
    for cv in critical_values:
        if cv % 7 == 0:
            entropy_proxy += cv // 7

    # Actual relevant path: count how many passed dynamic threshold
    threshold = len(critical_values) * 2 + (xor_fingerprint % 10)
    passed = sum(1 for v in critical_values if v > threshold)

    # Dead code path — never reached due to condition above
    if len(critical_values) > 100:
        backup_metric = (passed * 1000) // len(critical_values)
        return backup_metric

    return passed


def validate_stability(readings):
    # Set operation distraction
    unique_readings = set(readings)
    anomalies = {r for r in unique_readings if r < 10}
    baseline = sum(unique_readings) / len(unique_readings)

    # Conditional expression decoy
    status_flag = 1 if len(anomalies) > 5 else -1

    # Irrelevant smoothing
    smoothed = []
    for i in range(1, len(readings)-1):
        avg = (readings[i-1] + readings[i] + readings[i+1]) / 3
        smoothed.append(avg)

    # Unused peak detection
    peaks = []
    for i in range(1, len(smoothed)-1):
        if smoothed[i] > smoothed[i-1] and smoothed[i] > smoothed[i+1]:
            peaks.append(smoothed[i])

    # Fake normalization
    normalized = [round(s / baseline, 3) for s in smoothed]

    # Real signal: count values above baseline
    return sum(1 for r in readings if r > baseline)


def evaluate_performance(metrics, data):
    # Combine two analysis results via conditional expression
    score_a = analyze_workload(data['workload']) if 'workload' in metrics else 0
    score_b = validate_stability(data['stability']) if 'stability' in metrics else 0

    # Bitwise red herring
    magic_key = (score_a << 1) ^ (score_b >> 2) & 0xFFFF

    # Decoy calculation with set operations
    fake_components = {score_a, score_b, magic_key}
    if len(fake_components) > 2:
        adjustment = sum(fake_components) % 7
    else:
        adjustment = 0

    # Critical distractor: misleading intermediate formula
    pseudo_entropy = score_a * 0.7 + score_b * 0.3 + adjustment

    # Actual answer derivation
    base_performance = score_a + score_b
    bonus = 10 if base_performance >= 15 else 0
    penalty = 5 if magic_key % 13 == 0 else 0

    final_score = base_performance + bonus - penalty

    # This print is required to expose the result
    print(f"Result: {final_score}")
    return final_score


# Input data
metric_set = ['workload', 'stability']
benchmark_data = {
    'workload': [65, 70, 55, 80, 45, 90, 120, 150, 180],
    'stability': [85, 92, 78, 63, 99, 88, 76, 95, 102]
}

# Execution point
final_score = evaluate_performance(metric_set, benchmark_data)