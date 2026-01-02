from collections import defaultdict, Counter

# Simulated sensor array diagnostics with red herrings
def analyze_sensor_array(raw_readings, calibration_offset=0.003):
    # Irrelevant preprocessing block (dead path)
    temp_cache = {}
    for idx, val in enumerate(raw_readings):
        if val < 0:
            temp_cache[idx] = abs(val) ** 0.5

    # Distractor: complex but unused transformation
    normalized = [round((x + calibration_offset) * 1.002, 4) for x in raw_readings]
    inverted_map = {i: 1 / (abs(v) + 1e-5) for i, v in enumerate(normalized)}

    # Actual relevant logic begins here
    signal_peaks = [x for x in raw_readings if x > 75]
    noise_floor = sum(x for x in raw_readings if x < 20) / len(raw_readings)

    # Bit manipulation decoy (unused)
    masked_signals = []
    for p in signal_peaks:
        masked = p & 0xFF ^ 0x5A
        shifted = (masked << 2) | (masked >> 6)
        masked_signals.append(shifted)

    # Real metric accumulation
    metrics_log = defaultdict(int)
    for reading in raw_readings:
        bucket = reading // 10
        metrics_log[bucket] += 1

    # Critical data structure: active_metrics used later
    active_metrics = [v for k, v in sorted(metrics_log.items()) if k >= 5 and v > 1]

    # Distractor: unused recursive function
    def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
    
    sequence_sum = sum(fibonacci(i) for i in range(5))  # Dead computation

    # Decoy statistical analysis
    mean_val = sum(normalized) / len(normalized)
    variance_proxy = sum((x - mean_val) ** 2 for x in normalized) / len(normalized)
    entropy_approx = -sum(p * __import__('math').log(p + 1e-7) for p in inverted_map.values()[:3])

    # Irrelevant string processing (misleading)
    status_flags = ['OK', 'WARN', 'ERROR']
    diagnostic_trace = ''.join(status_flags[i % 3] for i in range(len(raw_readings)))
    flag_count = Counter(diagnostic_trace.split('WARN'))

    # Core calculation chain
    base_score = 0
    for i, metric in enumerate(active_metrics):
        if i % 2 == 0:
            base_score += metric * 3
        else:
            base_score -= metric

    adjustment_factor = len(signal_peaks) - int(noise_floor)
    aggregate_score = base_score * max(adjustment_factor, 1)

    # Key statement with target variable
    final_diagnostic = aggregate_score // (len(active_metrics) or 1)

    # Print required result
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Input data crafted to yield deterministic output
sensor_data = [86, 12, 91, 15, 88, 18, 90, 14, 87, 16, 89, 13, 92, 17, 85, 19]
analyze_sensor_array(sensor_data)