from collections import defaultdict
from itertools import combinations

# Simulated sensor data analysis with performance scoring
def analyze_sensor_array(raw_readings):
    processed = defaultdict(int)
    anomalies = set()
    temp_buffer = []

    for idx, reading in enumerate(raw_readings):
        if reading % 7 == 0:
            processed['divisible_by_7'] += 1
        if reading > 50 and reading % 2 == 1:
            anomalies.add(idx)
            processed['high_odd'] += reading // 10

        temp_buffer.append(reading * 0.1)

    # Irrelevant smoothing operation (dead-end computation)
    smoothed = [temp_buffer[i] + temp_buffer[i-1]*0.5 for i in range(1, len(temp_buffer))]
    smoothed_sum = sum(smoothed)

    return processed, anomalies, smoothed_sum

# Metric evaluation logic
def compute_derived_metrics(base_stats):
    score = 0
    penalty = 0

    if 'divisible_by_7' in base_stats:
        score += base_stats['divisible_by_7'] * 3
    if 'high_odd' in base_stats:
        score += base_stats['high_odd'] * 2
        # Misleading redundant check
        if base_stats['high_odd'] > 10:
            penalty += 5

    # Fake complexity: unused transformation
    transformed = {k: v**2 for k, v in base_stats.items()}
    total_transformed = sum(transformed.values())

    return score - penalty

# Final performance evaluator
def evaluate_performance(metrics, baseline):
    base_value = sum(baseline) % 100
    adjustment = 0

    # Nested logic with moderate depth
    if len(metrics) >= 2:
        adjustment += 10
        if 'divisible_by_7' in metrics:
            if metrics['divisible_by_7'] > 3:
                adjustment += 5
            else:
                adjustment -= 2

    raw_score = compute_derived_metrics(metrics)
    final_score = (raw_score + base_value + adjustment) % 89

    # Dead code path: never accessed under normal execution
    debug_trace = []
    for i in range(3):
        debug_trace.append(f"step_{i}")

    return final_score

# Main execution
sensor_readings = [42, 55, 14, 61, 70, 33, 84, 95]
stats, flagged, _ = analyze_sensor_array(sensor_readings)
baseline_data = [12, 18, 24, 30]

# Key computational statement
final_score = evaluate_performance(stats, baseline_data)
print(f"Result: {final_score}")