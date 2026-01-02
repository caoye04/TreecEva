def analyze_system_performance(sensor_data, threshold=0.75):
    # Irrelevant helper: computes entropy but not used in final result
    def compute_entropy(data):
        from math import log
        freq = {}
        for x in data:
            freq[x] = freq.get(x, 0) + 1
        total = len(data)
        entropy = 0
        for count in freq.values():
            p = count / total
            entropy -= p * log(p)
        return round(entropy, 4)

    # Distractor: unused variable and dead code path
    baseline_metrics = {'stability': 0.92, 'jitter': 0.03, 'outliers': []}
    if len(sensor_data) > 100:
        baseline_metrics['outliers'] = [x for x in sensor_data if x < 0.1]

    # Real processing begins
    normalized = [x / max(sensor_data) for x in sensor_data]
    segments = [normalized[i:i+5] for i in range(0, len(normalized), 5)]
    
    # Use enumerate and conditional expression (required Python features)
    segment_peaks = []
    for idx, seg in enumerate(segments):
        peak = max(seg) if len(seg) > 0 else 0
        segment_peaks.append((idx, peak))

    # Compute activation_map using zip (required feature)
    indices, values = zip(*segment_peaks)
    activation_map = {i: v > threshold for i, v in zip(indices, values)}

    # Track active zones with set operations (required concept)
    active_zones = set(i for i, active in activation_map.items() if active)
    inactive_zones = set(range(len(segments))) - active_zones

    # Distractor: irrelevant statistical computation
    avg_peak = sum(values) / len(values) if values else 0
    fluctuation_index = len([i for i in range(1, len(values)) if values[i] != values[i-1]])

    # Core logic hidden among distractions
    zone_ratio = len(active_zones) / len(segments) if segments else 0
    system_yield = len([v for v in values if v >= threshold])

    # Another red herring: complex but unused bitwise calculation
    security_hash = 0
    for i, val in enumerate(values):
        shifted = int(val * 100) << 2
        security_hash ^= shifted + (i & 7)

    # Critical variables
    monitor_threshold = 24 if zone_ratio >= 0.6 else 12
    recovery_sequence = [1, 1]
    for _ in range(5):
        recovery_sequence.append(recovery_sequence[-1] + recovery_sequence[-2])
    
    # Final computation buried in middle of noise
    final_diagnostic = monitor_threshold * system_yield

    # More distractors: unused container and redundant transformation
    diagnostic_log = {
        'readings': sensor_data,
        'normalized': normalized,
        'peak_distribution': {k: v for k, v in enumerate(values)},
        'activation_count': len(active_zones)
    }

    # Print required output format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulate deterministic input
import random
random.seed(42)
data_sample = [0.3, 0.82, 0.15, 0.88, 0.76, 0.41, 0.91, 0.22, 0.77, 0.83, 0.69, 0.94, 0.52, 0.85]
analyze_system_performance(data_sample)