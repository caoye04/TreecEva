from collections import defaultdict
import math

def analyze_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 0.5
    return trend_score

# Simulate sensor drift compensation (distractor function)
def apply_drift_correction(raw_signal):
    corrected = [x - 0.1 * i for i, x in enumerate(raw_signal)]
    normalization_factor = sum(corrected) / len(corrected)
    return [x / normalization_factor for x in corrected]

# Main evaluation logic
def evaluate_performance(metrics, threshold):
    # Irrelevant preprocessing (distractor)
    adjusted_metrics = defaultdict(float)
    for k, v in metrics.items():
        adjusted_metrics[k] = v * 1.05 if v > 0 else v
    
    # Key intermediate computations
    magnitude = sum(abs(v) for v in metrics.values())
    variance_proxy = sum(v ** 2 for v in metrics.values()) / len(metrics)
    stability = abs(analyze_trend(list(metrics.values())))

    # Red herring: unused complex calculation
    entropy = 0
    total = sum(metrics.values())
    for v in metrics.values():
        if v > 0 and total > 0:
            prob = v / total
            entropy -= prob * math.log(prob)
    
    # Actual scoring logic (depends on magnitude, variance_proxy, and stability)
    base_score = magnitude * 0.4
    if variance_proxy < threshold:
        base_score += stability * 1.2
    else:
        base_score -= 8.5
    
    # Bonus for high consistency (hidden logic path)
    consistency_check = all(abs(v) >= 0.3 for v in metrics.values())
    if consistency_check:
        base_score += 5
    
    # Final adjustment using irrelevant drift-corrected data (but not actually used)
    dummy_signal = [1.2, 0.8, 1.5, 0.7]
    _ = apply_drift_correction(dummy_signal)  # Dead code path
    
    return int(base_score)

# Input data
metric_data = {
    'throughput': 2.1,
    'latency': -1.3,
    'jitter': 0.9,
    'packet_loss': 0.4
}

base_threshold = 3.0

# Trigger key computation
trend_analysis = analyze_trend([metric_data[k] for k in ['throughput', 'latency', 'jitter']])
final_score = evaluate_performance(metric_data, base_threshold)

print(f"Result: {final_score}")