from itertools import compress, cycle

# Simulate sensor data reliability and performance metrics
def analyze_reliability(readings):
    base_avg = sum(readings) / len(readings)
    variance = sum((x - base_avg) ** 2 for x in readings) / len(readings)
    threshold = base_avg * 0.1
    stable = [abs(r - base_avg) < threshold for r in readings]
    return stable, base_avg

# Generate synthetic telemetry data
telemetry = [104.3, 105.1, 99.8, 103.0, 107.2, 101.9, 100.4, 102.6]

# Analyze signal stability
reliable_flags, avg_value = analyze_reliability(telemetry)

corrected_values = [v for v, r in zip(telemetry, reliable_flags) if r]
dummy_offset = sum(1.0 for _ in range(3)) * 0.5  # Irrelevant computation
adjusted_avg = (sum(corrected_values) + dummy_offset) - dummy_offset  # Neutralized effect

# Weight initialization with cycling pattern
weight_pattern = [0.8, 1.2, 0.9]
weights = list(cycle(weight_pattern))[:len(corrected_values)]

# Performance metrics including derived statistics
metric_a = adjusted_avg * 0.95
metric_b = sum(corrected_values[i] * weights[i] for i in range(len(corrected_values)))
metric_c = len([v for v in corrected_values if v > adjusted_avg])

metrics = (metric_a, metric_b, metric_c)

# Secondary analysis (unused, distraction)
rolling_deltas = [telemetry[i+1] - telemetry[i] for i in range(len(telemetry)-1)]
spike_count = sum(1 for d in rolling_deltas if abs(d) > 2.0)

# Core evaluation logic
def evaluate_performance(perf_metrics, scaling_weights):
    base_score = perf_metrics[0] * scaling_weights[0]
    bonus = perf_metrics[1] * 0.01
    multiplier = 1 + (perf_metrics[2] * 0.1)
    temp_adjust = len(scaling_weights)  # Unused intermediate
    noise_floor = sum(w ** 0.5 for w in scaling_weights) * 0.05  # Computed but irrelevant
    raw_score = (base_score + bonus) * multiplier
    final_score = int(raw_score - noise_floor)  # Final result
    return final_score

# Execute main evaluation
final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")