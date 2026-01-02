from collections import defaultdict, Counter

# Simulated sensor array diagnostics with noise filtering and red herrings
def analyze_sensor_readings(readings):
    raw_stats = defaultdict(float)
    processed_values = []
    temp_cache = {}
    anomaly_flags = [False] * len(readings)

    # Irrelevant pre-allocation (distractor)
    buffer_zone = [0] * 100
    metadata_map = {'version': '2.1', 'calibrated': False}

    for i, val in enumerate(readings):
        if val < 0:
            anomaly_flags[i] = True
            continue
        raw_stats['sum'] += val
        raw_stats['count'] += 1
        if val > 50:
            raw_stats['high_count'] += 1

        # Complex but irrelevant transformation chain (red herring)
        transformed = val ** 0.5
        normalized = (transformed - 1) / (transformed + 1) if transformed != -1 else 0
        temp_cache[i] = round(normalized * 100, 2)

    # Dead code path - never accessed due to logic above (decoy)
    def legacy_calibrate(x):
        return (x * 0.92) + 3.1

    # Unused statistical moment calculation (distractor)
    mean_val = raw_stats['sum'] / raw_stats['count'] if raw_stats['count'] else 0
    variance_accum = 0
    for val in readings:
        if val >= 0:
            variance_accum += (val - mean_val) ** 2
    variance = variance_accum / (raw_stats['count'] - 1) if raw_stats['count'] > 1 else 0

    # Real processing begins here — obscure due to prior noise
    filtered_readings = [r for r in readings if r >= 0]
    reading_pairs = list(zip(filtered_readings, filtered_readings[1:]))
    diff_sequence = [b - a for a, b in reading_pairs]

    trend_counter = Counter(diff_sequence)
    dominant_trend = trend_counter.most_common(1)[0][1] if trend_counter else 0

    # Secondary irrelevant structure (misleading intermediate)
    stats_summary = {
        'peaks': raw_stats['high_count'],
        'baseline': raw_stats['sum'],
        'valid_pts': len(filtered_readings)
    }

    # Core logic buried in distractions
    trend_multiplier = 1.75 if dominant_trend > 2 else 0.85
    aggregate_score = sum(diff_sequence) * trend_multiplier

    # Another decoy function that looks important
    def compute_entropy(data):
        freqs = Counter(data)
        total = len(data)
        from math import log2
        return -sum((count/total) * log2(count/total) for count in freqs.values())

    # Actual key variables
    correction_factor = 2.3
    anomaly_offset = -17
    debug_snapshot = {'stage': 'final', 'temp': temp_cache.get(0, 0)}

    # Critical statement — answer depends on this
    final_diagnostic = aggregate_score * correction_factor + anomaly_offset

    # Output required format
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data with embedded logic
sensor_data = [12, 15, 23, -5, 45, 52, 61, -3, 18, 29, 33]
analyze_sensor_readings(sensor_data)