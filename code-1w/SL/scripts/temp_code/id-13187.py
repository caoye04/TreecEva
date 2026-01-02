from itertools import combinations
from math import log

# Simulated sensor data and diagnostic metrics
def analyze_sensor_readings(readings):
    base_metrics = set()
    temp_sum = 0
    count_high = 0

    for val in readings:
        temp_sum += val
        if val > 75:
            count_high += 1
        if val % 5 == 0:
            base_metrics.add(val)

    avg = temp_sum / len(readings) if readings else 0
    base_metrics.add(int(avg))

    # Distractor: irrelevant frequency map
    freq_map = {}
    for r in readings:
        freq_map[r] = freq_map.get(r, 0) + 1

    return base_metrics, avg, count_high


def generate_diagnostic_flags(metrics, threshold=60):
    flags = set()
    temp_flags = []

    for m in metrics:
        if m > threshold:
            flags.add(f'ALERT_{m}')
        elif m < threshold * 0.5:
            temp_flags.append(f'INFO_{m}')

    # Dead code path - never used
    if len(temp_flags) > 10:
        flags.add('OVERLOADED_BUFFER')

    return flags


def compute_stability_index(values, window=3):
    if len(values) < window:
        return 0.0

    stability = 0.0
    for i in range(len(values) - window + 1):
        window_vals = values[i:i+window]
        variance = sum((v - sum(window_vals)/window) ** 2 for v in window_vals) / window
        stability += variance

    # Irrelevant smoothing
    smoothed = max(0.1, min(100, stability / 10))
    return round(smoothed, 4)


def evaluate_performance(metric_set, raw_data):
    # Key logic chain starts here
    filtered = {x for x in metric_set if x % 4 == 2}
    pairs = list(combinations(filtered, 2))

    score_components = []

    for a, b in pairs:
        diff = abs(a - b)
        if diff > 10:
            score_components.append(diff // 2)

    # Secondary path with distractor variables
    temp_result = 0
    for comp in score_components:
        temp_result += comp * 1.5

    aggregate = int(sum(score_components))

    # Use of set operations: symmetric difference with fixed baseline
    baseline = {12, 18, 22, 34, 42}
    deviation = metric_set.symmetric_difference(baseline)
    penalty = len([d for d in deviation if d > 50])

    # Final computation
    final_score = aggregate - (penalty * 3)

    # Debugging remnants (irrelevant prints commented out)
    # print(f'Debug - deviation size: {len(deviation)}')
    # print(f'Temp result (unused): {temp_result}')

    return final_score

# Main execution block
sensor_data = [68, 72, 76, 80, 65, 90, 58, 74, 85]
metric_set, average_temp, high_count = analyze_sensor_readings(sensor_data)
diagnostic_set = generate_diagnostic_flags(metric_set)
stability = compute_stability_index(sensor_data)

final_score = evaluate_performance(metric_set, sensor_data)

print(f"Result: {final_score}")