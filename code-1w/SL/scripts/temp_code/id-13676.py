import math

def analyze_signal(patterns):
    # Irrelevant transformation: frequency analysis (dead end)
    freq_map = {}
    for p in patterns:
        freq = sum(1 for bit in p if bit == 1)
        freq_map[frozenset(p)] = freq % 7

    # Distractor: complex but unused structure
    decoy_matrix = [[(i * j + 2) % 5 for j in range(4)] for i in range(4)]

    # Relevant: extract magnitude trends
    magnitudes = [sum(p) * 0.75 for p in patterns]
    normalized = [m / (max(magnitudes) + 1e-8) for m in magnitudes]

    # Slicing operation: windowed trend detection (critical)
    trend_windows = [normalized[i:i+3] for i in range(len(normalized) - 2)]
    trend_slices = [window[1] - window[0] + (window[2] - window[1]) * 0.5 for window in trend_windows]

    return trend_slices

def compute_entropy(seq):
    # Unused function — red herring
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

def validate_sequence(seq):
    # Misleading validation with side calculations
    checksum = 0
    for i, val in enumerate(seq):
        if i % 2 == 0:
            checksum += int(val * 3) % 9
        else:
            checksum -= int(val * 2) % 7
    # This looks important but isn't used in final result
    status_flags = {'valid': checksum == 0, 'peak': max(seq) > 0.8}
    return status_flags

def aggregate_measures(trends, factors):
    # Core computation: weighted diagnostic index
    weighted_sum = 0.0
    for i in range(len(trends)):
        weight = factors[i % len(factors)]
        contribution = trends[i] * weight
        if contribution > 0.1:
            weighted_sum += contribution * 1.2
        else:
            weighted_sum += contribution * 0.8

    # Apply nonlinear compression
    if weighted_sum != 0:
        weighted_sum = math.copysign(math.log(abs(weighted_sum) + 1), weighted_sum)

    # Final adjustment based on slice count parity (hidden logic step)
    adjustment = 1.0 if len(trends) % 2 == 0 else 0.9
    return round(weighted_sum * adjustment, 6)

def main():
    # Input signal pattern (simulated sensor readings)
    raw_patterns = [
        [1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1]
    ]

    # Dead code path: simulated calibration (never called)
    def calibrate_sensor(data):
        return [d * 1.05 for d in data if d > 0.1]

    # Weight vector for aggregation — appears arbitrary but matters
    weights = [0.8, 1.3, 0.9, 1.1]

    # Decoy data structure — looks like it's used
    diagnostics_log = {
        'stages': [],
        'errors': set(),
        'final_score': None
    }

    # Real processing pipeline
    trend_slices = analyze_signal(raw_patterns)
    
    # Another distractor: simulate health check
    system_health = sum(1 for t in trend_slices if abs(t) > 0.3)
    threshold_breached = system_health > 2

    # Critical assignment
    final_diagnostic = aggregate_measures(trend_slices, weights)

    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()